import os
import sys
# Injection de sécurité pour le dossier racine
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from typing import Any, TypedDict
from langgraph.graph import StateGraph, END

from agents.extractor import extract_and_store
from agents.analyzer import analyze_risks
from agents.writer import write_summary