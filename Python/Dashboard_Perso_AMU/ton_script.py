import streamlit as st
import streamlit.components.v1 as components
from svgs import FACILIT_AMU, ENT, SESAME, GRAFANA, GESTION, DASHBOARD


def load_css(file_name):
    """Charge et retourne le contenu du fichier CSS."""
    with open(file_name, encoding="utf-8") as f:
        return f.read()


def get_ico_svg(lien):
    """
    Retourne le code HTML de l'icône pour le lien.
    
    - Si 'icone' commence par "http", on retourne une balise <img>.
    - Sinon, on utilise un dictionnaire de correspondance pour retourner
      le SVG défini dans svgs.py.
    """
    if lien["icone"].startswith("http"):
        return f'<img src="{lien["icone"]}" alt="{lien["nom"]}" style="max-height: 50px;">'

    mapping = {
        "AMU": FACILIT_AMU,
        "LogoAMU": FACILIT_AMU,
        "🔧": ENT,
        "Sésame": SESAME,
        "GESTION": GESTION,
        "GRAFANA": GRAFANA,
        "DASHBOARD": DASHBOARD
    }
    key = lien["icone"]
    return mapping.get(key, f'<div class="emoji-icon">{lien["icone"]}</div>')


def dashboard_app():
    # Configuration de la page
    ##   page_title="Dashboard outils de gestion de parc", layout="wide")
    css_content = load_css("main.css")

    # Injection du CSS dans la page
    #st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

    # Affichage du titre avec du HTML personnalisé pour forcer la police
    st.header("MyDashboard")
    #st.subheader("Liens vers les outils de gestion")

    # Liste des liens avec icônes
    liens = [
        {
            "nom": "Facilit'AMU",
            "url": "https://facilitamu.univ-amu.fr/front/central.php",
            "icone": "GESTION"
        },
        {
            "nom": "ENT",
            "url": "https://ent.univ-amu.fr/",
            "icone": "DASHBOARD"
        },
        {
            "nom": "Sésame",
            "url": "https://sesame.univ-amu.fr/admin/",
            "icone": "AMU"
        },
        {
            "nom": "GLPI",
            "url": "https://m-glpi.univ-amu.fr/front/dashboard_assets.php",
            # Ici vous pouvez ajuster selon vos besoins (ou utiliser une URL)
            "icone": "Sésame"
        },
        {
            "nom": "Grafana",
            "url": "https://dashboard-it.univ-amu.fr/d/ddn2tfvvim1ogf/facilit-amu-pour-les-equipes?orgId=1&refresh=1m&var-Equipe=46&var-Gestionnaire=19478&var-Zone=$__all&from=now-2y&to=now&timezone=browser",
            "icone": GRAFANA # Utilisation de "AMU" pour afficher FACILIT_AMU
        },
        {
            "nom": "Courrier",
            "url": "https://mail.univ-amu.fr/owa/#path=/mail",
            "icone": GRAFANA  # Utilisation de "AMU" pour afficher FACILIT_AMU
        },
        {
            "nom": "Calendrier",
            "url": "https://mail.univ-amu.fr/owa/#path=/calendar/view/Week",
            "icone": GRAFANA  # Utilisation de "AMU" pour afficher FACILIT_AMU
        }
    ]

    # Construction du HTML pour les cartes
    cards_html = '<div class="dashboard">'
    for lien in liens:
        icon_html = get_ico_svg(lien)
        cards_html += f'''
        <div class="card">
            <a href="{lien["url"]}" target="_blank">
                {icon_html}
                <h3>{lien["nom"]}</h3>
            </a>
        </div>
        '''
    cards_html += '</div>'


    full_html = f'''
    <html>
      <head>
        <meta charset="utf-8">
        <style>{css_content}</style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Sortable/1.14.0/Sortable.min.js"></script>
      </head>
      <body>
        {cards_html}
        <script>
          // Rendre le conteneur de cartes sortable
          var el = document.querySelector('.dashboard');
          Sortable.create(el, {{
            animation: 150,
            onEnd: function (evt) {{
              console.log("Carte déplacée : nouvelle position", evt.newIndex);
              // Vous pouvez ajouter ici une logique pour sauvegarder l'ordre si besoin.
            }}
          }});
        </script>
      </body>
    </html>
    '''

    # Affichage du contenu HTML via un composant Streamlit
    components.html(full_html, height=500, scrolling=True)


