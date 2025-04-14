import streamlit as st
from analysis import nba, mlb, ufc

st.set_page_config(page_title="Cerebellum vX", layout="wide")
st.title("CEREBELLUM vX - Sistema de Predicción Quirúrgico")

option = st.sidebar.selectbox("Selecciona un módulo", ["NBA - Q1/Q4", "MLB - 1I/9I", "UFC - Fights"])

if option == "NBA - Q1/Q4":
    nba.render()
elif option == "MLB - 1I/9I":
    mlb.render()
elif option == "UFC - Fights":
    ufc.render()
