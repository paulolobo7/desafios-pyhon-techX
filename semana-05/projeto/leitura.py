import csv

from excecoes import FormatoInvalidoError, IdadeInvalidaError
from validacoes import validar_registro


def ler_arquivo(caminho):
    arquivo = None
    try:
        arquivo = open(caminho, encoding="utf-8")
        registros = list(csv.DictReader(arquivo))
    except FileNotFoundError:
        print(f"Erro: o arquivo '{caminho}' não foi encontrado.")
        return None
    else:
        print(f"Arquivo '{caminho}' lido com {len(registros)} registro(s).")
        return registros
    finally:
        if arquivo is not None:
            arquivo.close()


def analisar_registros(registros):
    validos = []
    invalidos = []
    for linha, registro in enumerate(registros, start=2):
        try:
            idade = validar_registro(registro)
        except KeyError as erro:
            raise KeyError(f"coluna {erro} não existe no arquivo") from erro
        except (FormatoInvalidoError, IdadeInvalidaError) as erro:
            invalidos.append((linha, registro["nome"], str(erro)))
        except ValueError:
            motivo = f"data inexistente: '{registro['data_nascimento']}'"
            invalidos.append((linha, registro["nome"], motivo))
        else:
            registro["idade"] = idade
            validos.append(registro)
    return validos, invalidos
