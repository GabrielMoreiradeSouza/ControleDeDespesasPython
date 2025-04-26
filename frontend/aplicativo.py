
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="Controle de Despesas Pessoais", layout="wide")
st.title("Controle de Despesas Pessoais")

st.header("Adicionar Transação")
with st.form("formulario_transacao"):
    tipo = st.selectbox("Tipo", ["crédito", "débito"])
    valor = st.number_input("Valor", min_value=0.01, step=0.01)
    categoria = st.selectbox("Categoria", ["Alimentação", "Moradia", "Transporte", "Lazer", "Outros"])
    data = st.date_input("Data", value=datetime.now())
    enviar = st.form_submit_button("Adicionar")
    if enviar:
        response = requests.post("http://localhost:5000/transacoes", json={
            "tipo": tipo,
            "valor": valor,
            "categoria": categoria,
            "data": str(data)
        })
        if response.status_code == 201:
            st.success("Transação adicionada com sucesso!")
        else:
            st.error("Erro ao adicionar transação.")

st.header("Transações")
response = requests.get("http://localhost:5000/transacoes")
if response.status_code == 200:
    transacoes = response.json()
    df = pd.DataFrame(transacoes)
    st.dataframe(df)

st.header("Evolução Mensal")
response = requests.get("http://localhost:5000/mensal")
if response.status_code == 200:
    dados_mensais = response.json()
    df_mensal = pd.DataFrame(dados_mensais)
    if not df_mensal.empty:
        fig = px.line(df_mensal, x="mes", y="total", color="tipo", title="Evolução de Créditos e Débitos por Mês", labels={"mes": "Mês", "total": "Valor (R$)"})
        st.plotly_chart(fig)

st.header("Distribuição por Categoria")
response = requests.get("http://localhost:5000/categorias")
if response.status_code == 200:
    dados_categorias = response.json()
    df_categorias = pd.DataFrame(dados_categorias)
    if not df_categorias.empty:
        fig = px.pie(df_categorias, values="total", names="categoria", title="Distribuição de Despesas por Categoria")
        st.plotly_chart(fig)
