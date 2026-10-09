import re
from datetime import datetime, date

from excecoes import FormatoInvalidoError, IdadeInvalidaError

PADRAO_EMAIL = r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$"
PADRAO_CPF = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
PADRAO_TELEFONE = r"^\(?\d{2}\)?\s?9?\d{4}-?\d{4}$"
PADRAO_DATA = r"^\d{2}/\d{2}/\d{4}$"

IDADE_MINIMA = 0
IDADE_MAXIMA = 120


def validar_email(email):
    if not re.match(PADRAO_EMAIL, email):
        raise FormatoInvalidoError("E-mail", email)


def validar_cpf(cpf):
    if not re.match(PADRAO_CPF, cpf):
        raise FormatoInvalidoError("CPF", cpf)


def validar_telefone(telefone):
    if not re.match(PADRAO_TELEFONE, telefone):
        raise FormatoInvalidoError("Telefone", telefone)


def validar_data(data_texto):
    if not re.match(PADRAO_DATA, data_texto):
        raise FormatoInvalidoError("Data", data_texto)
    nascimento = datetime.strptime(data_texto, "%d/%m/%Y").date()
    hoje = date.today()
    idade = hoje.year - nascimento.year
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1
    if idade < IDADE_MINIMA or idade > IDADE_MAXIMA:
        raise IdadeInvalidaError(idade)
    return idade


def validar_registro(registro):
    validar_email(registro["email"].strip())
    validar_cpf(registro["cpf"].strip())
    validar_telefone(registro["telefone"].strip())
    return validar_data(registro["data_nascimento"].strip())
