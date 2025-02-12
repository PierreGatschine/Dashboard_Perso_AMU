

import streamlit as st
from wiki import wiki_app  # Import de la fonction wiki_app depuis wiki.py
from ton_script import dashboard_app  # Import de la fonction dashboard_app depuis ton_script.py


def main():
    # Affiche le dashboard en haut de la page
    dashboard_app()

    # Séparation visuelle
    st.markdown("<hr>", unsafe_allow_html=True)

    # Appel de la fonctionnalité wiki (définie dans wiki.py)
    wiki_app()


if __name__ == "__main__":
    main()
