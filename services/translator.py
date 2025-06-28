from openai import OpenAI
from app.config import OPENAI_API_KEY, MODEL_TRANSLATION

client = OpenAI(api_key=OPENAI_API_KEY)

def translate(text: str, target_lang: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_TRANSLATION,
        messages=[{"role": "user", "content": f"Translate to {target_lang}: {text}"}]
    )
    return response.choices[0].message.content.strip()
