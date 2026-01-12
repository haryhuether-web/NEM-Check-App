{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww13440\viewh11100\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import pandas as pd\
\
# --- KONFIGURATION ---\
st.set_page_config(page_title="NEM-Check Experte", page_icon="\uc0\u55356 \u57151 ", layout="wide")\
\
# Styling f\'fcr die App\
st.markdown("""\
    <style>\
    .main \{ background-color: #f5f7f9; \}\
    .stMetric \{ background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); \}\
    </style>\
    """, unsafe_allow_html=True)\
\
# --- DATENBASIS NACH DR. H\'dcTHER & HARTWIG ---\
PLUS_KRITERIEN = \{\
    "Vollst\'e4ndigkeit": "Alle Vitamine, Mineralien und Spurenelemente[cite: 6].",\
    "Lebensmittel-Basis": "Vielfalt an nat\'fcrlichen Lebensmitteln statt Isolate.",\
    "Sekund\'e4re Pflanzenstoffe": "Gro\'dfe Bandbreite an sek. Pflanzenstoffen[cite: 8, 20].",\
    "Nat\'fcrliche \'d6le": "Wertvolle nat\'fcrliche \'d6le (z.B. Omega-3)[cite: 9, 20].",\
    "Vitaminoide": "Enth\'e4lt Carnitin und Coenzym Q10[cite: 10].",\
    "Fermentation/Enzyme": "Milchsauer vergoren oder mit Enzymen[cite: 11, 20].",\
    "Fl\'fcssigform": "Fl\'fcssig zur besseren Aufnahme ('Botschaft & Energie').",\
    "Kr\'e4uterextrakte": "Kaltgepresste Kr\'e4uterextrakte enthalten[cite: 12].",\
    "Reinheit": "Frei von Aromen, S\'fc\'dfstoffen und Chemie."\
\}\
\
MINUS_KRITERIEN = \{\
    "Kapsel/Tablette": "Darreichung als feste Form (Abzug laut Hartwig).",\
    "Zusatzstoffe": "Aromen, S\'fc\'dfungsmittel oder Geschmacksverst\'e4rker.",\
    "Isolation": "Synthetische oder isolierte Vitalstoffe.",\
    "Wundermittel": "Basiert auf nur einem Lebensmittel (z.B. Noni).",\
    "Glyk\'e4mischer Index": "Hoher glyk\'e4mischer Index (Zuckerlast)."\
\}\
\
# --- LOGIK ---\
st.title("\uc0\u55356 \u57151  NEM-Check: Analyse-Tool")\
st.write("Bewertungstool basierend auf den Standards f\'fcr optimale Nahrungserg\'e4nzung[cite: 5, 15].")\
\
with st.sidebar:\
    st.header("1. Produkteingabe")\
    name = st.text_input("Produktname", "Unbekanntes Produkt")\
    monatspreis = st.number_input("Preis pro Monat (\'80)", min_value=1.0, value=30.0)\
    \
    st.header("2. Merkmale w\'e4hlen")\
    st.subheader("Positive Eigenschaften")\
    pos_auswahl = [k for k in PLUS_KRITERIEN.keys() if st.checkbox(k)]\
    \
    st.subheader("Negative Eigenschaften")\
    neg_auswahl = [k for k in MINUS_KRITERIEN.keys() if st.checkbox(k)]\
\
# --- BERECHNUNG ---\
score = len(pos_auswahl) - len(neg_auswahl)\
preis_pro_tag = monatspreis / 30\
effizienz = score / preis_pro_tag if preis_pro_tag > 0 else 0\
\
# --- AUSGABE ---\
st.header(f"Analyse: \{name\}")\
\
c1, c2, c3 = st.columns(3)\
with c1:\
    st.metric("Qualit\'e4ts-Score", score)\
with c2:\
    st.metric("Preis pro Tag", f"\{preis_pro_tag:.2f\} \'80")\
with c3:\
    st.metric("Effizienz-Index", f"\{effizienz:.1f\}")\
\
st.divider()\
\
col_left, col_right = st.columns(2)\
with col_left:\
    st.subheader("\uc0\u9989  St\'e4rken")\
    for p in pos_auswahl:\
        st.success(f"**\{p\}**: \{PLUS_KRITERIEN[p]\}")\
\
with col_right:\
    st.subheader("\uc0\u10060  Schwachstellen")\
    for n in neg_auswahl:\
        st.error(f"**\{n\}**: \{MINUS_KRITERIEN[n]\}")\
\
# --- FAZIT ---\
st.subheader("Experten-Fazit")\
if score >= 7 and preis_pro_tag <= 1.50:\
    st.balloons()\
    st.info(f"Dieses Produkt entspricht fast ideal den Kriterien von Dr. H\'fcther (Optimal: Fl\'fcssig, Natur, G\'fcnstig)[cite: 6, 13, 20].")\
elif score < 0:\
    st.warning("Vorsicht: Die negativen Merkmale (Isolate, Kapseln, Chemie) \'fcberwiegen.")\
else:\
    st.write("Das Produkt liegt im Mittelfeld. Pr\'fcfen Sie, ob eine fl\'fcssige Alternative wirtschaftlicher w\'e4re.")}