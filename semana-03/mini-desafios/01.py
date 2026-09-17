def celsius_para_fahrenheit(celsius: float) -> float:
  """Converte uma temperatura de Celsius para Fahrenheit."""
  return (celsius * 9 / 5) + 32


if __name__ == "__main__":
  try:
    entrada = float(input("Digite a temperatura em °C: "))
    resultado = celsius_para_fahrenheit(entrada)
    print(f"{entrada:.1f}°C equivalem a {resultado:.1f}°F")
  except ValueError:
    print("Erro: Digite um valor numérico válido.")