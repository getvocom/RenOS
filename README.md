# RenOS website

Static marketing site for RenOS by Ren Group: the governance layer for AI at work.
Sections, copy and numbers follow the Atlas design (Option A); titles, meta descriptions and keyword pages follow the RenOS website spec.

The HTML pages are generated. Edit the files in `_build/`, then rebuild.

## Structure

```
_build/build.py     Layout, components, SEO tags and schema
_build/content.py   Every page's copy, titles, descriptions and FAQs, plus switches
_build/stars.py     Star positions for the hero globe
assets/css/site.css Styles
assets/js/site.js   Mega menu, mobile menu, forms, pricing toggle
assets/og-image.png Social share image
images/             Product screenshots (see below)
*.html, product/, teams/, industries/   Generated pages (don't edit by hand)
```

## Build

```bash
python3 _build/build.py
```

This builds the site for https://rengroup.ai with every page set to `noindex` while it is pre-launch. It also writes the `CNAME` file GitHub Pages needs for the custom domain.

When you are ready for search engines, build with `--prod`. That removes `noindex` and writes `sitemap.xml` and `robots.txt`. The domain is set by `DOMAIN` at the top of `_build/build.py`.

## Switches in `_build/content.py`

- `SHOW_PRICES = True`: shows the Atlas prices and dollar figures (plans, comparison table, credit rate, receipts, sample budgets). Set to `False` to replace them with "Talk to Sales" and credit-only wording everywhere.
- `FORM_ENDPOINT = ""`: the pilot and contact forms tell visitors nothing was sent. Set it to a form service URL (for example a Formspree endpoint) to make them work; a successful send goes to `/thanks`.
- `APP_URL`: where Sign In hands off (`{APP_URL}/login`).

## Adding product screenshots

Drop an image into `images/` with one of these names (`.webp` preferred, under 200 KB), then rebuild. It replaces the HTML mockup in that spot.

| File name | Where it appears |
|---|---|
| `home-hero` | Home hero |
| `product-hero` | Product overview hero |
| `product-chat`, `product-builder`, `product-agents` | Mode page heroes |
| `product-routing`, `product-audit-trail`, `product-admin` | Feature page heroes |
| `models-hero` | Models hero |
| `teams-<slug>` (e.g. `teams-sales`) | Team page heroes |
| `industries-<slug>` (e.g. `industries-credit-unions`) | Industry page heroes |

## Not built yet (blocked by the spec's open items)

- Privacy and Terms pages: need real legal text.
- Team photos for the About page (names and roles are in from the Atlas design).
- Blog posts: each needs a verified, current news hook.
