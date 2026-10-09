def gerar_relatorio(validos, invalidos):
    total = len(validos) + len(invalidos)
    percentual = len(validos) / total * 100 if total else 0

    print()
    print("=" * 60)
    print(f"{'RELATÓRIO DE ANÁLISE DE DADOS':^60}")
    print("=" * 60)

    print(f"\nRegistros válidos ({len(validos)}):")
    for r in validos:
        print(f"  {r['nome']:<18} {r['email']:<28} {r['idade']:>3} anos")

    print(f"\nRegistros inválidos ({len(invalidos)}):")
    for linha, nome, motivo in invalidos:
        print(f"  Linha {linha:>2} | {nome:<16} | {motivo}")

    print("\nEstatísticas:")
    print(f"  Total de registros lidos: {total}")
    print(f"  Passaram na validação:    {len(validos)}")
    print(f"  Reprovados:               {len(invalidos)}")
    print(f"  Taxa de aprovação:        {percentual:.1f}%")

    if validos:
        idades = [r["idade"] for r in validos]
        media = sum(idades) / len(idades)
        print(f"  Média de idade (válidos): {media:.1f} anos")
    print("=" * 60)
