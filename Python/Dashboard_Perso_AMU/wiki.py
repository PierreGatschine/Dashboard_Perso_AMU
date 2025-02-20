import sqlite3
import streamlit as st


def init_db():
    """
    Initialise la base de données et crée la table 'solutions' si elle n'existe pas.
    """
    conn = sqlite3.connect("wiki.db", check_same_thread=False)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS solutions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    return conn


def add_solution(conn, title, content):
    """
    Ajoute une solution dans la base de données.
    """
    c = conn.cursor()
    c.execute("INSERT INTO solutions (title, content) VALUES (?, ?)",
              (title, content))
    conn.commit()


def get_solutions(conn):
    """
    Récupère toutes les solutions classées par date décroissante.
    """
    c = conn.cursor()
    c.execute(
        "SELECT id, title, content, created_at FROM solutions ORDER BY created_at DESC")
    return c.fetchall()


def update_solution(conn, solution_id, new_title, new_content):
    """
    Met à jour une solution existante.
    """
    c = conn.cursor()
    c.execute("UPDATE solutions SET title = ?, content = ? WHERE id = ?",
              (new_title, new_content, solution_id))
    conn.commit()


def delete_solution(conn, solution_id):
    """
    Supprime une solution de la base de données.
    """
    c = conn.cursor()
    c.execute("DELETE FROM solutions WHERE id = ?", (solution_id,))
    conn.commit()


def wiki_app():
    """
    Affiche l'interface du wiki avec les fonctionnalités CRUD.
    """
    st.header("MyWiki")

    # Initialisation ou récupération de la base de données
    conn = init_db()

    # --- Création d'une nouvelle solution ---
    #st.subheader("")
    with st.form("create_solution"):
        new_title = st.text_input("Titre de la solution", key="new_title")
        new_content = st.text_area("Contenu de la solution", key="new_content")
        submitted_create = st.form_submit_button("Ajouter")
        if submitted_create:
            if new_title and new_content:
                add_solution(conn, new_title, new_content)
                st.success("Solution ajoutée avec succès !")
                #st.experimental_rerun()  # Rafraîchit l'interface pour afficher la nouvelle solution
            else:
                st.error("Veuillez renseigner le titre et le contenu.")

    # --- Lecture et affichage des solutions ---
    st.subheader("Solutions déposées")
    solutions = get_solutions(conn)
    if solutions:
        for solution in solutions:
            st.markdown(f"### {solution[1]}")
            st.write(solution[2])
            st.caption(f"Ajoutée le {solution[3]}")

            # Création de deux colonnes pour les boutons Modifier et Supprimer
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Modifier", key=f"edit_{solution[0]}"):
                    # Stockage des informations de la solution dans st.session_state pour édition
                    st.session_state["edit_id"] = solution[0]
                    st.session_state["edit_title"] = solution[1]
                    st.session_state["edit_content"] = solution[2]
            with col2:
                if st.button("Supprimer", key=f"delete_{solution[0]}"):
                    delete_solution(conn, solution[0])
                    st.success("Solution supprimée")
                    #st.experimental_rerun()

            # Si une solution est sélectionnée pour modification, afficher un formulaire d'édition
            if "edit_id" in st.session_state and st.session_state["edit_id"] == solution[0]:
                st.subheader("Modifier la solution")
                with st.form(key=f"edit_form_{solution[0]}"):
                    edit_title = st.text_input(
                        "Titre", value=st.session_state["edit_title"], key=f"edit_title_{solution[0]}")
                    edit_content = st.text_area(
                        "Contenu", value=st.session_state["edit_content"], key=f"edit_content_{solution[0]}")
                    submitted_edit = st.form_submit_button("Mettre à jour")
                    if submitted_edit:
                        update_solution(
                            conn, solution[0], edit_title, edit_content)
                        st.success("Solution mise à jour !")
                        # Nettoyage de la session d'édition
                        st.session_state.pop("edit_id", None)
                        st.session_state.pop("edit_title", None)
                        st.session_state.pop("edit_content", None)
                        #st.experimental_rerun()
    else:
        st.info("Aucune solution déposée pour le moment.")
