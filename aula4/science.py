import pandas as pd
import matplotlib.pyplot as plt 

# ler o csv
df = pd.read_csv("aula4/vendas_loja.csv", comment='#')

# nomes das colunas 
# criar coluna chamada receita
df["Receita"] = df["Quantidade"] * df["Preço_Unitario"]

# sum -> somar
total_receita = df["Receita"].sum()

print("Total de vendas R$", total_receita) # Total de receita faturado

# mean -> media
media_receita = df["Receita"].mean()
print("Média da Receita R$", media_receita)

# Produto mais vendido em quantidade 
produto_mais_vendido = df.groupby("Produto")["Quantidade"].sum().idxmax()
# idxmax -> pegar o maior valor
print("Produto mais vendido:", produto_mais_vendido)

# Categoria com maior receita
categoria_top_receita = df.groupby("Categoria")["Receita"].sum().idxmax()
print("Categoria com maior receita:", categoria_top_receita)

# Grafico de barras - Receita por categoria
# Plot - > gerar gráfico
df.groupby("Categoria")["Receita"].sum().plot(kind="bar", title="Receita por Categoria")
plt.ylabel("Receita (R$)")
plt.ticklabel_format() # finalizar o layout
plt.show() # exibir o gráfico

# Gráfico de Linha - Receita por Mês 

df["Data"] = pd.to_datetime(df["Data"])
df["Mes"] = df["Data"].dt.to_period("M") # Capturando o M -> Mês da data
# Group by
df.groupby("Mes")["Receita"].sum().plot(kind="line", title="Receita Mensal")
plt.ylabel("Receita R$")
plt.xlabel("Mês")
plt.tight_layout()
plt.show()