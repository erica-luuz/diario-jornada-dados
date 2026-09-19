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

## Atalhos (clique duplo na pasta do projeto)

- `novo-post.bat` — pergunta título, categoria e tags, e cria o arquivo do post já com data de hoje.
- `visualizar.bat` — abre o site no navegador para conferir antes de publicar.
- `publicar.bat` — confere o site, salva no GitHub e atualiza o site ao vivo.

## Como criar um novo post (manualmente)

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
