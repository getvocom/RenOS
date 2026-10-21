#!/usr/bin/env python3
"""Build the RenOS static site.

    python3 _build/build.py            # staging build for GitHub Pages (noindex, /RenOS base path)
    python3 _build/build.py --prod     # production build for https://renos.vocom.ai
    python3 _build/build.py --out DIR  # write somewhere else (used for checks)

Standard library only. Content lives in content.py; this file is layout and components.
"""
import html
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import content as C  # noqa: E402

SITE = "https://renos.vocom.ai"
PROD = "--prod" in sys.argv
BASE = "" if PROD else "/RenOS"
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else ROOT
NOINDEX_ALL = not PROD
IMAGE_EXTS = ("webp", "avif", "svg", "png", "jpg", "jpeg")

e = html.escape


# ---------------------------------------------------------------- helpers

def find_shot(name):
    """Return the site path of a screenshot in /images if one has been added."""
    for ext in IMAGE_EXTS:
        if os.path.isfile(os.path.join(ROOT, "images", f"{name}.{ext}")):
            return f"/images/{name}.{ext}"
    return None


def btn(label, href, kind="primary", size=""):
    cls = f"btn btn--{kind}" + (f" btn--{size}" if size else "")
    return f'<a class="{cls}" href="{href}">{e(label)}</a>'


def section_head(s):
    out = []
    if s.get("eyebrow"):
        out.append(f'<p class="eyebrow">{e(s["eyebrow"])}</p>')
    if s.get("h2"):
        out.append(f'<h2 class="section-title">{e(s["h2"])}</h2>')
    if s.get("lede"):
        out.append(f'<p class="section-lede">{s["lede"]}</p>')
    return f'<header class="section-head">{"".join(out)}</header>' if out else ""


# ---------------------------------------------------------------- visuals

def globe():
    stars = "".join(
        f'<circle cx="{x}" cy="{y}" r="{r}" opacity="{o}"/>' for x, y, r, o in C.STARS
    )
    nodes = [(418, 302, "#5fd0a0"), (101, 302, "#f2b45a"), (335, 133, "#8f80f7"),
             (184, 133, "#6aa8ff"), (260, 407, "#f08bb8")]
    links = "".join(f'<line x1="260" y1="260" x2="{x}" y2="{y}"/>' for x, y, _ in nodes)
    dots = "".join(
        f'<circle cx="{x}" cy="{y}" r="14" fill="#12151d" stroke="{c}" stroke-opacity=".35"/>'
        f'<circle cx="{x}" cy="{y}" r="4.5" fill="{c}"/>' for x, y, c in nodes)
    lat = [(82, 102.5, 16), (157, 177.5, 28), (260, 205, 32.5), (362, 177.5, 28), (437, 102.5, 16)]
    lon = [201.5, 192.5, 157, 131.5, 70, 35.5]
    lines = "".join(f'<ellipse cx="260" cy="{cy}" rx="{rx}" ry="{ry}"/>' for cy, rx, ry in lat)
    lines += "".join(f'<ellipse cx="260" cy="260" rx="{rx}" ry="205"/>' for rx in lon)
    return f'''<svg class="globe" viewBox="0 0 520 520" xmlns="http://www.w3.org/2000/svg">
<defs><filter id="glow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
<circle cx="260" cy="260" r="250" fill="#8f80f7" opacity="0.12"/><circle cx="260" cy="260" r="205" fill="#fff" opacity="0.05"/>
<g class="globe-lines">{lines}</g><g class="globe-stars">{stars}</g><g class="globe-links">{links}</g>
<g filter="url(#glow)">{dots}</g>
<circle class="globe-hub-pulse" cx="260" cy="260" r="28" fill="none" stroke="#5ee0ff" stroke-opacity=".6"/>
<g filter="url(#glow)"><circle cx="260" cy="260" r="28" fill="#181c26" stroke="#5ee0ff" stroke-opacity=".5"/><circle cx="260" cy="260" r="7" fill="#5ee1ff"/></g>
</svg>'''


def panel(p):
    """A small product-UI card built from real text: [('pill', text), ('kv', k, v), ('note', text), ('bar', label, pct)]."""
    rows = []
    for item in p:
        kind = item[0]
        if kind == "pill":
            rows.append(f'<span class="pill pill--accent"><span class="dot"></span>{e(item[1])}</span>')
        elif kind == "ok":
            rows.append(f'<span class="pill pill--light"><span class="dot dot--green"></span>{e(item[1])}</span>')
        elif kind == "label":
            rows.append(f'<p class="float-label">{e(item[1])}</p>')
        elif kind == "kv":
            rows.append(f'<div class="ui-kv"><span>{e(item[1])}</span><strong>{e(item[2])}</strong></div>')
        elif kind == "note":
            rows.append(f'<p class="ui-note">{e(item[1])}</p>')
        elif kind == "bar":
            rows.append(f'<div class="ui-bar"><span>{e(item[1])}</span><i style="--w:{item[2]}"></i></div>')
        elif kind == "split":
            cols = "".join(f'<div class="ui-col"><p class="float-label">{e(a)}</p><p class="ui-note">{e(b)}</p></div>' for a, b in item[1])
            rows.append(f'<div class="ui-split">{cols}</div>')
    return f'<div class="card ui-panel" aria-hidden="true">{"".join(rows)}</div>'


# ---------------------------------------------------------------- product showcases
# HTML rebuilds of the Figma product screens. Names, prices and vendors are generic on purpose.

def ui(title, body, badge="", wide=False):
    b = f'<span class="ui-badge">{e(badge)}</span>' if badge else ""
    return (f'<div class="ui{" ui--wide" if wide else ""}" aria-hidden="true"><div class="ui-top">'
            f'<span class="ui-dots"><i></i><i></i><i></i></span><span class="ui-title">{e(title)}</span>{b}</div>'
            f'<div class="ui-body">{body}</div></div>')


def ui_rows(pairs):
    return '<dl class="ui-dl">' + "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in pairs) + "</dl>"


def ui_btns(*labels):
    return '<div class="ui-btns">' + "".join(
        f'<span class="ui-btn{" ui-btn--ghost" if i else ""}">{e(l)}</span>' for i, l in enumerate(labels)) + "</div>"


def sc_signin():
    return ui("Sign In", '''<div class="ui-center"><span class="brand"><span class="brand-mark"></span>RenOS</span>
<p class="ui-muted">One governed workspace for every model.</p>
<p class="ui-h">Sign in with your company account</p>
<p class="ui-muted">Your role and policies are already set by your admin. There is nothing to configure.</p>
<span class="ui-btn ui-btn--block">Continue With Company SSO</span><span class="ui-btn ui-btn--ghost ui-btn--block">Use Work Email</span>
<p class="ui-foot"><span class="dot dot--green"></span>Every task is logged for your organization</p></div>''')


def sc_workspace():
    approvals = [("Post product announcement", "Marketing agent · draft ready", "Posting"),
                 ("Run migration script on staging", "Developer agent · 14 files changed", "Code execution"),
                 ("Move to the next project stage", "Report accepted by reviewer", "Stage gate")]
    agents = [("Research: market scan", "Running"), ("Developer: onboarding flow", "Running"),
              ("Marketing: homepage copy", "Waiting")]
    ap = "".join(f'<li><div><strong>{e(a)}</strong><span>{e(b)}</span></div><em>{e(c)}</em></li>' for a, b, c in approvals)
    ag = "".join(f'<li><div><strong>{e(a)}</strong></div><em class="{"is-run" if s == "Running" else ""}">{e(s)}</em></li>' for a, s in agents)
    return ui("Workspace", f'''<p class="ui-h ui-h--lg">Good afternoon. What should we work on?</p>
<div class="ui-input">Ask RenOS, or type / for commands<span class="ui-btn">Send</span></div>
<div class="ui-chips"><span>Plan this week's launch</span><span>Summarize research notes</span><span>Draft the pricing page</span></div>
<div class="ui-cols"><div><p class="ui-label">Ready for Review <b>3</b></p><ul class="ui-list">{ap}</ul></div>
<div><p class="ui-label">Agents at Work</p><ul class="ui-list">{ag}</ul></div></div>''', "Chat · Builder · Agent", wide=True)


def sc_task():
    return ui("Agent · Intake Summaries", '''<p class="ui-muted">Client operations</p>
<p class="ui-prompt">Summarize these 12 client intake forms and flag missing insurance details.</p>
<div class="ui-route"><p><span class="dot"></span><strong>Routed to an approved model</strong> <span class="ui-tag">Approved supply</span></p>
<p class="ui-muted">Why: the forms contain personal client data. Your policy allows approved models only, and this task needs long-document reasoning.</p></div>
''' + ui_rows([("Estimated cost", "Checked before it runs"), ("Budget", "Client operations · within cap")]) + ui_btns("Run Task"), "Agent Mode")


def sc_budgets():
    teams = [("Client operations", "62%", "On track"), ("Front desk", "38%", "On track"), ("Finance", "91%", "Near cap")]
    bars = "".join(f'<div class="ui-meter"><div><strong>{e(n)}</strong><span>{e(s)}</span></div><i style="--w:{w}"{" class=hot" if s == "Near cap" else ""}></i></div>' for n, w, s in teams)
    return ui("Budgets and Spend Caps", f'''<p class="ui-muted">This month, by team</p>{bars}
''' + ui_rows([("Alerts", "Admins hear as each team nears its cap"), ("Agent mode", "Each task stops at its own ceiling"),
               ("At the cap", "Work pauses · owners can approve more")]) + ui_btns("Save Budgets"))


def sc_supply():
    rows_ = [("Personal client data", ["Approved models only"]), ("Confidential", ["Approved models", "Your own keys"]),
             ("General", ["Any approved model"])]
    tr = "".join(f'<tr><td>{e(a)}</td><td>{"".join(f"<span class=ui-tag>{e(x)}</span>" for x in b)}</td></tr>' for a, b in rows_)
    return ui("Model Supply Policy", f'''<table class="ui-table"><thead><tr><th>Data class</th><th>Allowed models</th></tr></thead><tbody>{tr}</tbody></table>
<p class="ui-foot"><span class="dot dot--green"></span>Your own model keys · connected on Enterprise</p>''', "Policy: Sensitive Data")


def sc_audit():
    return ui("Audit Record · Task A-20931", ui_rows([
        ("When", "Oct 14 · 10:42"), ("Who", "Client operations"), ("Mode", "Agent mode, 3 rounds"),
        ("Model", "Approved model"), ("Policy", "Personal data requires approved models"),
        ("Cost", "Recorded in the admin view"), ("Overrides", "None")]) +
        '<p class="ui-foot">Kept 90 days on Pro · one year or more on Enterprise</p>' + ui_btns("Export Record"), "Exportable")


def sc_limit():
    return ui("Budget Limit Reached", '''<p class="ui-prompt">This task needs more than Finance has left this month.</p>''' +
              ui_btns("Request Approval", "Use a Lower-Cost Model") +
              '''<div class="ui-route"><p class="ui-muted">Sent to the budget owner</p><p><strong>Approve a one-time increase for Finance?</strong></p>''' +
              ui_btns("Approve", "Decline") + '''</div>
<p class="ui-foot"><span class="dot dot--amber"></span>Agent run stopped at its per-task ceiling after 7 rounds</p>''', "Finance · At Cap")


def sc_oversight():
    rows_ = [("12:44", "Front desk", "Chat", "Routed", "Personal data, so approved models only"),
             ("12:41", "Finance", "Builder", "Routed", "Confidential, so an approved model"),
             ("12:38", "Client ops", "Agent", "Routed", "Low sensitivity, so a lower-cost model"),
             ("12:31", "Marketing", "Chat", "Blocked", "Client assets aren't allowed on this model"),
             ("12:20", "Finance", "Chat", "Allowed", "Standard policy")]
    tr = "".join(f'<tr><td>{a}</td><td>{e(b)}</td><td>{e(c)}</td><td><span class="ui-out ui-out--{d.lower()}">{d}</span></td><td>{e(r)}</td></tr>' for a, b, c, d, r in rows_)
    attn = ["2 exception requests are waiting for review", "Finance is close to its spend cap",
            "One rule has had no hits this month"]
    li = "".join(f"<li>{e(x)}</li>" for x in attn)
    return ui("Oversight", f'''<p class="ui-muted">Every AI task across your organization, whichever team ran it.</p>
<div class="ui-scroll"><table class="ui-table"><thead><tr><th>Time</th><th>Team</th><th>Mode</th><th>Outcome</th><th>Routing rationale</th></tr></thead><tbody>{tr}</tbody></table></div>
<p class="ui-label">Needs Attention</p><ul class="ui-attn">{li}</ul>''', "Admin", wide=True)


SHOWCASES = {"signin": sc_signin, "workspace": sc_workspace, "task": sc_task, "budgets": sc_budgets,
             "supply": sc_supply, "audit": sc_audit, "limit": sc_limit, "oversight": sc_oversight}


def visual(v, alt=""):
    if not v:
        return ""
    if isinstance(v, str) and v in SHOWCASES:
        return SHOWCASES[v]()
    if isinstance(v, dict) and v.get("shot"):
        src = find_shot(v["shot"])
        if src:
            return (f'<figure class="shot"><img src="{src}" alt="{e(v.get("alt", alt))}" '
                    f'loading="lazy" decoding="async"></figure>')
        return visual(v.get("fallback"), alt)
    if v == "globe":
        return f'''<div class="hero-visual" aria-hidden="true">{globe()}
<div class="float-card float-card--rationale"><p class="float-label">ROUTING RATIONALE</p><p class="float-text">Confidential tenant data, so policy sent this task to an approved model.</p></div>
<div class="float-card float-card--session"><span class="pill pill--light"><span class="dot dot--green"></span>Audit entry written</span><p class="float-meta">who · task · model · policy · result</p></div></div>'''
    if isinstance(v, list):
        return panel(v)
    return ""


# ---------------------------------------------------------------- sections

def hero(s, crumbs_html):
    h1 = e(s["h1"])
    if s.get("h1_accent"):
        h1 += f' <span class="gradient-text">{e(s["h1_accent"])}</span>'
    buttons = "".join(btn(*b) for b in s.get("buttons", []))
    proof = "".join(f'<li class="pill"><span class="dot dot--green"></span>{e(p)}</li>' for p in s.get("proof", []))
    vis = visual(s.get("visual"), s.get("visual_alt", ""))
    grid = "hero-grid" if vis else "hero-grid hero-grid--solo"
    return f'''<section class="hero">{crumbs_html}<div class="container {grid}"><div class="hero-copy">
<span class="pill pill--cyan"><span class="dot"></span>{e(s["eyebrow"])}</span>
<h1 class="hero-title">{h1}</h1><p class="hero-lede">{s["lede"]}</p>
{f'<div class="hero-actions">{buttons}</div>' if buttons else ''}
{f'<ul class="hero-proof">{proof}</ul>' if proof else ''}</div>{vis}</div></section>'''


def cards(s):
    cols = s.get("cols", 3)
    items = []
    for c in s["items"]:
        tag = "a" if c.get("href") else "article"
        href = f' href="{c["href"]}"' if c.get("href") else ""
        accent = f' style="--accent:{c["accent"]}"' if c.get("accent") else ""
        top = ""
        if c.get("num"):
            top = f'<span class="step-num">{e(c["num"])}</span>'
        elif s.get("icons", True):
            top = '<span class="cap-icon" aria-hidden="true"></span>'
        more = f'<span class="card-more">{e(c.get("more", "Learn More"))} →</span>' if c.get("href") else ""
        quote = f'<p class="card-quote">“{e(c["quote"])}”</p>' if c.get("quote") else ""
        demo = ""
        if c.get("demo"):
            demo = f'<div class="step-demo"><span class="pill pill--accent"><span class="dot"></span>{e(c["demo"][0])}</span><p class="step-demo-text">{e(c["demo"][1])}</p></div>'
        items.append(f'<{tag} class="card capability{" card--link" if href else ""}"{href}{accent}>{top}'
                     f'<h3>{e(c["title"])}</h3>{quote}<p>{c.get("text", "")}</p>{demo}{more}</{tag}>')
    return f'<div class="grid-{cols}">{"".join(items)}</div>'


def rows(s):
    out = []
    for i, r in enumerate(s["items"]):
        bullets = "".join(f"<li>{b}</li>" for b in r.get("bullets", []))
        link = f'<p class="row-link"><a href="{r["link"][1]}">{e(r["link"][0])} →</a></p>' if r.get("link") else ""
        out.append(f'''<div class="feature-row{" feature-row--flip" if i % 2 else ""}"><div class="feature-copy">
<h3>{e(r["title"])}</h3><p>{r["text"]}</p>{f'<ul class="feature-list">{bullets}</ul>' if bullets else ''}{link}</div>
<div class="feature-visual">{visual(r.get("visual"), r["title"])}</div></div>''')
    return "".join(out)


def chips(s):
    return '<ul class="tag-list">' + "".join(
        f'<li><a href="{h}">{e(t)}</a></li>' if h else f"<li>{e(t)}</li>" for t, h in s["items"]) + "</ul>"


def faq(s):
    return '<div class="faq">' + "".join(
        f'<details class="card faq-item"><summary><h3>{e(title_case(q))}</h3></summary><p>{a}</p></details>'
        for q, a in s["items"]) + "</div>"


def prose(s):
    return f'<div class="prose">{s["html"]}</div>'


def timeline_card(s):
    steps = "".join(
        f'<li><span class="timeline-dot{" timeline-dot--green" if i == len(s["timeline"]) - 1 else ""}"></span>'
        f'<div><time>{e(t)}</time><strong>{e(a)}</strong><span>{e(b)}</span></div></li>'
        for i, (t, a, b) in enumerate(s["timeline"]))
    return (f'<article class="card session-card"><p class="eyebrow">In Plain Language</p>'
            f'<p class="session-summary">{e(s["summary"])}</p><ol class="timeline">{steps}</ol></article>')


def split(s):
    bullets = "".join(f"<li>{b}</li>" for b in s.get("bullets", []))
    right = timeline_card(s) if s.get("timeline") else visual(s.get("visual"))
    btns = "".join(btn(*b) for b in s.get("buttons", []))
    return f'''<div class="session-grid"><div>{section_head(s)}
{f'<ul class="feature-list">{bullets}</ul>' if bullets else ''}{f'<div class="hero-actions">{btns}</div>' if btns else ''}</div>{right}</div>'''


def flow(s):
    steps = "".join(
        f'<li class="flow-step"><div class="flow-head"><span class="flow-num">{i + 1}</span><h3>{e(t)}</h3></div>'
        f'{visual(v)}<p>{cap}</p></li>' for i, (t, v, cap) in enumerate(s["steps"]))
    return f'<ol class="flow">{steps}</ol>'


def pick(p, key):
    """Price-dependent copy: the priced version only when prices are switched on."""
    return p.get(key + "_priced") if (C.SHOW_PRICES and p.get(key + "_priced")) else p.get(key)


def pricing(s):
    toggle = ""
    if C.SHOW_PRICES:
        toggle = '''<div class="billing" role="group" aria-label="Billing period">
<button type="button" class="is-on" data-bill="annual" aria-pressed="true">Annual</button>
<button type="button" data-bill="monthly" aria-pressed="false">Monthly</button>
<span class="billing-note">Annual billing saves 17%</span></div>'''
    plans = []
    for p in s["plans"]:
        feats = "".join(f"<li>{f}</li>" for f in (pick(p, "features") or []))
        if C.SHOW_PRICES and p.get("price"):
            mon = p.get("price_monthly")
            price = (f'<p class="plan-price"><span data-annual>{e(p["price"])}</span>'
                     + (f'<span data-monthly hidden>{e(mon)}</span>' if mon else "")
                     + f' <small>{e(p["unit"])}</small></p><p class="plan-terms">{e(p["terms"])}</p>')
        else:
            price = '<p class="plan-price">Talk to Sales</p>'
        tag = f'<span class="plan-tag">{e(p["tag"])}</span>' if p.get("tag") else ""
        plans.append(f'''<article class="card plan{" plan--featured" if p.get("featured") else ""}">{tag}
<h3>{e(p["name"])}</h3><p class="plan-blurb">{e(p["blurb"])}</p>{price}
{btn(*pick(p, "cta"), "primary" if p.get("featured") else "ghost")}<ul class="feature-list">{feats}</ul></article>''')
    extras = "".join(
        f'<article class="card plan-extra"><h3>{e(x["title"])}</h3><p>{pick(x, "text")}</p></article>' for x in s.get("extras", []))
    return f'{toggle}<div class="grid-3 plans">{"".join(plans)}</div>' + (f'<div class="grid-2 plan-extras">{extras}</div>' if extras else "")


def compare(s):
    head = "".join(f"<th scope=col>{e(h)}</th>" for h in s["cols"])
    body = "".join(
        f'<tr><th scope="row">{e(r[0])}</th>' + "".join(
            f'<td>{"<span class=muted>Not included</span>" if c is None else e(c)}</td>' for c in (pick(r[1], "cells") if isinstance(r[1], dict) else r[1:])) + "</tr>"
        for r in s["rows"])
    return f'<div class="card table-wrap"><table class="compare"><thead><tr><th scope="col">Feature</th>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def form(s):
    fields = []
    for f in s["fields"]:
        name, label, kind = f[0], f[1], f[2]
        req = " required" if (len(f) < 4 or f[3]) else ""
        fid = f"f-{name}"
        if kind == "select":
            opts = "".join(f'<option value="{v}">{e(t)}</option>' for v, t in f[4])
            ctl = f'<select id="{fid}" name="{name}"{req}>{opts}</select>'
        elif kind == "textarea":
            ctl = f'<textarea id="{fid}" name="{name}" rows="4"{req}></textarea>'
        else:
            auto = {"email": "email", "name": "name", "company": "organization"}.get(name, "off")
            ctl = f'<input id="{fid}" name="{name}" type="{kind}" autocomplete="{auto}"{req}>'
        fields.append(f'<div class="field{" field--wide" if kind == "textarea" else ""}"><label for="{fid}">{e(label)}</label>{ctl}</div>')
    action = C.FORM_ENDPOINT
    return f'''<form class="card lead-form" method="post" action="{action or "#"}" data-endpoint="{"1" if action else ""}">
<div class="form-grid">{"".join(fields)}</div>
<button class="btn btn--primary" type="submit">{e(s["submit"])}</button>
<p class="form-status" role="status" aria-live="polite"></p></form>'''


def toc(s):
    return '<nav class="card toc" aria-label="On this page"><p class="eyebrow">On This Page</p><ol>' + "".join(
        f'<li><a href="#{a}">{e(t)}</a></li>' for a, t in s["items"]) + "</ol></nav>"


RENDER = {"cards": cards, "rows": rows, "chips": chips, "faq": faq, "prose": prose,
          "pricing": pricing, "form": form, "toc": toc, "flow": flow, "compare": compare}


def section(s):
    kind = s["type"]
    sid = f' id="{s["id"]}"' if s.get("id") else ""
    if kind == "split":
        return f'<section class="section"{sid}><div class="container">{split(s)}</div></section>'
    if kind == "problems":
        return f'<section class="problems"{sid} aria-label="The problem"><div class="container">{cards({**s, "icons": False})}</div></section>'
    body = RENDER[kind](s)
    return f'<section class="section{" section--tight" if s.get("tight") else ""}"{sid}><div class="container">{section_head(s)}{body}</div></section>'


def cta_band(c):
    return f'''<section class="cta" id="cta"><div class="container"><div class="cta-panel">
<h2>{e(c.get("h2", "See RenOS Run on Your Own Work"))}</h2>
<p>{c.get("text", "Bring one real task. We'll route it live, with the routing rationale and audit trail included.")}</p>
<div class="hero-actions hero-actions--center">{btn("Book a Demo", "/contact", "primary", "lg")}{btn("Start a Pilot", "/pilot", "ghost", "lg")}</div>
</div></div></section>'''


# ---------------------------------------------------------------- chrome

def nav():
    groups = []
    for label, cols in C.NAV:
        if isinstance(cols, str):
            groups.append(f'<a class="nav-top" href="{cols}">{e(label)}</a>')
            continue
        col_html = []
        for heading, links in cols:
            items = "".join(
                f'<li><a href="{h}"><strong>{e(t)}</strong><span>{e(d)}</span></a></li>' for t, h, d in links)
            col_html.append(f'<div class="mega-col"><p class="mega-head">{e(heading)}</p><ul>{items}</ul></div>')
        groups.append(f'''<div class="nav-item"><button class="nav-top" type="button" aria-expanded="false">{e(label)}<span class="caret" aria-hidden="true"></span></button>
<div class="mega"><div class="mega-inner">{"".join(col_html)}</div></div></div>''')
    return f'''<header class="site-header" id="top"><nav class="container nav" aria-label="Primary">
<a class="brand" href="/" aria-label="RenOS home"><span class="brand-mark" aria-hidden="true"></span>RenOS</a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-menu" aria-label="Open menu"><span></span></button>
<div class="nav-menu" id="nav-menu"><div class="nav-groups">{"".join(groups)}</div>
<div class="nav-actions"><a class="nav-sales" href="/contact">Talk to Sales</a>{btn("Start a Pilot", "/pilot", "primary", "sm")}</div></div>
</nav></header>'''


def footer():
    cols = "".join(
        f'<div class="footer-col"><p class="footer-head">{e(h)}</p><ul>' +
        "".join(f'<li><a href="{u}">{e(t)}</a></li>' for t, u in links) + "</ul></div>"
        for h, links in C.FOOTER)
    return f'''<footer class="site-footer"><div class="container">
<div class="footer-top"><div class="footer-brand"><a class="brand" href="/"><span class="brand-mark" aria-hidden="true"></span>RenOS</a>
<p>{e(C.FACTS["tagline"])}. {e(C.FACTS["status"])}.</p></div><div class="footer-cols">{cols}</div></div>
<div class="footer-row"><span>RenOS is from <a href="https://www.vocom.ai">Vocom AI</a></span><span class="footer-rule" aria-hidden="true"></span><span>© 2026 Vocom AI</span></div>
</div></footer>'''


def crumbs(page):
    if page["route"] == "/":
        return "", None
    trail = [("Home", "/")] + page.get("crumbs", []) + [(page["crumb"], page["route"])]
    vis = " <span aria-hidden=\"true\">/</span> ".join(
        f'<a href="{u}">{e(t)}</a>' if i < len(trail) - 1 else f'<span aria-current="page">{e(t)}</span>'
        for i, (t, u) in enumerate(trail))
    ld = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": t, "item": SITE + ("" if u == "/" else u)}
        for i, (t, u) in enumerate(trail)]}
    return f'<nav class="container crumbs" aria-label="Breadcrumb">{vis}</nav>', ld


MINOR = {"a", "an", "the", "and", "but", "or", "nor", "for", "so", "yet", "as", "at", "by", "in", "of",
         "on", "per", "to", "up", "via", "vs", "with", "from", "into", "than"}


def title_case(s):
    """Title Case for headings: capitalize every word except minor ones, keep existing capitals (AI, RenOS)."""
    words = s.split(" ")
    out = []
    for i, w in enumerate(words):
        if i and w.lower() in MINOR:
            out.append(w)
        else:
            out.append(w[:1].upper() + w[1:])
    return " ".join(out)


def strip_tags(s):
    return " ".join(re.sub(r"<[^>]+>", "", s).split())


def page_html(page):
    crumb_html, crumb_ld = crumbs(page)
    canonical = SITE + ("" if page["route"] == "/" else page["route"])
    graph = []
    if page["route"] == "/":
        graph += [
            {"@type": "Organization", "name": "RenOS", "url": SITE,
             "logo": SITE + "/assets/og-image.png",
             "parentOrganization": {"@type": "Organization", "name": "Vocom AI", "url": "https://www.vocom.ai"}},
            {"@type": "WebSite", "name": "RenOS", "url": SITE}]
    if page.get("software"):
        graph.append({"@type": "SoftwareApplication", "name": page.get("software_name", "RenOS"),
                      "applicationCategory": "BusinessApplication", "operatingSystem": "Web",
                      "description": page["description"], "url": canonical})
    for s in page["sections"]:
        if s["type"] == "faq":
            graph.append({"@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": title_case(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                for q, a in s["items"]]})
    if crumb_ld:
        graph.append(crumb_ld)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False) if graph else ""

    robots = '<meta name="robots" content="noindex, nofollow" />' if (NOINDEX_ALL or page.get("noindex")) else ""
    body = hero(page["hero"], crumb_html) + "".join(section(s) for s in page["sections"])
    if page.get("cta", True) is not False:
        body += cta_band(page.get("cta") or {})
    return f'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{e(page["title"])}</title>
<meta name="description" content="{e(page["description"])}" />
{robots}
<link rel="canonical" href="{canonical}" />
<meta property="og:type" content="website" />
<meta property="og:title" content="{e(page["title"])}" />
<meta property="og:description" content="{e(page["description"])}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:image" content="{SITE}/assets/og-image.png" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="theme-color" content="#0a0c11" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400&family=Space+Grotesk:wght@400;500;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/assets/css/site.css" />
{f'<script type="application/ld+json">{ld}</script>' if ld else ''}
</head>
<body>
<a class="skip-link" href="#main">Skip to Content</a>
<div class="bg-orb bg-orb--1" aria-hidden="true"></div><div class="bg-orb bg-orb--2" aria-hidden="true"></div>
{nav()}
<main id="main">{body}</main>
{footer()}
<script src="/assets/js/site.js" defer></script>
</body>
</html>
'''


def rebase(doc):
    """Prefix site-relative URLs with the base path (GitHub Pages serves the site under /RenOS)."""
    if not BASE:
        return doc
    return re.sub(r'(href|src|action)="/(?!/)', lambda m: f'{m.group(1)}="{BASE}/', doc)


def out_path(route):
    if route == "/":
        return os.path.join(OUT, "index.html")
    return os.path.join(OUT, route.strip("/") + ".html")


def main():
    pages = C.pages()
    # clear previously generated html (keep anything outside the generated set)
    manifest = os.path.join(OUT, ".generated")
    if os.path.isfile(manifest):
        for rel in open(manifest).read().split():
            p = os.path.join(OUT, rel)
            if os.path.isfile(p):
                os.remove(p)
    written = []
    for page in pages:
        path = out_path(page["route"])
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(rebase(page_html(page)))
        written.append(os.path.relpath(path, OUT))
        d = len(page["description"])
        if not page.get("noindex") and not 140 <= d <= 155:
            print(f"  note: {page['route']} description is {d} chars")
        if len(page["title"]) > 60:
            print(f"  note: {page['route']} title is {len(page['title'])} chars")
    # sitemap and robots for the production domain
    if PROD:
        urls = "".join(f"<url><loc>{SITE}{'' if p['route'] == '/' else p['route']}</loc></url>"
                       for p in pages if not p.get("noindex"))
        open(os.path.join(OUT, "sitemap.xml"), "w").write(
            f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
        open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
        written += ["sitemap.xml", "robots.txt"]
    if OUT != ROOT:
        for d in ("assets", "images"):
            src = os.path.join(ROOT, d)
            if os.path.isdir(src):
                shutil.copytree(src, os.path.join(OUT, d), dirs_exist_ok=True)
        shutil.copy(os.path.join(ROOT, "favicon.svg"), OUT)
    open(manifest, "w").write("\n".join(written) + "\n")
    print(f"Built {len(pages)} pages into {OUT} ({'production' if PROD else 'staging'}, base '{BASE}')")


if __name__ == "__main__":
    main()
