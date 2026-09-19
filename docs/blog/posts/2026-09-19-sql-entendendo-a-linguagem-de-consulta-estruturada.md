---
date: 2026-09-19
slug: sql-entendendo-a-linguagem-de-consulta-estruturada
authors:
  - erica
categories:
  - SQL
tags:
  - sql
  - fundamentos
description: "O que é SQL, por que ele surgiu e os elementos e chaves que formam a base da linguagem."
---

# SQL: entendendo a linguagem de consulta estruturada

Hoje comecei a estudar SQL e quis registrar aqui alguns dos conceitos que estou aprendendo.

<!-- more -->

## O que é SQL?

SQL (*Structured Query Language*, ou Linguagem de Consulta Estruturada) é uma linguagem universal, utilizada em sistemas de banco de dados. Ela foi criada pela IBM por volta de 1970.

## Por que o SQL surgiu

Antigamente, os relatórios eram feitos em papel, e as empresas tinham salas lotadas de armários de documentos. Com a popularização dos computadores e dos bancos de dados para armazenar essas informações, surgiu a necessidade de uma linguagem capaz de lidar com um grande volume de dados. Assim nasceu o SQL.

Hoje ele é utilizado para:

- criar tabelas;
- atualizar dados;
- consultar informações de várias tabelas;
- excluir dados, entre outras tarefas.

## Elementos do SQL

Dentro do SQL, temos alguns elementos:

| Elemento | O que é | Exemplos |
|---|---|---|
| Comandos | As ações que executamos | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |
| Cláusulas | As partes que compõem os comandos | `FROM`, `WHERE`, `GROUP BY` |
| Expressões | Operações e cálculos | `A + B`, `A * B` |
| Predicados | Condições a serem avaliadas | `A > B`, `C BETWEEN 50 AND 100` |
| Queries | Consultas que formamos usando as cláusulas anteriores, para obter o resultado esperado | `SELECT coluna FROM tabela` |

Por exemplo:

```sql
SELECT nome
FROM clientes;
```

Nesse caso:

- **SELECT** indica quais informações queremos obter.
- **FROM** indica de qual tabela essas informações serão buscadas.

Então podemos interpretar a consulta como:

> "Selecione a coluna `nome` da tabela `clientes`."

## Chaves: como as tabelas se relacionam

Dentro do SQL existem estruturas muito importantes: a **chave primária** (*Primary Key*) e a **chave estrangeira** (*Foreign Key*). Elas garantem a integridade dos relacionamentos entre as tabelas.

Cada tabela precisa de um identificador único. Em uma tabela de clientes, por exemplo, cada cliente é identificado por uma chave única, que não se repete. Exemplos bastante usados são o ID do cliente e o CPF.

A chave estrangeira, por sua vez, é o campo que aponta para a chave primária de outra tabela, criando a ligação entre elas.
