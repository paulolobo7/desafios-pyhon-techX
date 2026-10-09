import re


class Cliente:
    PADRAO_EMAIL = r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$"

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise ValueError("nome do cliente muito curto")
        self._nome = valor.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        valor = str(valor).strip().lower()
        if not re.match(self.PADRAO_EMAIL, valor):
            raise ValueError(f"e-mail inválido: '{valor}'")
        self._email = valor

    def __str__(self):
        return f"{self.nome} <{self.email}>"

    def __repr__(self):
        return f"Cliente(nome={self.nome!r}, email={self.email!r})"

    def __eq__(self, outro):
        if not isinstance(outro, Cliente):
            return NotImplemented
        return self.email == outro.email

    def __hash__(self):
        return hash(self.email)
