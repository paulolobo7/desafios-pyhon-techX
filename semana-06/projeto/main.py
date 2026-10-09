from produto import Produto
from alimento import Alimento
from eletronico import Eletronico
from roupa import Roupa
from cliente import Cliente
from carrinho import Carrinho


def titulo(texto):
    print(f"\n{'=' * 60}\n{texto}\n{'=' * 60}")


def criar_produtos():
    return [
        Alimento("A01", "Arroz", 6.50, 5),
        Alimento("A02", "Queijo minas", 42.90, 0.450),
        Alimento("A03", "Banana", 5.99, 1.2),
        Eletronico("E01", "Fone bluetooth", 129.90),
        Eletronico("E02", "Notebook", 3200.00, garantia_estendida=True),
        Eletronico("E03", "Mouse sem fio", 59.90),
        Roupa("R01", "Camiseta básica", 49.90, "M"),
        Roupa("R02", "Calça jeans", 159.90, "g", desconto=20),
        Roupa("R03", "Moletom", 189.00, "GG", desconto=50),
    ]


def demonstrar_polimorfismo(produtos):
    titulo("Polimorfismo: mesma chamada, cálculos diferentes")
    for p in produtos:
        print(f"{p.nome:<16} {p.categoria():<11} "
              f"base R$ {p.preco:>8.2f}  ->  "
              f"final R$ {p.calcular_preco_final():>8.2f}")


def demonstrar_dunders(produtos):
    titulo("Métodos especiais")
    print("__str__ :", produtos[7])
    print("__repr__:", repr(produtos[7]))

    outro_arroz = Alimento("A01", "Arroz", 7.00, 1)
    print(f"__eq__  : Arroz 5kg == Arroz 1kg (mesmo código)? "
          f"{produtos[0] == outro_arroz}")
    print(f"__eq__  : Arroz == Banana? {produtos[0] == produtos[2]}")
    print(f"__lt__  : Mouse < Notebook? {produtos[5] < produtos[4]}")

    print("\nOrdenado pelo preço final (usa o __lt__):")
    for p in sorted(produtos):
        print(f"  {p}")


def demonstrar_carrinho(produtos):
    titulo("Carrinho (composição)")
    ana = Cliente("Ana Souza", "Ana.Souza@Gmail.com")
    bruno = Cliente("Bruno Lima", "bruno@ufrn.br")
    print(f"Clientes: {ana} | {bruno}")
    print(f"Mesmo cliente? {ana == Cliente('Ana S.', 'ana.souza@gmail.com')}")

    carrinho_ana = Carrinho(ana)
    for p in (produtos[0], produtos[3], produtos[7]):
        carrinho_ana.adicionar(p)
    print(f"\n{carrinho_ana}")

    carrinho_bruno = Carrinho(bruno)
    carrinho_bruno.adicionar(produtos[4])
    carrinho_bruno.adicionar(produtos[8])
    print(f"\n{carrinho_bruno}")
    print(f"\nrepr: {carrinho_bruno!r}")
    return carrinho_ana


def demonstrar_erros(carrinho):
    titulo("Tratamento de entradas inválidas")
    testes = [
        ("Produto abstrato", lambda: Produto("X", "Genérico", 10)),
        ("Preço negativo", lambda: Eletronico("E9", "TV", -500)),
        ("Preço em texto", lambda: Roupa("R9", "Boné", "trinta", "M")),
        ("Nome vazio", lambda: Alimento("A9", "   ", 10, 1)),
        ("Peso zero", lambda: Alimento("A9", "Feijão", 8.99, 0)),
        ("Tamanho errado", lambda: Roupa("R9", "Bermuda", 79.9, "XG")),
        ("Desconto de 80%", lambda: Roupa("R9", "Jaqueta", 300, "M", 80)),
        ("E-mail inválido", lambda: Cliente("Carla", "carla@hotmail")),
        ("Item que não é produto", lambda: carrinho.adicionar("pizza")),
    ]
    for descricao, teste in testes:
        try:
            teste()
        except (ValueError, TypeError) as erro:
            print(f"{descricao:<24} -> {type(erro).__name__}: {erro}")
        else:
            print(f"{descricao:<24} -> passou (não deveria)")

    titulo("Setter impedindo estado inválido")
    calca = carrinho.itens[2]
    print(f"Antes: {calca}")
    try:
        calca.preco = -10
    except ValueError as erro:
        print(f"Tentei colocar preço -10: {erro}")
    calca.desconto = 10
    print(f"Depois de mudar o desconto pra 10%: {calca}")


def main():
    produtos = criar_produtos()
    demonstrar_polimorfismo(produtos)
    demonstrar_dunders(produtos)
    carrinho = demonstrar_carrinho(produtos)
    demonstrar_erros(carrinho)


if __name__ == "__main__":
    main()
