import os
import shutil
import chromadb
from dotenv import load_dotenv
from pydantic import SecretStr

load_dotenv()

try:
    from langchain_groq import ChatGroq
except ImportError:
    ChatGroq = None

try:
    from langchain_ollama import OllamaLLM
except ImportError:
    OllamaLLM = None


def get_analyzer_llm():
    groq_api_key = os.environ.get("GROQ_API_KEY")

    if ChatGroq is not None and groq_api_key:
        return ChatGroq(
            temperature=0.95,
            model="llama-3.1-8b-instant",
            api_key=SecretStr(groq_api_key),
        )

    if OllamaLLM is not None and shutil.which("ollama"):
        return OllamaLLM(model="llama3")

    return None


def analyze_risks(state):
    # 1. Récupération sécurisée du texte brut et de la langue (FR par défaut)
    if isinstance(state, dict):
        raw_text = state.get("raw_text", "")
        lang = state.get("language", "FR")
    else:
        raw_text = state.raw_text
        lang = getattr(state, "language", "FR")

    # 2. Cartographie de la langue cible pour forcer le LLM à s'adapter
    lang_mapping = {
        "FR": "français (French)",
        "EN": "anglais (English)",
        "ES": "espagnol (Spanish)"
    }
    target_language_name = lang_mapping.get(lang, "français (French)")

    client = chromadb.Client()
    collection = client.get_or_create_collection("financial_doc")

    results = collection.query(
        query_texts=["risques financiers, dépendances, réglementation, change"],
        n_results=5,
    )

    documents = results.get("documents") or []
    documents_trouves = documents[0] if documents else []
    contexte_propre = " ".join([doc.replace("\n", " ").strip() for doc in documents_trouves])

    llm = get_analyzer_llm()
    analyse_generee = None

    if llm is not None:
        # 3. PROMPT MODIFIÉ : Ordre absolu de rédiger dans la langue cible dès le départ
        prompt = f"""You are a senior financial analyst and risk management expert.
CRITICAL LANGUAGE DIRECTIVE: You must write the entire output, response, headers, and professional analysis exclusively in {target_language_name}. Do NOT use any other language.

À partir des données extraites du document, rédige une analyse détaillée des risques financiers de l'entreprise.
Structure ta réponse avec des paragraphes fluides, rédigés et professionnels.

CRITIQUE : Pour illustrer ton analyse, tu DOIS insérer de manière fluide exactement 1 ou 2 balises graphiques parmi les suivantes, au moment le plus opportun dans ton texte (juste après ou pendant que tu évoques des chiffres clés) :
- Insère la balise [GRAPH_EVOLUTION] si tu parles de la trajectoire globale, de la croissance ou de l'historique de l'entreprise.
- Insère la balise [GRAPH_REPARTITION] si tu parles de la structure du capital, de la répartition de la dette ou de la provenance des revenus.
- Insère la balise [GRAPH_PERFORMANCE] si tu analyses la rentabilité, les marges, l'EBITDA ou les coûts opérationnels/R&D.

Fais en sorte que ces balises soient écrites sur leur propre ligne entre deux paragraphes.

Données du document :
{raw_text}"""
        try:
            response = llm.invoke(prompt)
            analyse_generee = response if isinstance(response, str) else getattr(response, "content", str(response))
        except Exception:
            analyse_generee = None

    # 4. Traduction dynamique du mode de secours selon le choix de l'utilisateur
    if not analyse_generee:
        if lang == "EN":
            analyse_generee = (
                "### Risk Analysis (Backup Mode)\n\n"
                "No AI backend available or generation error. Here is the extracted context:\n\n"
                f"{contexte_propre}"
            )
        elif lang == "ES":
            analyse_generee = (
                "### Análisis de Riesgos (Modo de Reserva)\n\n"
                "No hay backend de IA disponible o error de generación. Aquí está el contexto extraído:\n\n"
                f"{contexte_propre}"
            )
        else:
            analyse_generee = (
                "### Analyse des Risques (Mode de secours)\n\n"
                "Aucun backend IA disponible ou erreur de génération. Voici le contexte extrait :\n\n"
                f"{contexte_propre}"
            )

    return {"analysis": analyse_generee}