{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww13440\viewh11100\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
\
# Titel und Info\
st.set_page_config(page_title="NEM-Check Profi", page_icon="\uc0\u55357 \u56620 ")\
st.title("\uc0\u55357 \u56620  NEM-Check: Inhaltsstoff-Analyse")\
st.write("Bewertung nach Dr. H\'fcther & Norbert Hartwig")\
\
# Datenbank der Kriterien (Keywords)\
PLUS = \{\
    "Fl\'fcssigform": ["fl\'fcssig", "saft", "konzentrat", "trinken"],\
    "Natur-Basis": ["gem\'fcse", "obst", "beeren", "lebensmittel", "extrakt"],\
    "Komplexit\'e4t": ["spektrum", "breitband", "vollst\'e4ndig", "komplex"],\
    "Fermentation": ["fermentiert", "milchsauer", "milchs\'e4ure"],\
    "Vitalstoffe": ["q10", "carnitin", "omega", "lecithin", "enzyme"]\
\}\
\
MINUS = \{\
    "Kapselform": ["kapsel", "tablette", "pressling", "pille"],\
    "Zusatzstoffe": ["aroma", "s\'fc\'dfstoff", "sucralose", "aspartam", "fruktose"],\
    "Isolation": ["isoliert", "synthetisch", "chemisch"]\
\}\
\
# Eingabefeld\
name = st.text_input("Name des Produkts:", "Mein Testprodukt")\
text = st.text_area("Hier Zutatenliste oder Beschreibung reinkopieren:", height=150)\
\
if st.button("Jetzt analysieren"):\
    if text:\
        text_lower = text.lower()\
        score = 0\
        gefundene_plus = []\
        gefundene_minus = []\
\
        # Analyse-Logik\
        for kat, keywords in PLUS.items():\
            if any(kw in text_lower for kw in keywords):\
                score += 1\
                gefundene_plus.append(kat)\
\
        for kat, keywords in MINUS.items():\
            if any(kw in text_lower for kw in keywords):\
                score -= 1\
                gefundene_minus.append(kat)\
\
        # Anzeige\
        st.divider()\
        st.subheader(f"Ergebnis f\'fcr \{name\}")\
        st.metric("Gesamt-Score", f"\{score:+\} Punkte")\
\
        c1, c2 = st.columns(2)\
        with c1:\
            st.write("**Pluspunkte:**")\
            for p in gefundene_plus: st.write(f"\uc0\u9989  \{p\}")\
        with c2:\
            st.write("**Abz\'fcge:**")\
            for m in gefundene_minus: st.write(f"\uc0\u10060  \{m\}")\
    else:\
        st.error("Bitte kopiere erst einen Text in das Feld!")}