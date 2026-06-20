import os
from langchain_ollama import OllamaLLM

def write_summary(state):
    if isinstance(state, dict):
        analysis = state.get("analysis", "")
    else:
        analysis = state.analysis

    if not isinstance(analysis, str):
        raise ValueError("analysis must be a string")

    prompt = f"""Tu es expert en communication financière.
    Analyse brute des risques :
    {analysis}
    Rédige une synthèse en 3 paragraphes pour un dirigeant non-expert.
    Utilise un langage simple et des exemples concrets."""

    # Utilisation d'Ollama comme fallback pour l'exécution locale
    llm = OllamaLLM(model="llama3")

    response = llm.invoke(prompt)
    summary = response if isinstance(response, str) else getattr(response, "content", str(response))
    
    return {"summary": summary}