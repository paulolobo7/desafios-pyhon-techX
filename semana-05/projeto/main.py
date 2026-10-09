import sys

from leitura import ler_arquivo, analisar_registros
from relatorio import gerar_relatorio


def main():
    if len(sys.argv) > 1:
        caminho = sys.argv[1]
    else:
        caminho = input("Nome do arquivo (enter para clientes.csv): ").strip()
        if not caminho:
            caminho = "clientes.csv"

    registros = ler_arquivo(caminho)
    if registros is None:
        return

    try:
        validos, invalidos = analisar_registros(registros)
    except KeyError as erro:
        print(f"Erro no arquivo: {erro.args[0]}")
        return

    gerar_relatorio(validos, invalidos)


if __name__ == "__main__":
    main()
