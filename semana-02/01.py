idade = int(input("Digite a sua idade: "))
renda = float(input("Digite a sua renda mensal: R$ "))

if renda < 2000.0:
    classificacao = "Bronze"
elif renda < 5000.0:
    classificacao = "Prata"
elif renda < 10000.0:
    classificacao = "Ouro"
else:
    classificacao = "Diamante"

print(f"Cliente de {idade} anos. Classificação baseada na renda: {classificacao}")