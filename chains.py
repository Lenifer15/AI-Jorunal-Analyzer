import os
import json
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from prompts import MOOD_PROMPT, THEME_PROMPT, INSIGHT_PROMPT

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY")
)

def detect_mood(journal: str) -> dict:
    prompt = PromptTemplate.from_template(MOOD_PROMPT)
    chain = prompt | llm
    result = chain.invoke({"journal": journal})
    text = result.content.strip()
    start = text.find("{")
    end = text.rfind("}") + 1
    return json.loads(text[start:end])

def extract_themes(journal: str) -> dict:
    prompt = PromptTemplate.from_template(THEME_PROMPT)
    chain = prompt | llm
    result = chain.invoke({"journal": journal})
    text = result.content.strip()
    start = text.find("{")
    end = text.rfind("}") + 1
    return json.loads(text[start:end])

def generate_insights(mood: str, themes: list) -> dict:
    prompt = PromptTemplate.from_template(INSIGHT_PROMPT)
    chain = prompt | llm
    result = chain.invoke({
        "mood": mood,
        "themes": ", ".join(themes)
    })
    text = result.content.strip()
    start = text.find("{")
    end = text.rfind("}") + 1
    return json.loads(text[start:end])