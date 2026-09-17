def exibir_ficha_aluno(**dados) -> None:
  """Imprime os campos recebidos em formato de ficha."""
  print("\n====== FICHA CADASTRAL ======")
  for campo, valor in dados.items():
    titulo = campo.replace("_", " ").title()
    print(f"{titulo}: {valor}")
  print("=============================")


if __name__ == "__main__":
  perfil = {}
  print("Preenchimento do cadastro do aluno:")
  perfil["nome"] = input("Nome completo: ").strip()
  perfil["curso"] = input("Curso: ").strip()
  perfil["matricula"] = input("Matrícula: ").strip()

  # Coleta campos customizados adicionais
  while True:
    tem_mais = input("Deseja adicionar mais um campo? (s/n): ").strip().lower()
    if tem_mais != "s":
      break
    chave = input("Nome do campo (ex: turno, email): ").strip().replace(" ", "_")
    valor = input(f"Valor para {chave}: ").strip()
    perfil[chave] = valor

  # Desempacota o dicionário dinâmico em **dados
  exibir_ficha_aluno(**perfil)