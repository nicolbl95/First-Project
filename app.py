import os
import sys

# 1. Configurer la variable d'environnement Protobuf
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

# 2. Configuration des chemins du package agents
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

sys.modules['agents'] = __import__('agents')

import streamlit as st
import tempfile
from graph_builder import AgentState, build_graph # Importation depuis graph_builder

# On initialise le graphe une seule fois au chargement global
graph = build_graph()

st.set_page_config(page_title="Analyseur Financier IA", page_icon="📊")
st.title("Assistant IA — Analyse Financière Multi-Agents")
st.write("Déposez un rapport financier PDF. 3 agents IA l'analysent en séquence.")

with st.sidebar:
    st.header("Architecture du système")
    st.write("1. Agent Extracteur (ChromaDB + RAG)")
    st.write("2. Agent Analyste (ChromaDB + Query)")
    st.write("3. Agent Rédacteur (LangGraph + Groq)")

def run_analysis(pdf_path: str):
    with st.status("Traitement du document par les agents IA...", expanded=True) as status:
        st.write("🕵️‍♂️ Étape 1 : L'Agent Extracteur récupère le texte du PDF...")
        st.write("🧠 Étape 2 : L'Agent Analyste évalue les risques financiers...")
        st.write("✍️ Étape 3 : L'Agent Rédacteur finalise la synthèse...")

        input_state: AgentState = {"pdf_path": pdf_path}
        result = graph.invoke(input_state)
        status.update(label="Analyse terminée avec succès !", state="complete", expanded=False)

    return result

uploaded_file = st.file_uploader("Choisir un PDF", type="pdf")

st.write("Ou bien sélectionnez un rapport PDF d'exemple pour lancer l'analyse immédiatement.")

example_reports = {
    "BioSensus 2025": r"C:\Users\nicol\Documents\First project\Rapport_Performance_BioSensus_2025.pdf",
    "TechNova": r"C:\Users\nicol\Documents\First project\Rapport_Financier_TechNova.pdf",
    "OmniDrive": r"C:\Users\nicol\Documents\First project\Rapport_Financier_Avance_OmniDrive.pdf",
}

cols = st.columns(len(example_reports))
selected_example = None
for col, (label, path) in zip(cols, example_reports.items()):
    if col.button(label):
        selected_example = path

result = None

if selected_example is not None:
    if not os.path.exists(selected_example):
        st.error(f"Fichier d'exemple introuvable : {selected_example}")
    else:
        result = run_analysis(selected_example)
elif uploaded_file and st.button("Lancer l'analyse IA"):
    # Création du fichier temporaire
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    result = run_analysis(tmp_path)

    # Nettoyage du fichier temporaire après l'analyse
    if os.path.exists(tmp_path):
        os.unlink(tmp_path)

if result is not None:
    st.subheader("Analyse des risques")
    st.markdown(result.get("analysis", "Aucune analyse générée."))

    st.subheader("Synthèse pour dirigeants")
    st.markdown(result.get("summary", "Aucune synthèse générée."))