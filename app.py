import streamlit as st
from pipeline import analyze_journal

st.set_page_config(page_title="AI Journal Analyzer", page_icon="📝", layout="centered")

st.title("📝 AI Journal Analyzer")
st.markdown("Write your journal entry and get mood analysis, themes & insights instantly.")

journal_input = st.text_area(
    "✍️ Write your journal entry here:",
    placeholder="Today was a tough day at work. I felt overwhelmed with tasks...",
    height=200
)

if st.button("🔍 Analyze My Journal", key="analyze_btn"):
    if journal_input.strip():
        with st.spinner("Analyzing your journal..."):
            result = analyze_journal(journal_input)

        mood_emoji = {
            "happy": "😊", "sad": "😢", "anxious": "😰",
            "angry": "😠", "neutral": "😐", "excited": "🤩"
        }
        emoji = mood_emoji.get(result["mood"].lower(), "🧠")

        st.markdown("---")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f"{emoji} Mood Detected")
            st.metric("Mood", result["mood"].capitalize())
            st.metric("Mood Score", f"{result['mood_score']}/10")
            st.caption(f"💬 {result['mood_reason']}")

        with col2:
            st.subheader("🗂️ Key Themes")
            for theme in result["themes"]:
                st.markdown(f"- {theme}")
            st.caption(f"📌 {result['summary']}")

        st.markdown("---")
        st.subheader("💡 Insights & Suggestions")
        for i, insight in enumerate(result["insights"], 1):
            st.info(f"{i}. {insight}")
    else:
        st.warning("Please write something in your journal first!")