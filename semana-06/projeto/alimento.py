from produto import Produto


class Alimento(Produto):
    def __init__(self, codigo, nome, preco_kg, peso_kg):
        super().__init__(codigo, nome, preco_kg)
        self.peso_kg = peso_kg

    @property
    def peso_kg(self):
        return self._peso_kg

    @peso_kg.setter
    def peso_kg(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError(f"peso inválido ({valor}), "
                             f"precisa ser maior que 0")
        self._peso_kg = float(valor)

    def calcular_preco_final(self):
        return self.preco * self.peso_kg

    def categoria(self):
        return "Alimento"

    def __str__(self):
        return f"{super().__str__()} ({self.peso_kg:.3f} kg)"

    def __repr__(self):
        return (f"Alimento(codigo={self.codigo!r}, nome={self.nome!r}, "
                f"preco_kg={self.preco}, peso_kg={self.peso_kg})")
