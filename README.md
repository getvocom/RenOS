# RenOS website

Static marketing site for RenOS, the AI operating system for teams, from Vocom AI.
Dark visual design from the approved homepage; sitemap, titles, keywords and copy from the RenOS website spec.

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

This builds the staging site for https://getvocom.github.io/RenOS/ (every page `noindex`, links prefixed with `/RenOS`).

When the site moves to https://renos.vocom.ai, build with `--prod` instead. That removes `noindex`, drops the `/RenOS` prefix and writes `sitemap.xml` and `robots.txt`.

## Switches in `_build/content.py`

- `SHOW_PRICES = False`: pricing cards, the comparison table and the private-deployment card show "Talk to Sales". Set to `True` once prices are cleared for public use.
- `FORM_ENDPOINT = ""`: the pilot and contact forms tell visitors nothing was sent. Set it to a form service URL (for example a Formspree endpoint) to make them work.

## Adding product screenshots

Drop an image into `images/` with one of these names (`.webp` preferred, under 200 KB), then rebuild. It replaces the HTML mockup in that spot.

| File name | Where it appears |
|---|---|
| `home-hero` | Home hero |
| `product-hero` | Product overview hero |
| `product-chat`, `product-builder`, `product-agents` | Mode page heroes |
| `product-routing`, `product-audit-trail`, `product-admin` | Feature page heroes |
| `models-hero`, `pilot-hero` | Models and pilot heroes |
| `teams-<slug>` (e.g. `teams-sales`) | Team page heroes |
| `industries-<slug>` (e.g. `industries-credit-unions`) | Industry page heroes |

## Not built yet (blocked by the spec's open items)

- Privacy and Terms pages: need real legal text.
- Team page: needs names, roles, photos and permission.
- Blog posts: each needs a verified, current news hook.
