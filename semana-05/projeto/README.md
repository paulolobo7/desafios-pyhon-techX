# Sistema de Análise de Dados - Sprint 5

Projeto da semana 05 de Desenvolvimento em Python. O programa lê um arquivo CSV com dados de clientes (nome, e-mail, CPF, telefone e data de nascimento), valida cada campo usando regex e no final mostra um relatório com quem passou e quem não passou na validação.

## Como rodar

Precisa só do Python 3, não usei nenhuma biblioteca de fora.

```
python main.py clientes.csv
```

Se rodar só `python main.py`, o programa pergunta o nome do arquivo. Apertando enter ele usa o `clientes.csv`.

## Arquivos

- `main.py`: programa principal, chama a leitura, a análise e o relatório
- `leitura.py`: abre o CSV e separa os registros válidos dos inválidos
- `validacoes.py`: funções de validação com regex
- `excecoes.py`: as exceções personalizadas
- `relatorio.py`: monta o relatório final
- `clientes.csv`: arquivo de teste com 10 clientes, alguns com erro de propósito
- `clientes_sem_coluna.csv`: arquivo sem a coluna de telefone, pra testar o KeyError

## Validações

Todas as validações ficam no `validacoes.py` e usam o módulo `re`. Os padrões começam com `^` e terminam com `$` pra obrigar o texto inteiro a seguir o formato, senão um e-mail tipo "abc fulano@gmail.com" passaria porque tem um pedaço válido no meio.

**E-mail:** `^[\w.+-]+@[\w-]+(\.[\w-]+)+$`

Antes do @ aceita letras, números, `_`, ponto, `+` e `-`. Depois do @ precisa ter o domínio e pelo menos um ponto com mais alguma coisa, então `gmail.com` e `ufrn.br` passam, e `com.br` também porque o grupo pode repetir. Coloquei a exigência do ponto porque um e-mail tipo `bruno.lima@hotmail` não existe na prática. Espaço não entra em nenhuma parte.

**CPF:** `^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$`

São 3 blocos de 3 dígitos e mais 2 no final. Os pontos e o traço têm `?` porque muita gente digita o CPF só com números, então aceito os dois jeitos (`123.456.789-10` e `12345678900`). Não fiz o cálculo dos dígitos verificadores porque a atividade pede validação de formato.

**Telefone:** `^\(?\d{2}\)?\s?9?\d{4}-?\d{4}$`

DDD com 2 dígitos, com ou sem parênteses, depois um espaço opcional (`\s?`), o 9 opcional pra aceitar celular e fixo, e o número com ou sem traço. Sem DDD não passa.

**Data:** `^\d{2}/\d{2}/\d{4}$`

O regex só confere se está no formato dd/mm/aaaa. Ele não sabe se a data existe, por exemplo 29/02/2003 passa no regex mas 2003 não foi bissexto. Por isso depois do regex eu converto com `datetime.strptime`, que dá `ValueError` quando a data não existe. Com a data convertida calculo a idade da pessoa.

## Exceções tratadas

**FileNotFoundError:** se o arquivo não existe, o programa mostra uma mensagem e para, sem aquele erro gigante do Python. Fica no `ler_arquivo`, que usa `try/except/else/finally`: o `try` abre e lê o arquivo, o `except` trata o arquivo inexistente, o `else` só roda se a leitura deu certo e o `finally` fecha o arquivo sempre que ele chegou a ser aberto.

**ValueError:** aparece quando a data tem o formato certo mas não existe (dia 31/02, 29/02 em ano que não é bissexto). O registro vai pra lista de inválidos com o motivo "data inexistente".

**KeyError:** o `csv.DictReader` transforma cada linha em dicionário usando o cabeçalho. Se faltar uma coluna no CSV, acessar `registro["telefone"]` dá KeyError. Nesse caso não adianta continuar porque todas as linhas vão dar o mesmo erro, então o programa avisa qual coluna está faltando e para.

**FormatoInvalidoError (personalizada):** criei pra quando algum campo não bate com o regex. Ela guarda o nome do campo e o valor errado, assim o relatório mostra exatamente o que estava errado em cada linha.

**IdadeInvalidaError (personalizada):** é uma regra de negócio, a data pode estar certa e mesmo assim não fazer sentido. Coloquei o limite de 0 a 120 anos, então uma data no futuro (idade negativa) ou alguém nascido em 1890 cai aqui.

As duas herdam de `Exception`.

## Exemplo de entrada

Trecho do `clientes.csv`:

```
nome,email,cpf,telefone,data_nascimento
Ana Souza,ana.souza@gmail.com,123.456.789-10,(11) 98765-4321,15/03/1998
Bruno Lima,bruno.lima@hotmail,987.654.321-00,(21) 99876-5432,02/07/2001
Carla Mendes,carla_mendes@outlook.com,111.222.333-44,(31) 3456-7890,29/02/2003
Diego Alves,diego@empresa.com.br,12345678900,11987654321,10/10/1985
```

## Exemplo de saída

Rodando `python main.py clientes.csv` (as idades mudam conforme a data em que roda):

```
Arquivo 'clientes.csv' lido com 10 registro(s).

============================================================
               RELATÓRIO DE ANÁLISE DE DADOS                
============================================================

Registros válidos (3):
  Ana Souza          ana.souza@gmail.com           28 anos
  Diego Alves        diego@empresa.com.br          40 anos
  João Pedro         joao.pedro@ufrn.br            22 anos

Registros inválidos (7):
  Linha  3 | Bruno Lima       | E-mail em formato inválido: 'bruno.lima@hotmail'
  Linha  4 | Carla Mendes     | data inexistente: '29/02/2003'
  Linha  6 | Eduarda Rocha    | CPF em formato inválido: '222.333.444-5'
  Linha  7 | Felipe Costa     | E-mail em formato inválido: 'felipe costa@gmail.com'
  Linha  8 | Gabriela Nunes   | idade fora do permitido: 136 anos
  Linha  9 | Henrique Dias    | Telefone em formato inválido: '1234-5678'
  Linha 10 | Isabela Martins  | idade fora do permitido: -4 anos

Estatísticas:
  Total de registros lidos: 10
  Passaram na validação:    3
  Reprovados:               7
  Taxa de aprovação:        30.0%
  Média de idade (válidos): 30.0 anos
============================================================
```

Com um arquivo que não existe:

```
Erro: o arquivo 'nao_existe.csv' não foi encontrado.
```

Com o arquivo sem a coluna de telefone:

```
Arquivo 'clientes_sem_coluna.csv' lido com 1 registro(s).
Erro no arquivo: coluna 'telefone' não existe no arquivo
```
