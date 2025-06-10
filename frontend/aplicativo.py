import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
from PIL import Image
import os
import zipfile
import io

st.set_page_config(page_title="Controle de Despesas Pessoais", layout="wide")
st.title("Controle de Despesas Pessoais")

# --- Adicionar Transação ---
st.header("Adicionar Transação")
tipo = st.selectbox("Tipo", ["crédito", "débito", "dinheiro", "pix"])
valor = st.number_input("Valor", min_value=0.01, step=0.01)
categoria = st.selectbox("Categoria", ["Alimentação", "Moradia", "Transporte", "Lazer", "Outros"])
if categoria == "Outros":
    categoria_personalizada = st.text_input("Especifique a Categoria")
else:
    categoria_personalizada = categoria
data = st.date_input("Data", value=datetime.now())

# Botão para adicionar a transação
if st.button("Adicionar"):
    response = requests.post("http://localhost:5000/transacoes", json={
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria_personalizada,
        "data": str(data)
    })
    if response.status_code == 201:
        st.success("Transação adicionada com sucesso!")
    else:
        st.error("Erro ao adicionar transação.")

# --- Upload de Imagem de Comprovante ---
st.header("Upload de Imagem de comprovante (Opcional)")
uploaded_file = st.file_uploader("Escolha uma imagem do comprovante...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Comprovante", use_column_width=True)

    # Nome do arquivo baseado na data, categoria e valor
    nome_arquivo = f"{data}_{categoria_personalizada}_{valor:.2f}".replace(" ", "_")
    extensao = os.path.splitext(uploaded_file.name)[-1]
    nome_final = nome_arquivo + extensao

    save_path = os.path.join("comprovantes", nome_final)
    os.makedirs("comprovantes", exist_ok=True)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Imagem salva com sucesso em: {save_path}")

# --- Exibição das Transações ---
st.header("Transações")
response = requests.get("http://localhost:5000/transacoes")
if response.status_code == 200:
    transacoes = response.json()
    df = pd.DataFrame(transacoes)
    st.dataframe(df)

# --- Evolução Mensal ---
st.header("Evolução Mensal")
response = requests.get("http://localhost:5000/mensal")
if response.status_code == 200:
    dados_mensais = response.json()
    df_mensal = pd.DataFrame(dados_mensais)
    if not df_mensal.empty:
        fig = px.line(df_mensal, x="mes", y="total", color="tipo",
                      title="Evolução de Créditos e Débitos por Mês",
                      labels={"mes": "Mês", "total": "Valor (R$)"})
        st.plotly_chart(fig)

# --- Distribuição por Categoria ---
st.header("Distribuição por Categoria")
response = requests.get("http://localhost:5000/categorias")
if response.status_code == 200:
    dados_categorias = response.json()
    df_categorias = pd.DataFrame(dados_categorias)
    if not df_categorias.empty:
        fig = px.pie(df_categorias, values="total", names="categoria",
                     title="Distribuição de Despesas por Categoria")
        st.plotly_chart(fig)

# --- Download de Comprovantes por Mês ---
st.header("📁 Baixar Comprovantes por Mês")

if not df.empty:
    df["data"] = pd.to_datetime(df["data"])
    meses_disponiveis = df["data"].dt.to_period("M").drop_duplicates().astype(str)
    mes_escolhido = st.selectbox("Selecione o mês", meses_disponiveis)

    if st.button("📥 Baixar ZIP"):
        transacoes_mes = df[df["data"].dt.to_period("M").astype(str) == mes_escolhido]
        comprovantes_path = "comprovantes"
        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, "w") as zipf:
            for _, row in transacoes_mes.iterrows():
                data_dt = row["data"]
                dia = f"{data_dt.day:02d}"
                nome_base = f"{data_dt.date()}_{row['categoria']}_{row['valor']:.2f}".replace(" ", "_")

                for arquivo in os.listdir(comprovantes_path):
                    if arquivo.startswith(nome_base):
                        caminho_completo = os.path.join(comprovantes_path, arquivo)
                        if os.path.isfile(caminho_completo):
                            zip_path = os.path.join(dia, arquivo)
                            zipf.write(caminho_completo, arcname=zip_path)

        zip_buffer.seek(0)

        if zipf.namelist():
            st.download_button(
                label=f"📦 Baixar comprovantes de {mes_escolhido}",
                data=zip_buffer,
                file_name=f"comprovantes_{mes_escolhido}.zip",
                mime="application/zip"
            )
        else:
            st.warning("Nenhum comprovante encontrado para este mês.")
