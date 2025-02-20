import streamlit as st
from wiki import wiki_app
from outlook_calendar import calendar_app  # si vous l'avez renommé
from grafana_view import grafana_app  # Import de la vue Grafana
# Assurez-vous que ton_script.py ne contient pas d'appel à set_page_config()
from ton_script import dashboard_app

# Appeler set_page_config() en tout premier, avant tout autre appel Streamlit
st.set_page_config(
    page_title="Dashboard Outils de Gestion de Parc", layout="wide")


def main():
    # Première ligne : deux colonnes, avec ratio 2:1
    col1, col2 = st.columns([3, 1])
    with col1:
        dashboard_app()
    
    with col2:
        calendar_app()

    # Deuxième ligne : affichage du wiki sur toute la largeur
    #st.markdown("<hr>", unsafe_allow_html=True)
    wiki_app()
    #st.markdown("<hr>", unsafe_allow_html=True)
    #grafana_app()    # Affiche la vue Grafana
    #calendar_app()
   
   


if __name__ == "__main__":
    main()
