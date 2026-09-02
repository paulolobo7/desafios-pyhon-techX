valor_compra = float(input("Valor da compra: R$ "))
valor_pago = float(input("Valor pago: R$ "))

troco = valor_pago - valor_compra

if troco < 0:
    print("Erro: O valor pago é insuficiente.")
else:
    print(f"Troco: R$ {troco:.2f}")