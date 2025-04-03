import streamlit as st

st.set_page_config(page_title="Verifica Obblighi RENTRI", layout="centered")
st.title("Verifica degli Obblighi RENTRI")

# Menu laterale
st.sidebar.title("🔍 Navigazione")
scelta = st.sidebar.radio("Vai a:", ["🏠 Home", "📋 Verifica Obblighi", "💶 Calcolo Costi", "📘 FIR & Registro"])

if scelta == "🏠 Home":
    st.switch_page("rentri_check_app.py")
elif scelta == "💶 Calcolo Costi":
    st.switch_page("calcolo_costi.py")
elif scelta == "📘 FIR & Registro":
    st.switch_page("fir_registro.py")

st.markdown("""
Compila il modulo seguente per verificare se la tua impresa è tenuta ad iscriversi al RENTRI.
""")

# Domande guidate
tipo_rifiuto = st.selectbox(
    "Che tipo di rifiuti produce la tua impresa?",
    [
        "Solo rifiuti non pericolosi da attività di costruzione/demolizione",
        "Rifiuti pericolosi",
        "Rifiuti non pericolosi da attività industriali/artigianali"
    ]
)

trasporto = st.radio(
    "La tua impresa effettua trasporto di rifiuti a titolo professionale?",
    ["Sì (cat. 1, 4 o 5)", "No", "Solo in conto proprio (cat. 2 bis)"]
)

n_dipendenti = st.slider("Quanti dipendenti ha l’impresa (inclusi part-time, esclusi amministratori senza contratto)?", 0, 200, 5)

categoria_albo = st.multiselect(
    "Sei iscritto all'Albo Gestori Ambientali? Se sì, in quale categoria?",
    ["Categoria 1", "Categoria 2 bis", "Categoria 4", "Categoria 5", "Categoria 9", "Categoria 10"]
)

st.divider()

# Logica di verifica
obbligo = False
scaglione = "Nessuno"
messaggio = "La tua impresa non è tenuta ad iscriversi al RENTRI."

if tipo_rifiuto == "Rifiuti pericolosi":
    obbligo = True
    if n_dipendenti >_
