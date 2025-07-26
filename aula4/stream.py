# Biblioteca para criação de Dashboards
import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt 


# Carregar dados 
df = pd.read_csv("aula4/vendas_loja.csv")


df["Receita"] = df["Quantidade"] * df["Preço_Unitario"]
df["Data"] = pd.to_datetime(df["Data"])
df["Mês"] = df["Data"].dt.to_period("M")

st.title("Dashboard de Vendas")

# Infos principais
# f "R$ {}"
st.metric("Total de Vendas", f"R$ {df['Receita'].sum():,.2f}")
st.metric("Média por Venda", f"R${df['Receita'].mean():,.2f}")

# Filtro por categoria
categoria = df["Categoria"].unique() # Categoria é unicas
categoria_selecionada = st.selectbox("Selecione a categoria:", categoria)
# Categoria === CategoriaSelecionado
df_filtrado = df[df['Categoria'] == categoria_selecionada]

# Grafico por produto
st.subheader("Receita por Produto")
# Criar uma figura 
fig1, ax1 = plt.subplots()
df_filtrado.groupby("Produto")["Receita"].sum().plot(kind="bar", ax=ax1)
st.pyplot(fig1)

# Grafico por mes
st.subheader("Receita Mensal")
fig2, ax2 = plt.subplots()
df.groupby("Mês")["Receita"].sum().plot(ax=ax2)
st.pyplot(fig2)