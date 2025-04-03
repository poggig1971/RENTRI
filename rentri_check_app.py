import streamlit as st
from PIL import Image

st.set_page_config(page_title="RENTRI Check - ANCE Piemonte", layout="wide")

# Menu laterale
st.sidebar.title("🔍 Navigazione")
scelta = st.sidebar.radio("Vai a:", ["🏠 Home", "📋 Verifica Obblighi", "💶 Calcolo Costi", "📘 FIR & Registro"])

if scelta == "📋 Verifica Obblighi":
    st.switch_page("verifica_obblighi.py")
elif scelta == "💶 Calcolo Costi":
    st.switch_page("calcolo_costi.py")
elif scelta == "📘 FIR & Registro":
    st.switch_page("fir_registro.py")

# Logo
logo = Image.open("image.png")
st.image(logo, width=300)

st.title("RENTRI Check")
st.subheader("Guida interattiva per le imprese edili")

st.markdown("""
Questa Web App è uno strumento operativo sviluppato da **ANCE Piemonte Valle d’Aosta** per aiutare le imprese a comprendere se sono tenute ad iscriversi al **RENTRI - Registro Elettronico Nazionale per la Tracciabilità dei Rifiuti**.

Puoi:
- Verificare rapidamente **se sei obbligato** a iscriverti
- Scoprire **in quale scaglione** rientri
- Calcolare i **costi di iscrizione**
- Generare una **scheda PDF personalizzata**
""")
