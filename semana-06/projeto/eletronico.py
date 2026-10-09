from produto import Produto


class Eletronico(Produto):
    IMPOSTO = 0.15
    TAXA_GARANTIA = 0.10

    def __init__(self, codigo, nome, preco, garantia_estendida=False):
        super().__init__(codigo, nome, preco)
        self.garantia_estendida = garantia_estendida

    def calcular_preco_final(self):
        total = self.preco * (1 + self.IMPOSTO)
        if self.garantia_estendida:
            total += self.preco * self.TAXA_GARANTIA
        return total

    def categoria(self):
        return "Eletrônico"

    def __str__(self):
        garantia = "com" if self.garantia_estendida else "sem"
        return f"{super().__str__()} ({garantia} garantia estendida)"

    def __repr__(self):
        return (f"Eletronico(codigo={self.codigo!r}, nome={self.nome!r}, "
                f"preco={self.preco}, "
                f"garantia_estendida={self.garantia_estendida})")
