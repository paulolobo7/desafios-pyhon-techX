from abc import ABC, abstractmethod


class Produto(ABC):
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("o nome do produto não pode ficar vazio")
        self._nome = valor.strip()

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("o preço tem que ser um número")
        if valor < 0:
            raise ValueError(f"preço negativo não é permitido ({valor})")
        self._preco = float(valor)

    @abstractmethod
    def calcular_preco_final(self):
        pass

    @abstractmethod
    def categoria(self):
        pass

    def __str__(self):
        return (f"[{self.categoria()}] {self.nome} - "
                f"R$ {self.calcular_preco_final():.2f}")

    def __repr__(self):
        return (f"{type(self).__name__}(codigo={self.codigo!r}, "
                f"nome={self.nome!r}, preco={self.preco})")

    def __eq__(self, outro):
        if not isinstance(outro, Produto):
            return NotImplemented
        return self.codigo == outro.codigo

    def __lt__(self, outro):
        if not isinstance(outro, Produto):
            return NotImplemented
        return self.calcular_preco_final() < outro.calcular_preco_final()

    def __hash__(self):
        return hash(self.codigo)
