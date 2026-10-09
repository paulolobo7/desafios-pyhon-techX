from desafio1_cadastro import cadastrar_produtos


def calcular_estatisticas(produtos):
    precos = [p["preco"] for p in produtos]
    return (min(precos), max(precos), sum(precos) / len(precos))


def main():
    produtos = cadastrar_produtos()
    menor, maior, media = calcular_estatisticas(produtos)
    print("\nEstatísticas de preço:")
    print(f"  Menor preço: R$ {menor:.2f}")
    print(f"  Maior preço: R$ {maior:.2f}")
    print(f"  Média:       R$ {media:.2f}")


if __name__ == "__main__":
    main()
