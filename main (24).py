
import streamlit as st

st.set_page_config(page_title="Painel Snaper", layout="wide")

st.title("Painel Snaper - Robô de Sinais")

with st.sidebar:
    st.header("Configurações")
    st.success("Robô carregado com sucesso!")

st.info("Este painel exibe os sinais automáticos de entrada com base na estratégia sniper.")
st.write("Aguarde o carregamento dos dados e verifique os sinais abaixo:")

st.metric("Sinal Atual", "COMPRA", "+2.3%")
st.metric("Confirmação", "Volume Acima da Média", delta="OK")
