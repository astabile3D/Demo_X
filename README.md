# Prodotto 3D – Frontend (KIRI)

Questo repository contiene **solo il frontend** (dashboard + template item).
La ricostruzione 3D viene effettuata **dietro le quinte** dal tuo **proxy KIRI**,
che pubblica i risultati qui dentro usando le GitHub API (scrivendo `items/<id>/status.json`,
`items/<id>/index.html`, `items/<id>/model.glb`).

## Flusso
1. L’utente usa la **Dashboard** (`index.html`) per caricare foto/video.
2. La Dashboard invia i file al **tuo proxy** (`/jobs`), *non* al browser.
3. Il proxy chiama le **API di KIRI**, monitora lo stato e quando termina **scrive** in questo repo:
   - `items/<id>/status.json` (stato e progresso)
   - `items/<id>/index.html` (pagina pubblica dell’item)
   - `items/<id>/model.glb` (+ eventuali varianti)
4. La pagina pubblica dell’item mostra la barra di avanzamento e poi il modello 3D.

> Nota: questo repo **non** contiene GitHub Actions. Non servono con KIRI,
> perché lo stato e i file finali vengono scritti dal proxy.

## Struttura
- `index.html` → **Dashboard amministrativa** (cattura/upload, lista items, anteprima).
- `items_template/index.html` → **Template di dettaglio item** (status + viewer). Il proxy lo copia in `items/<id>/index.html`.
- `data/index.json` → indice pubblico degli items (la Dashboard lo aggiorna via GitHub API dal browser).

## Configurazione Dashboard
Apri la Dashboard (`index.html`) e imposta in **⚙️ Impostazioni**:
- **Repo Owner**: il tuo utente/organizzazione GitHub (es. `astabile3D`)
- **Repo Name**: il nome di questo repo (es. `Demo_X`)
- **Branch**: tipicamente `main`
- **Token**: un **Personal Access Token** con permesso `repo`

## Configurazione Proxy KIRI
Il tuo proxy deve esporre:
```
POST /jobs
Body: {
  id: string,
  title?: string,
  images: [{ name: string, dataBase64: string }]
}
-> 200 { ok: true } oppure { ok: true, blocked: true }
```
Il proxy:
- crea job su KIRI,
- carica immagini,
- avvia,
- polla/attende il completamento,
- scarica il `model.glb`,
- pubblica in questo repo i file: `items/<id>/index.html`, `items/<id>/status.json`, `items/<id>/model.glb`,
- aggiorna `data/index.json` (stato `ready`).

Trovi uno **scheletro** del proxy nelle nostre conversazioni precedenti (Node.js/Express).

## Pubblicazione su GitHub Pages
- Imposta GitHub Pages su **root** del branch (Settings → Pages → Build and deployment).
- La pagina admin sarà disponibile a: `https://<owner>.github.io/<repo>/`
- La pagina pubblica di un item: `https://<owner>.github.io/<repo>/items/<id>/`

## Suggerimenti
- Soglie: `<20` foto → `blocked`; `20–39` → warning, il proxy può comunque procedere; `≥40` → ok.
- Per performance lato proxy, puoi comprimere immagini a **2048px max lato** prima di inviarle a KIRI.
