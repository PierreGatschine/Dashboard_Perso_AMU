# calendar.py

import streamlit as st
import streamlit.components.v1 as components


def load_css(file_name):
    """Charge et retourne le contenu du fichier CSS."""
    with open(file_name, encoding="utf-8") as f:
        return f.read()

def calendar_app():
    # Chargement du CSS
    css = load_css("main.css")
    st.header("MyCalendrier")
    cards_html = '<div class="dashboard">'
    # Remplacez par l'URL publique de votre calendrier Outlook
    calendar_url = "https://mail.univ-amu.fr/owa/calendar/388bbaa1c28c444f8326fe28b5e5429b@univ-amu.fr/0518d4f644d54aeda26cef55796ccbf12180997605482452348/calendar.html"

    iframe_code = f"""
    <style>
      /* Conteneur responsive avec aspect ratio 16:9 par défaut et border-radius */
      .responsive-iframe {{
        position: relative;
        width: 100%;
        height: 65px;
        padding-top: 56.25%; /* 16:9 ratio */
        overflow: hidden;
        border: 0.05px solid #ddd;
        border-radius: 10px;
      }}
      .responsive-iframe iframe {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: none;
        background: transparent;
        border-radius: 10px;
      }}
      /* Ajustement pour les écrans plus petits (ex. ratio 4:3) */
      @media (max-width: 768px) {{
        .responsive-iframe {{
          padding-top: 75%; /* Ratio 4:3 */
        }}
      }}
    </style>
    <div class="responsive-iframe">
      <iframe src="{calendar_url}" allowtransparency="true" scrolling="no"></iframe>
    </div>
    """

    components.html(iframe_code, height=500, scrolling=True)
