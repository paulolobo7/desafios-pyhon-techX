def ler_preco(mensagem):
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(texto)
            if valor >= 0:
                return valor
            print("O preço não pode ser negativo.")
        except ValueError:
            print("Digite um número válido.")


def ler_quantidade():
    while True:
        texto = input("Quantos produtos deseja cadastrar? ").strip()
        if texto.isdigit() and int(texto) > 0:
            return int(texto)
        print("Digite um número inteiro maior que zero.")


def cadastrar_produtos():
    produtos = []
    quantidade = ler_quantidade()
    for i in range(quantidade):
        print(f"\nProduto {i + 1}")
        nome = input("Nome: ").strip()
        preco = ler_preco("Preço: R$ ")
        categoria = input("Categoria: ").strip().lower()
        produtos.append({"nome": nome, "preco": preco, "categoria": categoria})
    return produtos


def exibir_lista(titulo, produtos):
    print(f"\n{titulo}")
    if not produtos:
        print("  Nenhum produto encontrado.")
        return
    for p in produtos:
        print(f"  {p['nome']:<20} R$ {p['preco']:>10.2f}   {p['categoria']}")


def main():
    produtos = cadastrar_produtos()
    exibir_lista("Produtos cadastrados:", produtos)


if __name__ == "__main__":
    main()
