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

## Como colocar imagens em um post

Salve o arquivo em `docs/assets/images/` e referencie no post assim (o caminho abaixo vale para posts em `docs/blog/posts/`):

```markdown
![Descrição da imagem](../../assets/images/nome-do-arquivo.png)
```

## Como publicar no GitHub Pages

```bash
mkdocs gh-deploy
```
