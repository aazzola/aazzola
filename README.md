# andreaazzola.com — Hugo starter

This is a ready-to-use Hugo skeleton to open in **VS Code**.

## Quick start (VS Code on macOS)

1. **Prerequisiti** (Terminale):
   ```bash
   xcode-select --install || true
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" || true
   brew install hugo git
   ```

2. **Apri questa cartella in VS Code** e apri il *Terminale integrato*.

3. **Inizializza git e aggiungi il tema PaperMod**:
   ```bash
   git init
   git submodule add https://github.com/adityatelange/hugo-PaperMod themes/PaperMod
   git add .
   git commit -m "Initial Hugo site with PaperMod"
   ```

4. **Avvio locale**:
   ```bash
   hugo server -D
   # Apri http://localhost:1313
   ```

5. **Modifica contenuti** in `content/`:
   - Home: `content/_index.md`
   - About: `content/about/_index.md`
   - Contact: `content/contact/_index.md`
   - Books: `content/books/_index.md`
   - Posts: `content/posts/`

6. **Imposta il dominio**:
   - `static/CNAME` contiene `andreaazzola.com`. Lascialo così se usi questo dominio.

7. **Crea repo su GitHub** (nuovo repository, branch `main`) e collega:
   ```bash
   git branch -M main
   git remote add origin git@github.com:<USER>/<REPO>.git
   git push -u origin main
   ```

8. **Pages**: il workflow GitHub Actions incluso costruisce e pubblica su Pages.
   - Vai su *Settings → Pages* e verifica che la *Build and deployment* sia impostata su **GitHub Actions**.
   - Dopo il push su `main`, il sito viene pubblicato su Pages con il dominio personalizzato del file `CNAME`.

## Importare contenuti dal sito attuale

Nel Terminale, in una cartella separata, puoi clonare l’HTML del sito e convertirlo in Markdown con **pandoc**:

```bash
brew install wget pandoc
mkdir -p ~/andrea-site-import && cd ~/andrea-site-import
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://andreaazzola.com/

mkdir -p content-import
find ./andreaazzola.com -name "*.html" -print0 | while IFS= read -r -d '' f; do
  rel="${f#./andreaazzola.com}"
  out="content-import/${rel%.html}.md"
  mkdir -p "$(dirname "$out")"
  pandoc -f html -t gfm --wrap=preserve --extract-media=../andrea-hugo-starter/static "$f" -o "$out"
done
```

Poi sposta i file Markdown in `content/` del progetto Hugo e aggiungi il *front matter* all’inizio di ogni file.

## VS Code helpers

- **.vscode/tasks.json** include comandi rapidi per *serve* e *build*.
- Consigliate estensioni: *Markdown All in One*, *YAML*, *GitLens*, *Hugo Language and Syntax Support*.


## Local template overrides

Overrides track PaperMod commit `d3768854d00ad003b0a8dbdba254ce9224377a01`.
Compare them with upstream before changing the submodule:

- `layouts/baseof.html`: Hugo `Direction` and per-page `contentLanguage`.
- `layouts/rss.xml`: Hugo `Locale`.
- `layouts/_partials/head.html`: reciprocal language alternatives for existing EN/IT URLs.
- `layouts/_partials/templates/opengraph.html`: Hugo `Locale` (per-page locale supported).
- `layouts/_partials/templates/schema_json.html`: per-page content language.
- `layouts/single.html`: historical context and translation navigation before the article body.
- `layouts/list.html`: music moved from Articles/home lists to the archive; historical labels on list entries.
- Existing custom footer plus `extend_footer.html`: analytics preferences and local consent controller.
- `layouts/404.html`: legacy redirect map as an object, with a real fallback page.

## Editorial conventions

`archiveKind: technical` identifies historical technical notes; `archiveKind: music`
identifies earlier music projects. Neither changes the original URL, publication date,
indexability or taxonomy membership. `/archive/` lists the English source articles and
links to available Italian versions. Technical notes also remain in Articles; music
remains accessible through Archive, taxonomies and the existing RSS feeds. There is no
bulk `noindex` policy. Optional `archiveScope` clarifies a particular note's limitations.

Italian articles retain `/it/` URLs using `contentLanguage: it`, `locale: it-IT`,
`translationURL` and `translationLanguage`. Set reciprocal translation fields on the
English article too. This is a compatibility layer, not a Hugo multilingual migration.

## Analytics

Only `params.analyticsMeasurementID` configures analytics. Do not set Hugo's top-level
`googleAnalytics` or `services.googleAnalytics.ID`: those would bypass the consent
controller. The local script loads Google only after acceptance, stores the choice for
180 days, and provides withdrawal through Cookie settings. Withdrawal disables the
property, clears accessible first-party GA cookies and reloads to remove its runtime.
If browser storage is unavailable, consent is not retained across pages. Historical
third-party media embeds are outside the scope of this analytics control.

## Verification for the editorial pass (2026-09-19)

Hugo Extended 0.166.0 production build: 655 pages, 7 paginator pages, 102 static files,
265 aliases. Browser checks cover the consent lifecycle (requests intercepted so no
production telemetry is sent), cookie cleanup, unavailable storage, 32 language pages,
35 archive entries, contact, mobile layout and known/unknown legacy paths.
Professional biography, case studies and opinion changes remain separate editorial work.
