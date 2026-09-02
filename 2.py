segundos_totais = int(input("Digite a quantidade de segundos: "))

horas = segundos_totais // 3600
minutos = (segundos_totais % 3600) // 60
segundos = segundos_totais % 60

print(f"{horas} horas, {minutos} minutos e {segundos} segundos")