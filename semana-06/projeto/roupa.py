from produto import Produto


class Roupa(Produto):
    TAMANHOS = ("PP", "P", "M", "G", "GG")
    DESCONTO_MAXIMO = 50

    def __init__(self, codigo, nome, preco, tamanho, desconto=0):
        super().__init__(codigo, nome, preco)
        self.tamanho = tamanho
        self.desconto = desconto

    @property
    def tamanho(self):
        return self._tamanho

    @tamanho.setter
    def tamanho(self, valor):
        valor = str(valor).upper().strip()
        if valor not in self.TAMANHOS:
            raise ValueError(f"tamanho '{valor}' não existe, "
                             f"use {', '.join(self.TAMANHOS)}")
        self._tamanho = valor

    @property
    def desconto(self):
        return self._desconto

    @desconto.setter
    def desconto(self, valor):
        if not 0 <= valor <= self.DESCONTO_MAXIMO:
            raise ValueError(f"desconto de {valor}% não permitido, "
                             f"o máximo é {self.DESCONTO_MAXIMO}%")
        self._desconto = valor

    def calcular_preco_final(self):
        return self.preco * (1 - self.desconto / 100)

    def categoria(self):
        return "Roupa"

    def __str__(self):
        texto = f"{super().__str__()} (tam. {self.tamanho}"
        if self.desconto:
            texto += f", {self.desconto}% off"
        return texto + ")"

    def __repr__(self):
        return (f"Roupa(codigo={self.codigo!r}, nome={self.nome!r}, "
                f"preco={self.preco}, tamanho={self.tamanho!r}, "
                f"desconto={self.desconto})")
