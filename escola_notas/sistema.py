import streamlit as st 
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Escolar", layout="wide")
st.title("Dashboard de Desempenho Escolar")

# upload de arquivo
arquivo = st.file_uploader("Envie o arquivo CSV com notas", type=["csv"])

if arquivo:
    try:
        df = pd.read_csv(arquivo)
        df["Data_Prova"] = pd.to_datetime(df["Data_Prova"])
        df["Mês"] = df["Data_Prova"].dt.to_period("M").astype(str)                

        # KPI - Indicador Chave de Desempenho
        media_geral = df["Nota"].mean()
        disciplina_top = df.groupby("Disciplina")["Nota"].mean().idxmax()          
        aluno_pior = df.groupby("Aluno")["Nota"].mean().idxmax()

        # Coluna
        col1, col2, col3 = st.columns(3)
        col1.metric("Media Geral", f"{media_geral:.2f}")
        col2.metric("Melhor Disciplina", disciplina_top)
        col3.metric("Aluno com menor média", aluno_pior)

        # Filtro
        aluno_sel = st.selectbox("Filtrar por Alunos:", df["Aluno"].unique())
        df_filtrado = df[df["Aluno"] == aluno_sel]

        # Titulo do gráfico
        # Gráfico de notas por disciplina do Aluno
        st.subheader(f"Notas de {aluno_sel} por disciplina")
        # Configurando gráfico de Barras
        fig_bar = px.bar(df_filtrado, x="Disciplina", y="Nota", color="Disciplina", text_auto=True)
        st.plotly_chart(fig_bar, use_container_width=True) # Exibindo Gráfico

        # Grafico de linha - evolução das notas do aluno
        st.subheader("Evolução de Notas por mês")
        fig_linha = px.line(df, x="Mês", y="Nota", color="Aluno", markers=True, title="Notas ao longo do tempo")
        st.plotly_chart(fig_linha, use_container_width=True)

    except Exception as e:
       st.error(f"Erro ao processar o arquivo: {e}")      
else:
    st.info("Envie um arquivo CSV com a colunas: Aluno, Disciplina, Data_Prova, Nota")

## python -m streamlit run escola_notas/sistema.py    