from desafio1_cadastro import cadastrar_produtos, exibir_lista
from desafio2_filtro import filtrar_por_preco
from desafio3_ordenacao import ordenar_produtos
from desafio4_categorias import categorias_unicas
from desafio5_estatisticas import calcular_estatisticas


def exibir_relatorio(produtos, filtro, ordenados, categorias, estatisticas):
    limite, opcao, filtrados = filtro
    crescente, decrescente = ordenados
    menor, maior, media = estatisticas

    print(f"\n{'=' * 50}")
    print(f"{'RELATÓRIO FINAL':^50}")
    print(f"{'=' * 50}")
    print(f"Total de produtos cadastrados: {len(produtos)}")

    exibir_lista("Produtos cadastrados:", produtos)
    exibir_lista(f"Produtos {opcao} de R$ {limite:.2f}:", filtrados)
    exibir_lista("Ordem crescente de preço:", crescente)
    exibir_lista("Ordem decrescente de preço:", decrescente)

    lista_categorias = ", ".join(sorted(categorias))
    print(f"\nCategorias únicas ({len(categorias)}): {lista_categorias}")

    print("\nEstatísticas de preço:")
    print(f"  Menor preço: R$ {menor:.2f}")
    print(f"  Maior preço: R$ {maior:.2f}")
    print(f"  Média:       R$ {media:.2f}")
    print(f"{'=' * 50}")


def main():
    produtos = cadastrar_produtos()
    filtro = filtrar_por_preco(produtos)
    ordenados = ordenar_produtos(produtos)
    categorias = categorias_unicas(produtos)
    estatisticas = calcular_estatisticas(produtos)
    exibir_relatorio(produtos, filtro, ordenados, categorias, estatisticas)


if __name__ == "__main__":
    main()
