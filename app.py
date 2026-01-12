{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww13440\viewh11100\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
\
# --- KONFIGURATION ---\
st.set_page_config(page_title="NEM-Check Experte", page_icon="\uc0\u55357 \u56589 ")\
\
# --- EXPERTEN-KRITERIEN (Keywords f\'fcr die Suche) ---\
KRITERIEN = \{\
    "plus": \{\
        "Fl\'fcssigform": ["fl\'fcssig", "saft", "konzentrat", "trinken"],\
        "Vollst\'e4ndigkeit": ["vitamine", "mineralstoffe", "spurenelemente", "komplex"],\
        "Lebensmittel-Basis": ["aus lebensmitteln", "gem\'fcse", "obst", "beeren", "extrakt"],\
        "Sek. Pflanzenstoffe": ["sekund\'e4re pflanzenstoffe", "polyphenole", "flavonoide", "carotinoide"],\
        "Nat\'fcrliche \'d6le": ["omega-3", "lein\'f6l", "fisch\'f6l", "algen\'f6l", "borretsch\'f6l"],\
        "Vitaminoide": ["carnitin", "q10", "coenzym", "l-carnitin"],\
        "Fermentation": ["milchsauer", "vergoren", "fermentiert", "milchs\'e4urebakterien"],\
        "Enzyme": ["enzyme", "schonend hergestellt", "kaltgepresst"],\
        "Heimisch": ["heimisch", "regional", "kr\'e4uter"]\
    \},\
    "minus": \{\
        "Darreichungsform": ["kapsel", "tablette", "pressling", "pille"],\
        "Zusatzstoffe": ["aroma", "s\'fc\'dfstoff", "sucralose", "aspartam", "geschmacksverst\'e4rker", "konservierungsstoff"],\
        "Isolation": ["isoliert", "synthetisch", "chemisch"],\
        "Zucker": ["zuckerzusatz", "glukose", "fruktosesirup"]\
    \}\
\}\
\
st.title("\uc0\u55357 \u56589  Intelligente NEM-Analyse")\
st.write("F\'fcge die Inhaltsstoffe oder eine Beschreibung ein, um das Produkt nach Dr. H\'fcther zu bewerten.")\
\
# --- EINGABEBEREICH ---\
produkt_name = st.text_input("Name des Produkts", placeholder="z.B. SuperVit 500")\
beschreibung = st.text_area("Inhaltsstoffe oder Produktbeschreibung hier einf\'fcgen:", height=200, \
                            placeholder="Kopiere hier die Zutatenliste von der Herstellerseite hinein...")\
\
if st.button("Analyse starten"):\
    if beschreibung:\
        text_basis = beschreibung.lower()\
        gefundene_plus = []\
        gefundene_minus = []\
\
        # Analyse-Schleife\
        for kat, keywords in KRITERIEN["plus"].items():\
            if any(kw in text_basis for kw in keywords):\
                gefundene_plus.append(kat)\
        \
        for kat, keywords in KRITERIEN["minus"].items():\
            if any(kw in text_basis for kw in keywords):\
                gefundene_minus.append(kat)\
\
        # Score Berechnung\
        score = len(gefundene_plus) - len(gefundene_minus)\
\
        # Ergebnisse anzeigen\
        st.divider()\
        st.subheader(f"Analyse-Ergebnis f\'fcr: \{produkt_name\}")\
        \
        col1, col2 = st.columns(2)\
        col1.metric("Qualit\'e4ts-Score", score)\
        \
        if score >= 5:\
            col2.success("Sehr empfehlenswert \uc0\u9989 ")\
        elif score >= 1:\
            col2.warning("Bedingt empfehlenswert \uc0\u9888 \u65039 ")\
        else:\
            col2.error("Nicht empfohlen \uc0\u10060 ")\
\
        # Detail-Listen\
        c1, c2 = st.columns(2)\
        with c1:\
            st.write("**Positive Merkmale:**")\
            for p in gefundene_plus: st.write(f"\uc0\u55357 \u57314  \{p\}")\
            if not gefundene_plus: st.write("Keine gefunden.")\
        \
        with c2:\
            st.write("**Punktabz\'fcge f\'fcr:**")\
            for m in gefundene_minus: st.write(f"\uc0\u55357 \u56628  \{m\}")\
            if not gefundene_minus: st.write("Keine gefunden.")\
            \
    else:\
        st.warning("Bitte f\'fcge einen Text zur Analyse ein.")}