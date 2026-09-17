print("=== CALCULADORA ===")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = int(input("Escolha o número da operação (1 a 4): "))

if 1 <= opcao <= 4:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

match opcao:
    case 1:
        resultado = numero1 + numero2
        print(f"Resultado da soma: {resultado:.2f}")
    case 2:
        resultado = numero1 - numero2
        print(f"Resultado da subtração: {resultado:.2f}")
    case 3:
        resultado = numero1 * numero2
        print(f"Resultado da multiplicação: {resultado:.2f}")
    case 4:
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"Resultado da divisão: {resultado:.2f}")
        else:
            print("Erro: Não é possível dividir por zero!")
    case _:
        print("Opção inválida! Por favor, escolha um número de 1 a 4.")