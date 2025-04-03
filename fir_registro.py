import streamlit as st

st.set_page_config(page_title="FIR e Registro C/S", layout="centered")
st.title("Formulario di Identificazione dei Rifiuti e Registro Carico/Scarico")

# Menu laterale
st.sidebar.title("🔍 Navigazione")
scelta = st.sidebar.radio("Vai a:", ["🏠 Home", "📋 Verifica Obblighi", "💶 Calcolo Costi", "📘 FIR & Registro"])

if scelta == "🏠 Home":
    st.switch_page("rentri_check_app.py")
elif scelta == "📋 Verifica Obblighi":
    st.switch_page("verifica_obblighi.py")
elif scelta == "💶 Calcolo Costi":
    st.switch_page("calcolo_costi.py")

st.markdown("""
A partire dal 13 febbraio 2025, entrano in vigore i **nuovi modelli** di:

- **Formulario di Identificazione dei Rifiuti (FIR)**
- **Registro cronologico di carico e scarico**

Chi è iscritto al RENTRI dovrà gestire entrambi i documenti **esclusivamente in formato digitale**.

---

### 🧾 FIR – Formulario di Identificazione dei Rifiuti
- Dal **13/02/2025** saranno obbligatori i nuovi modelli FIR vidimati digitalmente.
- Dal **13/02/2026** i soggetti iscritti al RENTRI dovranno utilizzare il **FIR digitale**.
- È possibile accompagnare il trasporto con:
  - Una **stampa cartacea** del FIR digitale
  - Un **dispositivo mobile** per mostrarlo in digitale
- I FIR vecchi non potranno più essere usati dal 13/02/2025.

🔗 [Accedi all'area FIR sul portale RENTRI](https://www.rentri.gov.it/)

---

### 📘 Registro Cronologico di Carico e Scarico
- Obbligatorio per:
  - Produttori di rifiuti pericolosi
  - Produttori di rifiuti non pericolosi art. 184, c.3, lett. c), d), g)
  - Trasportatori professionali
  - Impianti e consorzi
- Il **nuovo formato entra in vigore il 13/02/2025**
- Dopo l’iscrizione al RENTRI, il Registro va tenuto **solo digitalmente**

📥 Scaricabile dall’area "Produttori non iscritti" o "Operatori" sul portale RENTRI.

📌 Conservazione: **3 anni**  
📌 Tempistiche annotazioni: **entro 10 giorni lavorativi** (produttori)  
📌 Trasmissione al RENTRI: **entro fine mese successivo all’ultima annotazione**

---

Per ulteriori dettagli:
- [FAQ ufficiali RENTRI](https://www.rentri.gov.it/supporto)
- [Manuale operativo DM 59/2023](https://www.rentri.gov.it/)
""")
