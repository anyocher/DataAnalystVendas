import pandas as pd
import random
from datetime import datetime, timedelta

# Gerar dados simulados
produtos = ["Mouse Gamer", "Notebook", "Teclado Mecânico", "Headset", "Monitor", "Cadeira Gamer"]
categorias = ["Periféricos", "Informática", "Periféricos", "Periféricos", "Informática", "Móveis"]
regioes = ["Sul", "Sudeste", "Nordeste", "Centro-Oeste", "Norte"]
nomes = ["João", "Maria", "Lucas", "Ana", "Carlos", "Beatriz", "Rafael", "Camila"]

dados = []
for i in range(200):
    data_venda = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 364))
    produto = random.choice(produtos)
    categoria = categorias[produtos.index(produto)]
    quantidade = random.randint(1, 5)
    preco = random.randint(50, 4000)
    regiao = random.choice(regioes)
    cliente = random.choice(nomes)
    idade = random.randint(18, 60)
    sexo = random.choice(["M", "F"])
    dados.append([i+1, data_venda, produto, categoria, quantidade, preco, regiao, cliente, idade, sexo])

# Criar DataFrame
df = pd.DataFrame(dados, columns=[
    "ID_Venda", "Data_Venda", "Produto", "Categoria", "Quantidade", "Preço_Unitário",
    "Região", "Cliente", "Idade", "Sexo"
])


df.to_csv("vendas.csv", index=False)
print("Arquivo vendas.csv criado com sucesso!")
