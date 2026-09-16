# Diário da Jornada de Dados

Blog/diário de estudos em dados, construído com [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Como rodar localmente

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

Depois abra http://127.0.0.1:8000 no navegador.

## Como criar um novo post

Adicione um arquivo em `docs/blog/posts/AAAA-MM-DD-titulo.md`, seguindo o modelo do post existente (cabeçalho com `date`, `authors`, `categories`, `tags`).

## Como publicar no GitHub Pages

```bash
mkdocs gh-deploy
```
