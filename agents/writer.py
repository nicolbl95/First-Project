from langchain_ollama import OllamaLLM

def write_summary(analysis: str):
    prompt = f"""Tu es expert en communication financière.
    Analyse brute des risques :
    {analysis}
    Rédige une synthèse en 3 paragraphes pour un dirigeant non-expert.
    Utilise un langage simple et des exemples concrets."""

    llm = OllamaLLM(model="llama3")
    return llm.invoke(prompt)