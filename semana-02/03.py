soma = 0.0
maior_numero = float('-inf')
menor_numero = float('inf')
quantidade_numeros = 5

for i in range(1, quantidade_numeros + 1):
    numero_atual = float(input(f"Digite o {i}º número: "))

    # Soma
    soma += numero_atual

    # Verifica o maior
    if numero_atual > maior_numero:
        maior_numero = numero_atual

    # Verifica o menor
    if numero_atual < menor_numero:
        menor_numero = numero_atual

media = soma / quantidade_numeros

print("\n--- Resultados ---")
print(f"Soma total: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")