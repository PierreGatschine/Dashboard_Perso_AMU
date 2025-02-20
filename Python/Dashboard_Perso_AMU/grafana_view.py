import streamlit as st
import streamlit.components.v1 as components


def grafana_app():
    st.header("Vue Grafana")

    # URL du dashboard Grafana (remplacez par la vôtre si besoin)
    grafana_url = (
        "https://facilitamu.univ-amu.fr/front/ticket.php?is_deleted=0&as_map=0&browse=0&itemtype=Ticket&sort%5B0%5D=19&order%5B0%5D=DESC&savedsearches_id=51&criteria%5B0%5D%5Blink%5D=AND&criteria%5B0%5D%5Bfield%5D=5&criteria%5B0%5D%5Bsearchtype%5D=equals&criteria%5B0%5D%5Bvalue%5D=19478&criteria%5B1%5D%5Blink%5D=AND&criteria%5B1%5D%5Bfield%5D=12&criteria%5B1%5D%5Bsearchtype%5D=equals&criteria%5B1%5D%5Bvalue%5D=process&reset=reset"
    
    )

    # Code HTML avec CSS pour un iframe responsive et avec border-radius
    iframe_code = f"""
    <style>
      .responsive-iframe {{
        position: relative;
        width: 100%;
        padding-top: 56.25%; /* Aspect ratio 16:9 */
        overflow: hidden;
        border-radius: 10px;
      }}
      .responsive-iframe iframe {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: none;
        border-radius: 10px;
      }}
    </style>
    <div class="responsive-iframe">
      <iframe src="{grafana_url}" allowtransparency="true" scrolling="no"></iframe>
    </div>
    """

    # Affiche l'iframe dans l'application Streamlit
    components.html(iframe_code, height=600, scrolling=True)


if __name__ == "__main__":
    grafana_app()
