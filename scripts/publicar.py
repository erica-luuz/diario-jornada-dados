import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = Path(__file__).resolve().parent.parent
PYTHON = sys.executable
SIMULAR = "--simular" in sys.argv


def executar(comando, saida=False):
    if SIMULAR:
        print("[simulação] " + " ".join(comando))
        return ""
    resultado = subprocess.run(comando, cwd=RAIZ, text=True, encoding="utf-8", capture_output=saida, check=True)
    return resultado.stdout if saida else ""


def main():
    print("=== Publicar o diário ===\n")
    alteracoes = subprocess.run(
        ["git", "status", "--short"], cwd=RAIZ, text=True, encoding="utf-8", capture_output=True, check=True
    ).stdout.strip()

    if alteracoes:
        print("Estas são as mudanças que serão publicadas:\n")
        print(alteracoes)
    else:
        print("Não há mudanças novas nos arquivos. Vou apenas atualizar o site ao vivo.")

    if input("\nPublicar agora? (s/n): ").strip().lower() != "s":
        print("Cancelado. Nada foi publicado.")
        return

    print("\n1/3 Conferindo se o site monta sem erros...")
    executar([PYTHON, "-m", "mkdocs", "build", "--quiet"])

    if alteracoes:
        mensagem = input("\nDescreva em uma frase o que mudou (Enter para usar a padrão): ").strip()
        mensagem = mensagem or "Atualiza conteúdo do diário"
        print("\n2/3 Salvando no GitHub...")
        executar(["git", "add", "-A"])
        executar(["git", "commit", "-m", mensagem])
        executar(["git", "push", "origin", "main"])
    else:
        print("\n2/3 Nada novo para salvar no GitHub.")

    print("\n3/3 Atualizando o site ao vivo...")
    executar([PYTHON, "-m", "mkdocs", "gh-deploy"])

    print("\nPronto! Em 1 ou 2 minutos o site estará atualizado:")
    print("https://erica-luuz.github.io/diario-jornada-dados/")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as erro:
        print(f"\nAlgo deu errado ao rodar: {' '.join(map(str, erro.cmd))}")
        print("Nada mais foi executado depois disso. Copie a mensagem acima e me envie para eu ajudar.")
