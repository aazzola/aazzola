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

