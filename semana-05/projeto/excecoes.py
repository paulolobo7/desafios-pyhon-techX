class FormatoInvalidoError(Exception):
    def __init__(self, campo, valor):
        self.campo = campo
        self.valor = valor
        super().__init__(f"{campo} em formato inválido: '{valor}'")


class IdadeInvalidaError(Exception):
    def __init__(self, idade):
        self.idade = idade
        super().__init__(f"idade fora do permitido: {idade} anos")
