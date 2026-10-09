from cliente import Cliente
from produto import Produto


class Carrinho:
    def __init__(self, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("o carrinho precisa de um Cliente")
        self.cliente = cliente
        self._itens = []

    def adicionar(self, produto):
        if not isinstance(produto, Produto):
            raise TypeError(f"só dá pra adicionar produtos, "
                            f"não {type(produto).__name__}")
        self._itens.append(produto)

    def remover(self, produto):
        if produto not in self._itens:
            raise ValueError(f"{produto.nome} não está no carrinho")
        self._itens.remove(produto)

    @property
    def itens(self):
        return list(self._itens)

    def total(self):
        return sum(p.calcular_preco_final() for p in self._itens)

    def __len__(self):
        return len(self._itens)

    def __str__(self):
        linhas = [f"Carrinho de {self.cliente.nome} ({len(self)} itens)"]
        for produto in self._itens:
            linhas.append(f"  {produto}")
        linhas.append(f"  Total: R$ {self.total():.2f}")
        return "\n".join(linhas)

    def __repr__(self):
        return f"Carrinho(cliente={self.cliente!r}, itens={len(self)})"
