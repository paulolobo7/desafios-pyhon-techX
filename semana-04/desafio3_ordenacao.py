from desafio1_cadastro import cadastrar_produtos, exibir_lista


def ordenar_produtos(produtos):
    crescente = produtos.copy()
    crescente.sort(key=lambda p: p["preco"])
    decrescente = sorted(produtos, key=lambda p: p["preco"], reverse=True)
    return crescente, decrescente


def main():
    produtos = cadastrar_produtos()
    crescente, decrescente = ordenar_produtos(produtos)
    exibir_lista("Ordem crescente de preço:", crescente)
    exibir_lista("Ordem decrescente de preço:", decrescente)


if __name__ == "__main__":
    main()
