"# notes" 


this repository contains notes.

live at https://harmeet773.github.io/notes/

## Search setup

- The search index is stored in `search.json`.
- Regenerate it after editing pages with:

```bash
python3 scripts/generate_search_index.py
```

- Serve the site over HTTP for search to work reliably, for example:

```bash
python3 -m http.server 8000
```
