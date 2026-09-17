senha_cadastrada = "python123"
tentativas_realizadas = 0
limite_tentativas = 3

while tentativas_realizadas < limite_tentativas:
    senha_digitada = input("Digite a sua senha: ")
    tentativas_realizadas += 1

    if senha_digitada == senha_cadastrada:
        print("Acesso liberado! Bem-vindo ao sistema.")
        break
    else:
        tentativas_restantes = limite_tentativas - tentativas_realizadas
        if tentativas_restantes > 0:
            print(f"Senha incorreta! Você tem mais {tentativas_restantes} tentativa(s).")
else:
    # O else do while só é executado se o loop terminar sem atingir um break
    print("Acesso bloqueado! Você errou a senha 3 vezes.")