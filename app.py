import streamlit as st

# Titel und Info
st.set_page_config(page_title="NEM-Check Profi", page_icon="🔬")
st.title("🔬 NEM-Check: Inhaltsstoff-Analyse")
st.write("Bewertung nach Dr. Hüther & Norbert Hartwig")

# Datenbank der Kriterien (Keywords)
PLUS = {
    "Flüssigform": ["flüssig", "saft", "konzentrat", "trinken"],
    "Natur-Basis": ["gemüse", "obst", "beeren", "lebensmittel", "extrakt"],
    "Komplexität": ["spektrum", "breitband", "vollständig", "komplex"],
    "Fermentation": ["fermentiert", "milchsauer", "milchsäure"],
    "Vitalstoffe": ["q10", "carnitin", "omega", "lecithin", "enzyme"]
}

MINUS = {
    "Kapselform": ["kapsel", "tablette", "pressling", "pille"],
    "Zusatzstoffe": ["aroma", "süßstoff", "sucralose", "aspartam", "fruktose"],
    "Isolation": ["isoliert", "synthetisch", "chemisch"]
}

# Eingabefeld
name = st.text_input("Name des Produkts:", "Mein Testprodukt")
text = st.text_area("Hier Zutatenliste oder Beschreibung reinkopieren:", height=150)

if st.button("Jetzt analysieren"):
    if text:
        text_lower = text.lower()
        score = 0
        gefundene_plus = []
        gefundene_minus = []

        # Analyse-Logik
        for kat, keywords in PLUS.items():
            if any(kw in text_lower for kw in keywords):
                score += 1
                gefundene_plus.append(kat)

        for kat, keywords in MINUS.items():
            if any(kw in text_lower for kw in keywords):
                score -= 1
                gefundene_minus.append(kat)

        # Anzeige
        st.divider()
        st.subheader(f"Ergebnis für {name}")
        st.metric("Gesamt-Score", f"{score:+} Punkte")

        c1, c2 = st.columns(2)
        with c1:
            st.write("**Pluspunkte:**")
            for p in gefundene_plus: st.write(f"✅ {p}")
        with c2:
            st.write("**Abzüge:**")
            for m in gefundene_minus: st.write(f"❌ {m}")
    else:
        st.error("Bitte kopiere erst einen Text in das Feld!")