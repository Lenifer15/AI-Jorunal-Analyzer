# 📝 AI Journal Analyzer

## 📌 Project Overview
AI Journal Analyzer is an intelligent journaling assistant that analyzes your daily journal entries using Large Language Models. It detects your mood, extracts key themes, and generates personalized motivational insights — all powered by LangGraph, LangChain, and Groq's blazing-fast LLaMA model.

---

## 🚀 Features
- 😊 Mood detection with score (1–10) and reasoning
- 🗂️ Key theme extraction with one-line summary
- 💡 Personalized motivational insights and action suggestions
- ⚡ Powered by Groq (free & ultra-fast inference)
- 🔁 LangGraph 3-node pipeline (Mood → Themes → Insights)
- 🎨 Clean and interactive Streamlit UI

---

## 🧠 Technologies Used
- [LangChain](https://www.langchain.com/) — Prompt chaining and LLM interaction
- [LangGraph](https://langchain-ai.github.io/langgraph/) — Multi-node stateful pipeline orchestration
- [Groq API](https://console.groq.com/) — Ultra-fast LLaMA 3.3 70B inference
- [Streamlit](https://streamlit.io/) — Interactive web UI
- [Python-dotenv](https://pypi.org/project/python-dotenv/) — Environment variable management

---

## ⚙️ How It Works
1. User writes a journal entry in the Streamlit UI
2. **Node 1 — Mood Detector:** LLM analyzes emotional tone, assigns mood label and score
3. **Node 2 — Theme Extractor:** LLM identifies top 3 key themes and generates a summary
4. **Node 3 — Insight Generator:** LLM produces 3 personalized motivational insights based on mood and themes
5. Results are displayed in a clean two-column layout with metrics and info cards

---

## 🛠️ Installation

Clone the repository and set up the environment:

    git clone https://github.com/Lenifer15/AI-Journal-Analyzer.git
    cd AI-Journal-Analyzer

    python -m venv venv
    venv\Scripts\activate

    pip install langchain langchain-groq langchain-core langgraph streamlit python-dotenv

Create a `.env` file in the root folder and add your Groq API key:

    GROQ_API_KEY=your_groq_api_key_here

Get your free Groq API key at https://console.groq.com/

---

## ▶️ Usage

    streamlit run app.py --server.fileWatcherType none

Then open your browser at http://localhost:8501

---

## 💡 Example

**Input:**

    Today was a tough day at work. I felt overwhelmed with deadlines and couldn't focus.
    I kept procrastinating and now I'm worried about falling behind.

**Output:**

    😰 Mood Detected : Anxious
    Mood Score       : 7/10
    Reason           : Writer expresses stress, overwhelm, and worry about performance

    🗂️ Key Themes    : Work Stress, Procrastination, Self-Doubt
    Summary          : A day marked by pressure and loss of focus at work

    💡 Insights:
    1. Break your tasks into smaller steps to reduce the feeling of overwhelm.
    2. Practice a 5-minute mindfulness reset before starting your next task.
    3. Remember that one tough day does not define your overall productivity.

---

## 📁 Folder Structure

    AI-Journal-Analyzer/
    │
    ├── app.py              # Streamlit UI
    ├── pipeline.py         # LangGraph 3-node pipeline
    ├── chains.py           # LangChain LLM chains
    ├── prompts.py          # Prompt templates
    ├── requirements.txt    # Project dependencies
    └── .env                # Groq API key (not committed)

---

## 🤝 Contributing
- Fork the repository
- Create a new branch: git checkout -b feature/your-feature
- Commit your changes: git commit -m 'Add your feature'
- Push to the branch: git push origin feature/your-feature
- Open a Pull Request

---

## 📄 License
MIT

---

## Author
**Jessica Lenefer R.**
