


def somar(a: float, b: float) -> float:
  """Retorna a soma de dois números."""
  return a + b


def subtrair(a: float, b: float) -> float:
  """Retorna a diferença entre dois números."""
  return a - b


def multiplicar(a: float, b: float) -> float:
  """Retorna o produto de dois números."""
  return a * b


def dividir(a: float, b: float):
  """Retorna a divisão entre dois números ou None com aviso em caso de divisão por zero."""
  if b == 0:
    print("Erro: Divisão por zero não é permitida.")
    return None
  return a / b


if __name__ == "__main__":
  # Testes locais isolados do módulo
  print("Testando somar:", somar(10, 5))
  print("Testando subtrair:", subtrair(10, 5))
  print("Testando multiplicar:", multiplicar(10, 5))
  print("Testando dividir:", dividir(10, 2))
  print("Testando divisão por zero:", dividir(10, 0))