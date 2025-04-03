import streamlit as st
from fpdf import FPDF
import tempfile
import os

st.set_page_config(page_title="Calcolo Costi RENTRI", layout="wide")

# Menu laterale
st.sidebar.title("🔍 Navigazione")
scelta = st.sidebar.radio("Vai a:", ["🏠 Home", "📋 Verifica Obblighi", "💶 Calcolo Costi", "📘 FIR & Registro"])

if scelta == "🏠 Home":
    st.switch_page("rentri_check_app.py")
elif scelta == "📋 Verifica Obblighi":
    st.switch_page("verifica_obblighi.py")
elif scelta == "📘 FIR & Registro":
    st.switch_page("fir_registro.py")

st.title("Calcolo Costi di Iscrizione al RENTRI")

# Input dell'utente
n_dipendenti = st.slider("Numero complessivo di dipendenti dell’impresa:", 0, 200, 5)
n_unita_locali = st.number_input("Numero di Unità Locali da iscrivere:", min_value=1, value=1)

# Determina la fascia di contribuzione
if n_dipendenti > 50:
    fascia = "> 50 dipendenti"
    diritto = 10
    contributo_primo = 100
    contributo_successivi = 60
elif n_dipendenti > 10:
    fascia = "11-50 dipendenti"
    diritto = 10
    contributo_primo = 50
    contributo_successivi = 30
else:
    fascia = "≤ 10 dipendenti"
    diritto = 10
    contributo_primo = 15
    contributo_successivi = 10

# Calcolo costi totali
totale_iscrizione = n_unita_locali * (diritto + contributo_primo)
totale_annuo_successivi = n_unita_locali * contributo_successivi

# Output dei risultati
st.markdown(f"""
### Risultato
**Classe:** {fascia}  
**Diritti di segreteria:** €{diritto} x {n_unita_locali} UL = €{diritto * n_unita_locali}  
**Contributo 1° anno:** €{contributo_primo} x {n_unita_locali} UL = €{contributo_primo * n_unita_locali}  

📌 **Totale Iscrizione Iniziale:** €{totale_iscrizione}  
🔁 **Totale annuo successivo:** €{totale_annuo_successivi}
""")

# Generazione PDF
if st.button("📄 Scarica Scheda PDF Costi"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="RENTRI – Calcolo Costi Iscrizione", ln=True, align='C')
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=f"""
Classe di iscrizione: {fascia}
Numero di UL: {n_unita_locali}
Numero dipendenti: {n_dipendenti}

- Diritti di segreteria: €{diritto * n_unita_locali}
- Contributo 1° anno: €{contributo_primo * n_unita_locali}
- Totale iscrizione iniziale: €{totale_iscrizione}
- Contributo annuale successivo: €{totale_annuo_successivi}
    """)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdf.output(tmp_file.name)
        st.success("Scheda PDF generata con successo!")
        st.download_button(
            label="📥 Scarica PDF",
            data=open(tmp_file.name, "rb").read(),
            file_name="scheda_costi_RENTRI.pdf",
            mime="application/pdf"
        )
        os.unlink(tmp_file.name)
