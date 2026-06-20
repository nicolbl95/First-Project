import chromadb
# Importe ton client LLM ici si nécessaire (ex: de langchain_community.llms import Ollama ou autre)

def analyze_risks(state):
    # 1. Récupérer le texte brut ou l'état si besoin
    if isinstance(state, dict):
        raw_text = state.get("raw_text", "")
    else:
        raw_text = state.raw_text

    # 2. Re-connecter au client ChromaDB local pour interroger la collection
    client = chromadb.Client()
    collection = client.get_or_create_collection("financial_doc")

    # 3. Effectuer la requête RAG sur la collection
    # On cherche par exemple les segments parlant de "risques" ou "financier"
    results = collection.query(
        query_texts=["risques financiers, dépendances, réglementation, change"],
        n_results=5
    )
    
    # Récupération des fragments de texte trouvés
    documents_trouves = results.get("documents", [[]])[0]
    contexte_rag = "\n".join(documents_trouves)

    # 4. Simulation ou appel de ton modèle IA (Ollama / Llama 3) avec le contexte
    # Remplace cette ligne par ton vrai appel LLM si tu as une variable spécifique
    analyse_generee = f"Analyste IA - Analyse basée sur le contexte extrait :\n\n{contexte_rag}\n\n[Analyse des risques complétée]"

    # 5. On met à jour l'état du graphe avec le résultat de l'analyse
    return {"analysis": analyse_generee}