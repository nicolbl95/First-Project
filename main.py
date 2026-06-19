from typing import Any, TypedDict

from langgraph.graph import StateGraph, END
from agents.extractor import extract_and_store
from agents.analyzer import analyze_risks
from agents.writer import write_summary


class WorkflowState(TypedDict, total=False):
    pdf_path: str
    collection: Any
    analysis: str
    summary: str


def extract(state: WorkflowState) -> WorkflowState:
    assert "pdf_path" in state, "pdf_path is required"
    pdf_path = state["pdf_path"]
    collection = extract_and_store(pdf_path)
    return {"pdf_path": pdf_path, "collection": collection}


def analyze(state: WorkflowState) -> WorkflowState:
    assert "pdf_path" in state, "pdf_path is required"
    assert "collection" in state, "collection is required"
    return {
        "pdf_path": state["pdf_path"],
        "collection": state["collection"],
        "analysis": analyze_risks(state["collection"]),
    }


def write(state: WorkflowState) -> WorkflowState:
    assert "pdf_path" in state, "pdf_path is required"
    assert "collection" in state, "collection is required"
    assert "analysis" in state, "analysis is required"
    return {
        "pdf_path": state["pdf_path"],
        "collection": state["collection"],
        "analysis": state["analysis"],
        "summary": write_summary(state["analysis"]),
    }


def build_graph():
    workflow = StateGraph(WorkflowState)

    workflow.add_node(extract)
    workflow.add_node(analyze)
    workflow.add_node(write)

    workflow.set_entry_point("extract")
    workflow.add_edge("extract", "analyze")
    workflow.add_edge("analyze", "write")
    workflow.add_edge("write", END)
    return workflow.compile()


if __name__ == "__main__":
    graph = build_graph()
    input_state: WorkflowState = {"pdf_path": "rapport.pdf"}
    result = graph.invoke(input_state)
    print(result["summary"])
