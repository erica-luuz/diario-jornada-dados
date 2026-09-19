---
date: 2026-09-18
slug: primeiros-passos-com-pandas
authors:
  - erica
categories:
  - Python
tags:
  - python
  - pandas
readtime: 8
description: Anotações sobre manipulação, limpeza e análise de dados.
---

# Primeiros passos com Pandas

Anotações sobre manipulação, limpeza e análise de dados.

<!-- more -->

## Por que Pandas

É a biblioteca padrão em Python para trabalhar com dados em formato de tabela — os `DataFrame`. Grande parte do trabalho de um analista de dados começa aqui.

## O básico que uso o tempo todo

```python
import pandas as pd

df = pd.read_csv("dados.csv")
df.head()
df.info()
df.describe()
```

## Limpeza de dados

Antes de qualquer análise, vale checar valores nulos e duplicados:

```python
df.isnull().sum()
df.drop_duplicates(inplace=True)
```

Pequenos passos, mas que evitam conclusões erradas mais à frente.
