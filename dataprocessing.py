import pandas as pd

# Ler os dados
df = pd.read_csv("vendas.csv")

# Converter datas
df["Data_Venda"] = pd.to_datetime(df["Data_Venda"])

# Criar coluna de faturamento
df["Faturamento"] = df["Quantidade"] * df["Preço_Unitário"]

# Remover possíveis duplicatas
df = df.drop_duplicates()

# Verificar valores ausentes
print(df.isnull().sum())

# Salvar base limpa
df.to_csv("vendas_tratadas.csv", index=False)
print("Base tratada salva como vendas_tratadas.csv")
