from typing import TypedDict
from langgraph.graph import StateGraph, END
from chains import detect_mood, extract_themes, generate_insights

# --- State ---
class JournalState(TypedDict):
    journal: str
    mood: str
    mood_score: int
    mood_reason: str
    themes: list
    summary: str
    insights: list

# --- Nodes ---
def mood_node(state: JournalState) -> JournalState:
    result = detect_mood(state["journal"])
    return {
        **state,
        "mood": result["mood"],
        "mood_score": result["mood_score"],
        "mood_reason": result["reason"]
    }

def theme_node(state: JournalState) -> JournalState:
    result = extract_themes(state["journal"])
    return {
        **state,
        "themes": result["themes"],
        "summary": result["summary"]
    }

def insight_node(state: JournalState) -> JournalState:
    result = generate_insights(state["mood"], state["themes"])
    return {
        **state,
        "insights": result["insights"]
    }

# --- Build Graph ---
def build_pipeline():
    workflow = StateGraph(JournalState)
    workflow.add_node("detect_mood", mood_node)
    workflow.add_node("extract_themes", theme_node)
    workflow.add_node("generate_insights", insight_node)

    workflow.set_entry_point("detect_mood")
    workflow.add_edge("detect_mood", "extract_themes")
    workflow.add_edge("extract_themes", "generate_insights")
    workflow.add_edge("generate_insights", END)

    return workflow.compile()

pipeline = build_pipeline()

def analyze_journal(journal_text: str) -> JournalState:
    return pipeline.invoke({
        "journal": journal_text,
        "mood": "",
        "mood_score": 0,
        "mood_reason": "",
        "themes": [],
        "summary": "",
        "insights": []
    })