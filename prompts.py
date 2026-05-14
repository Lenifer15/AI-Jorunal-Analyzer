MOOD_PROMPT = """
You are an emotional intelligence expert.
Analyze the journal entry below and detect the writer's mood.

Return a JSON like:
{{"mood": "happy/sad/anxious/angry/neutral/excited", "mood_score": 1-10, "reason": "brief reason"}}

Journal: {journal}

Return ONLY valid JSON. No explanation.
"""

THEME_PROMPT = """
You are a journaling coach.
Extract the top 3 key themes from this journal entry.

Return a JSON like:
{{"themes": ["theme1", "theme2", "theme3"], "summary": "one line summary"}}

Journal: {journal}

Return ONLY valid JSON. No explanation.
"""

INSIGHT_PROMPT = """
You are a supportive life coach.
Based on the mood: {mood} and themes: {themes},
write 3 short motivational insights or action suggestions for the writer.

Return a JSON like:
{{"insights": ["insight1", "insight2", "insight3"]}}

Return ONLY valid JSON. No explanation.
"""