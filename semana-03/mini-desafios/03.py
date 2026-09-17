def calcular_caixa(*precos: float):
  """Calcula total, maior preço e média de uma tupla de valores."""
  if not precos:
    return 0.0, 0.0, 0.0
  total = sum(precos)
  maior = max(precos)
  media = total / len(precos)
  return total, maior, media


if __name__ == "__main__":
  lista_valores = []
  print("Informe os preços dos itens (digite 'fim' para encerrar):")

  while True:
    dado = input("Preço do item: ").strip()
    if dado.lower() == "fim":
      break
    try:
      preco = float(dado.replace(",", "."))
      if preco >= 0:
        lista_valores.append(preco)
      else:
        print("Digite um preço positivo.")
    except ValueError:
      print("Valor inválido.")

  if lista_valores:
    # O operador * desempacota a lista dinâmica na tupla *args da função
    total, maior, media = calcular_caixa(*lista_valores)
    print(f"\n--- Fechamento do Caixa ---")
    print(f"Total: R$ {total:.2f}")
    print(f"Item mais caro: R$ {maior:.2f}")
    print(f"Média por item: R$ {media:.2f}")
  else:
    print("Nenhum item foi registrado.")