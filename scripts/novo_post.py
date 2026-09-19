import os
import re
import shutil
import subprocess
import sys
import unicodedata
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = Path(__file__).resolve().parent.parent
PASTA_POSTS = RAIZ / "docs" / "blog" / "posts"
CATEGORIAS = [
    "Python",
    "SQL",
    "Power BI",
    "Estatística",
    "Engenharia de Dados",
    "Projetos",
    "Visualização de Dados",
    "Carreira e Aprendizado",
]


def criar_slug(texto):
    ascii_puro = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_puro.lower()).strip("-")


def escolher_categoria():
    print("\nEscolha a categoria:")
    for numero, nome in enumerate(CATEGORIAS, 1):
        print(f"  {numero}. {nome}")
    print(f"  {len(CATEGORIAS) + 1}. Outra (você digita o nome)")
    while True:
        resposta = input("Número da categoria: ").strip()
        if resposta.isdigit() and 1 <= int(resposta) <= len(CATEGORIAS):
            return CATEGORIAS[int(resposta) - 1]
        if resposta == str(len(CATEGORIAS) + 1):
            nome = input("Nome da nova categoria: ").strip()
            if nome:
                return nome
        print("Opção inválida, tente de novo.")


def abrir_no_editor(arquivo):
    codigo = shutil.which("code")
    if codigo:
        subprocess.Popen(f'"{codigo}" "{arquivo}"', shell=True)
    else:
        os.startfile(arquivo)


def main():
    print("=== Novo post ===\n")
    titulo = input("Título do post: ").strip()
    if not titulo:
        print("Título vazio, nada foi criado.")
        return

    categoria = escolher_categoria()
    tags = [t.strip() for t in input("\nTags separadas por vírgula (Enter para pular): ").split(",") if t.strip()]
    descricao = input("Frase curta que aparece no cartão da página inicial (Enter para pular): ").strip()

    hoje = date.today().isoformat()
    slug = criar_slug(titulo)
    arquivo = PASTA_POSTS / f"{hoje}-{slug}.md"
    if arquivo.exists():
        print(f"\nJá existe um post com esse nome: {arquivo.name}")
        return

    cabecalho = [f"date: {hoje}", f"slug: {slug}", "authors:", "  - erica", "categories:", f"  - {categoria}"]
    if tags:
        cabecalho.append("tags:")
        cabecalho.extend(f"  - {tag}" for tag in tags)
    if descricao:
        cabecalho.append('description: "' + descricao.replace('"', "'") + '"')

    corpo = (
        f"# {titulo}\n\n"
        "Escreva aqui a introdução do post (este trecho aparece na lista do blog).\n\n"
        "<!-- more -->\n\n"
        "## Título da primeira seção\n\n"
        "Escreva aqui o conteúdo.\n"
    )

    arquivo.write_text("---\n" + "\n".join(cabecalho) + "\n---\n\n" + corpo, encoding="utf-8", newline="\n")
    print(f"\nPost criado: {arquivo.relative_to(RAIZ)}")

    if "--sem-abrir" not in sys.argv:
        abrir_no_editor(arquivo)
        print("O arquivo foi aberto para você escrever. Quando terminar, salve (Ctrl+S) e use o atalho 'publicar'.")


if __name__ == "__main__":
    main()
