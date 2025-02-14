import streamlit as st
from wiki import wiki_app
from outlook_calendar import calendar_app  # si vous l'avez renommé
# Assurez-vous que ton_script.py ne contient pas d'appel à set_page_config()
from ton_script import dashboard_app

# Appeler set_page_config() en tout premier, avant tout autre appel Streamlit
st.set_page_config(
    page_title="Dashboard Outils de Gestion de Parc", layout="wide")


def main():
    dashboard_app()
    st.markdown("<hr>", unsafe_allow_html=True)
    calendar_app()
    st.markdown("<hr>", unsafe_allow_html=True)
    wiki_app()


if __name__ == "__main__":
    main()
