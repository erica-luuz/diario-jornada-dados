---
date: 2026-10-06
slug: sql-comando-where
authors:
  - erica
categories:
  - SQL
tags:
  - sql
  - where
  - mapa-mental
description: "Como filtrar registros com WHERE, IN e LIKE."
---

# SQL — Comando WHERE

Quando queremos utilizar um filtro em uma consulta, utilizamos o comando **WHERE**.

Por exemplo:

```sql
SELECT *
FROM clientes
WHERE cidade = 'SP';
```

Nesse caso, estamos dizendo:

> "Selecione todas as colunas da tabela `clientes` onde a coluna `cidade` seja igual a `SP`."

O resultado será somente os registros dos clientes cuja cidade possui o valor `SP`.

<!-- more -->

## Textos e números

Uma coisa importante é observar o tipo de dado que estamos utilizando no filtro.

Quando estamos filtrando textos, normalmente colocamos o valor entre aspas simples:

```sql
WHERE cidade = 'SP'
```

Já quando estamos trabalhando com números, não precisamos utilizar aspas:

```sql
WHERE idade = 30
```

Isso acontece porque `SP` é um texto, enquanto `30` é um número.

## Filtrando vários valores com IN

E se eu quiser buscar vários valores diferentes na mesma coluna? Podemos utilizar o comando **IN**.

Por exemplo:

```sql
SELECT *
FROM clientes
WHERE idade IN (3, 6, 9);
```

Nesse caso, estou buscando os registros em que a idade seja 3, 6 ou 9.

O `IN` funciona como uma forma mais prática de escrever várias condições de igualdade. Em vez de:

```sql
WHERE idade = 3
   OR idade = 6
   OR idade = 9
```

podemos escrever:

```sql
WHERE idade IN (3, 6, 9);
```

## Utilizando LIKE e os curingas

Outra possibilidade interessante do `WHERE` é utilizar o **LIKE** para procurar textos que seguem determinado padrão.

O símbolo `%` funciona como um coringa, representando qualquer quantidade de caracteres. Por exemplo:

```sql
SELECT *
FROM produtos
WHERE descricao LIKE 'Alto%';
```

Nesse caso, estou procurando descrições que começam com "Alto". Poderíamos encontrar, por exemplo:

- Alto-falante
- Alto rendimento
- Alto padrão

Também podemos colocar o `%` antes da palavra:

```sql
WHERE descricao LIKE '%Alto';
```

Nesse caso, estamos procurando valores que terminam com "Alto".

E podemos colocar o `%` dos dois lados:

```sql
WHERE descricao LIKE '%Alto%';
```

Aqui, estamos procurando valores que contenham "Alto" em qualquer parte do texto.

## O que estou aprendendo com o WHERE

O `WHERE` é um comando muito importante porque permite deixar nossas consultas mais específicas. Com ele, podemos começar com uma tabela cheia de informações e fazer perguntas mais direcionadas aos dados.

Por exemplo:

- Quais clientes são de SP?

  ```sql
  WHERE cidade = 'SP'
  ```

- Quais clientes têm idade 3, 6 ou 9?

  ```sql
  WHERE idade IN (3, 6, 9)
  ```

- Quais produtos possuem "Alto" em sua descrição?

  ```sql
  WHERE descricao LIKE '%Alto%'
  ```

Estou percebendo que, conforme avanço nos estudos de SQL, os comandos começam a se combinar e a consulta passa a ficar cada vez mais poderosa.

> `SELECT` mostra o que quero consultar.
>
> `WHERE` define quais registros quero encontrar.

## Mapa mental

![Mapa mental sobre o comando WHERE](../../assets/images/mapa-mental-where.png)

[:material-download: Baixar o mapa mental](../../assets/images/mapa-mental-where.png){ .md-button download="mapa-mental-where.png" }
