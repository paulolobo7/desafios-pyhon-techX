import math

# class Cliente:
#
#     def __init__(self, nome, email, cpf):
#         self.nome = nome
#         self.email = email
#         self.cpf = cpf
#
#     def exibir(self):
#
#         print(f"Nome: {self.nome}, Email: {self.email}, CPF: {self.cpf}")
#
# ana = Cliente("Ana Silva", "ana@email.com", "123 456 789 10")
# bruno = Cliente("Bruno Silva", "bruno@email.com", "123 456 789 10")
#
# ana.exibir()
# print("---")
# bruno.exibir()



# class Produto:
#
#     taxa_imposto = 0.20
#
#     def __init__(self, nome, preco):
#         self.nome = nome
#         self.preco = preco
#
#     def exibir(self):
#         print(f"Nome do produto: {self.nome}, Preço: {self.preco}")
#
#     def preco_com_imposto(self):
#         return round(self.preco * (1 + Produto.taxa_imposto), 2)
#
# p1 = Produto("Mouse", "100")
# p2 = Produto("Teclado", "205.99")
#
# p1.exibir()
# p2.exibir()
# print(Produto.taxa_imposto)


class Calculadora:
    def __init__(self, valor):
        self.valor = valor

    def dobrar(self):
        return self.valor * 2

    @classmethod
    def criar_com_zero(cls):
        return cls(0)

    @staticmethod
    def somar(a, b):
        return a + b

c = Calculadora(10)
print(c.dobrar())
print(Calculadora.criar_com_zero().valor)
print(Calculadora.somar(5, 3))


class Circulo:
    def __init__(self, raio):
        self.raio = raio


    @property
    def area(self):
        return math.pi * self.raio ** 2


c1 = Circulo(5)
print(f"{c1.area:.2f}")