import os
from langchain_groq import ChatGroq

def write_summary(state):
    # 1. Récupérer l'analyse générée par l'agent précédent
    if isinstance(state, dict):
        analysis = state.get("analysis", "")
    else:
        analysis = state.analysis

    # 2. Configurer le modèle Groq (gratuit, rapide et distant)
    llm = ChatGroq(
        temperature=0.3,
        model_name="llama-3.1-8b-instant",
        groq_api_key=os.environ.get("GROQ_API_KEY")
    )
    
    # 3. Préparer le prompt pour le résumé destiné aux dirigeants
    prompt = f"""Tu es un expert en communication financière auprès de comités de direction.
À partir de l'analyse détaillée des risques ci-dessous, rédige une synthèse exécutive (Summary) claire, concise et percutante.
Structure ta réponse sous forme de paragraphes fluides (pas de style haché ligne par ligne).

Analyse détaillée :
{analysis}"""
    
    try:
        response = llm.invoke(prompt)
        summary_genere = response.content
    except Exception as e:
        # En cas de problème avec l'API, repli de secours
        summary_genere = f"### Synthèse Exécutive de Secours\n\nL'analyse met en évidence les points clés extraits dans le rapport d'analyse des risques."

    # 4. Mettre à jour l'état du graphe avec le résumé
    return {"summary": summary_genere}