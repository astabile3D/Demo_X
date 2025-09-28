# Food 3D – Piattaforma gratuita (GitHub Pages + Actions)

- Dashboard unica in `admin/` con configurazione (repo/branch/token) salvata in **localStorage**
- Cattura da telefono (camera) o galleria (foto/video)
- Upload diretto nel repo via GitHub API
- Ricostruzione automatica (CPU) su **GitHub Actions** con OpenDroneMap (ODM)
- Stato avanzamento per elemento (`items/<id>/status.json`), preview 3D e QR
- Gestione elementi: copia link, elimina upload grezzi, elimina elemento

## Setup
1. Abilita **GitHub Pages** (main / root).
2. Carica tutto il contenuto del pacchetto nel tuo repo.
3. Apri `https://OWNER.github.io/REPO/admin/` → clicca **⚙️ Impostazioni** e inserisci:
   - `Repo Owner` (es. `astabile3D`)
   - `Repo Name`  (es. `Demo_X`)
   - `Branch`     (es. `main`)
   - `Token`      (Fine-grained token: Contents Read&Write su questo repo)
   > Le impostazioni rimangono salvate nel tuo browser (localStorage).

## Upload (struttura prevista dal workflow)
```
uploads/<id>/videos/clip_01.mp4   (altri clip opzionali)
uploads/<id>/*.jpg                (o uploads/<id>/images/*.jpg)
```

## Output
```
items/<id>/model.glb
items/<id>/index.html
items/<id>/status.json
```
