import streamlit as st
import pandas as pd

# --- KONFIGURATION ---
st.set_page_config(page_title="NEM-Check Experte", page_icon="🌿", layout="wide")

# Styling für die App
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- DATENBASIS NACH DR. HÜTHER & HARTWIG ---
PLUS_KRITERIEN = {
    "Vollständigkeit": "Alle Vitamine, Mineralien und Spurenelemente[cite: 6].",
    "Lebensmittel-Basis": "Vielfalt an natürlichen Lebensmitteln statt Isolate.",
    "Sekundäre Pflanzenstoffe": "Große Bandbreite an sek. Pflanzenstoffen[cite: 8, 20].",
    "Natürliche Öle": "Wertvolle natürliche Öle (z.B. Omega-3)[cite: 9, 20].",
    "Vitaminoide": "Enthält Carnitin und Coenzym Q10[cite: 10].",
    "Fermentation/Enzyme": "Milchsauer vergoren oder mit Enzymen[cite: 11, 20].",
    "Flüssigform": "Flüssig zur besseren Aufnahme ('Botschaft & Energie').",
    "Kräuterextrakte": "Kaltgepresste Kräuterextrakte enthalten[cite: 12].",
    "Reinheit": "Frei von Aromen, Süßstoffen und Chemie."
}

MINUS_KRITERIEN = {
    "Kapsel/Tablette": "Darreichung als feste Form (Abzug laut Hartwig).",
    "Zusatzstoffe": "Aromen, Süßungsmittel oder Geschmacksverstärker.",
    "Isolation": "Synthetische oder isolierte Vitalstoffe.",
    "Wundermittel": "Basiert auf nur einem Lebensmittel (z.B. Noni).",
    "Glykämischer Index": "Hoher glykämischer Index (Zuckerlast)."
}

# --- LOGIK ---
st.title("🌿 NEM-Check: Analyse-Tool")
st.write("Bewertungstool basierend auf den Standards für optimale Nahrungsergänzung[cite: 5, 15].")

with st.sidebar:
    st.header("1. Produkteingabe")
    name = st.text_input("Produktname", "Unbekanntes Produkt")
    monatspreis = st.number_input("Preis pro Monat (€)", min_value=1.0, value=30.0)
    
    st.header("2. Merkmale wählen")
    st.subheader("Positive Eigenschaften")
    pos_auswahl = [k for k in PLUS_KRITERIEN.keys() if st.checkbox(k)]
    
    st.subheader("Negative Eigenschaften")
    neg_auswahl = [k for k in MINUS_KRITERIEN.keys() if st.checkbox(k)]

# --- BERECHNUNG ---
score = len(pos_auswahl) - len(neg_auswahl)
preis_pro_tag = monatspreis / 30
effizienz = score / preis_pro_tag if preis_pro_tag > 0 else 0

# --- AUSGABE ---
st.header(f"Analyse: {name}")

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Qualitäts-Score", score)
with c2:
    st.metric("Preis pro Tag", f"{preis_pro_tag:.2f} €")
with c3:
    st.metric("Effizienz-Index", f"{effizienz:.1f}")

st.divider()

col_left, col_right = st.columns(2)
with col_left:
    st.subheader("✅ Stärken")
    for p in pos_auswahl:
        st.success(f"**{p}**: {PLUS_KRITERIEN[p]}")

with col_right:
    st.subheader("❌ Schwachstellen")
    for n in neg_auswahl:
        st.error(f"**{n}**: {MINUS_KRITERIEN[n]}")

# --- FAZIT ---
st.subheader("Experten-Fazit")
if score >= 7 and preis_pro_tag <= 1.50:
    st.balloons()
    st.info(f"Dieses Produkt entspricht fast ideal den Kriterien von Dr. Hüther (Optimal: Flüssig, Natur, Günstig)[cite: 6, 13, 20].")
elif score < 0:
    st.warning("Vorsicht: Die negativen Merkmale (Isolate, Kapseln, Chemie) überwiegen.")
else:
    st.write("Das Produkt liegt im Mittelfeld. Prüfen Sie, ob eine flüssige Alternative wirtschaftlicher wäre.")