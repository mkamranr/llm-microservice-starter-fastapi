from sentence_transformers import SentenceTransformer
from app.config import EMBED_MODEL

model = SentenceTransformer(EMBED_MODEL)

def embed(text: str):
    return model.encode([text])[0].tolist()
