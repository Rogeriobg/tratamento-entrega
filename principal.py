import pandas as pd
import numpy as np
from tabulate import tabulate  # <-- Importação adicionada

df_original = pd.read_csv('dados.csv', sep=';', engine='python')

print("Informações gerais:")
print(df_original.info())
print("\nPrimeiras 5 linhas:")
print(df_original.head())
print("\nÚltimas 5 linhas:")
print(df_original.tail())

df = df_original.copy()

df['Calories'] = df['Calories'].replace(r'^\s*$', np.nan, regex=True)
df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')
df['Calories'] = df['Calories'].fillna(0)

print("\nApós substituir valores nulos em 'Calories' por 0:")
print(df)

df['Date'] = df['Date'].replace(r'^\s*$', np.nan, regex=True)
df['Date'] = df['Date'].str.replace('"', '', regex=False)
df['Date'] = df['Date'].str.replace("'", '', regex=False)
df['Date'] = df['Date'].replace('20201226', '2020/12/26')
df['Date'] = df['Date'].fillna('1900/01/01')

print("\nApós limpeza e preenchimento provisório da coluna 'Date':")
print(df)

df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d', errors='coerce')
df['Date'] = df['Date'].replace(pd.Timestamp('1900-01-01'), pd.NaT)

print("\nApós conversão da coluna 'Date' para datetime:")
print(df)

df = df.dropna()

print("\nDataFrame final, com todos os valores nulos removidos:")
print(df)


print("\nDataFrame final formatado com tabulate:")
print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))

print("\nInformações finais do DataFrame:")
print(df.info())
