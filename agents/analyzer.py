from langchain_ollama import OllamaLLM

def analyze_risks(collection):
    results = collection.query(
        query_texts=["risques financiers, dettes, pertes, incohérences"],
        n_results=5
    )
    context = "\n".join(results["documents"][0])

    prompt = f"""Tu es un analyste financier expert.
    Voici des extraits d'un rapport financier :
    {context}
    Identifie les 3 principaux risques ou incohérences."""

    llm = OllamaLLM(model="llama3")
    return llm.invoke(prompt)