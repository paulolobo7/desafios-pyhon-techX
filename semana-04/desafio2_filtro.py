from desafio1_cadastro import cadastrar_produtos, exibir_lista, ler_preco


def filtrar_por_preco(produtos):
    limite = ler_preco("\nValor de referência para o filtro: R$ ")
    opcao = ""
    while opcao not in ("acima", "abaixo"):
        resposta = input("Mostrar produtos acima ou abaixo desse valor? ")
        opcao = resposta.strip().lower()
    if opcao == "acima":
        filtrados = [p for p in produtos if p["preco"] > limite]
    else:
        filtrados = [p for p in produtos if p["preco"] < limite]
    return limite, opcao, filtrados


def main():
    produtos = cadastrar_produtos()
    limite, opcao, filtrados = filtrar_por_preco(produtos)
    exibir_lista(f"Produtos {opcao} de R$ {limite:.2f}:", filtrados)


if __name__ == "__main__":
    main()
