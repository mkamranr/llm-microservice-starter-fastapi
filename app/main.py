from fastapi import FastAPI
from pydantic import BaseModel
from app.services.summarizer import summarize
from app.services.translator import translate
from app.services.embedder import embed

app = FastAPI()

class TextInput(BaseModel):
    text: str

class TranslateInput(TextInput):
    target_lang: str

@app.post("/summarize")
def summarize_text(input: TextInput):
    return {"summary": summarize(input.text)}

@app.post("/translate")
def translate_text(input: TranslateInput):
    return {"translation": translate(input.text, input.target_lang)}

@app.post("/embed")
def embed_text(input: TextInput):
    return {"embedding": embed(input.text)}
