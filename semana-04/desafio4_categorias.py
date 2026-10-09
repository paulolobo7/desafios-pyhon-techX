from desafio1_cadastro import cadastrar_produtos


def categorias_unicas(produtos):
    return {p["categoria"] for p in produtos}


def main():
    produtos = cadastrar_produtos()
    categorias = categorias_unicas(produtos)
    lista_categorias = ", ".join(sorted(categorias))
    print(f"\nCategorias únicas ({len(categorias)}): {lista_categorias}")


if __name__ == "__main__":
    main()
