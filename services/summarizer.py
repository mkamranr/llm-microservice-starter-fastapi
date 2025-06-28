from openai import OpenAI
from app.config import OPENAI_API_KEY, MODEL_SUMMARIZATION

client = OpenAI(api_key=OPENAI_API_KEY)

def summarize(text: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_SUMMARIZATION,
        messages=[{"role": "user", "content": f"Summarize this:\\n{text}"}]
    )
    return response.choices[0].message.content.strip()
