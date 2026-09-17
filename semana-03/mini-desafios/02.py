def validar_senha(senha: str) -> bool:
  """Retorna True se a senha possuir 8 ou mais caracteres."""
  return len(senha) >= 8


if __name__ == "__main__":
  while True:
    senha_usuario = input("Cadastre uma senha (mínimo 8 caracteres): ")
    if validar_senha(senha_usuario):
      print("✓ Senha cadastrada com sucesso!")
      break
    print("✗ Senha muito curta. Tente novamente.")