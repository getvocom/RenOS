# agentOS landing page

Static marketing site for agentOS: the governance layer for AI at work.
Plain HTML, CSS and a few lines of JavaScript. No build step, no dependencies.

## Structure

```
index.html      Page markup
css/styles.css  All styles (design tokens at the top under :root)
js/main.js      Mobile menu and sticky-header behaviour
favicon.svg     Browser tab icon
.nojekyll       Tells GitHub Pages to serve files as-is
```

## Run locally

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
```

Then visit http://localhost:8000.

## Deploy with GitHub Pages

1. Create a new repository on GitHub and push this folder to it:

   ```bash
   git remote add origin https://github.com/<you>/<repo>.git
   git push -u origin main
   ```

2. In the repository, go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to *Deploy from a branch*, choose `main` and `/ (root)`, then save.
4. The site will be live at `https://<you>.github.io/<repo>/` within a minute or two.

## Before going live

- The final **Book a pilot** button links to `mailto:hello@example.com`. Replace it in `index.html` (search for `TODO`) with your real email or booking link.
- The footer still says "Working draft for design review", as in the Figma file.
