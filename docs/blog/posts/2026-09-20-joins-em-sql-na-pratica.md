---
date: 2026-09-20
slug: joins-em-sql-na-pratica
authors:
  - erica
categories:
  - SQL
tags:
  - sql
  - joins
readtime: 5
description: Entendendo como combinar tabelas e evitar erros comuns nas consultas.
---

# Joins em SQL na prática

Entendendo como combinar tabelas e evitar erros comuns nas consultas.

<!-- more -->

## O problema que os joins resolvem

Dados raramente vivem em uma única tabela. Separar informações em tabelas relacionadas evita repetição e mantém tudo consistente — mas isso significa que, na hora de consultar, é preciso juntar essas tabelas de volta.

## Os tipos mais comuns

- `INNER JOIN` — retorna só as linhas que têm correspondência nas duas tabelas.
- `LEFT JOIN` — retorna tudo da tabela da esquerda, com `NULL` onde não houver correspondência.
- `RIGHT JOIN` e `FULL JOIN` — menos usados no dia a dia, mas úteis em casos específicos.

## Erro comum: duplicação de linhas

Um `JOIN` mal condicionado pode multiplicar linhas silenciosamente, inflando somas e contagens sem gerar erro nenhum. Sempre vale checar o número de linhas antes e depois do join.
