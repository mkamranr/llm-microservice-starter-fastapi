# 🧠 LLM Microservices Boilerplate

This is a modular microservice-style boilerplate built with **FastAPI** for running LLM-powered services like summarization, translation, and embedding generation.

## 🧰 Features
- Summarize text using OpenAI GPT
- Translate text to multiple languages
- Generate sentence embeddings using Sentence Transformers
- Expose all services via REST APIs
- Docker-ready for scalable deployment

## 📦 Services
| Endpoint       | Description               |
|----------------|---------------------------|
| `/summarize`   | Summarizes input text     |
| `/translate`   | Translates to given lang  |
| `/embed`       | Returns vector embedding  |

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/yourname/llm-microservice-boilerplate.git
cd llm-microservice-boilerplate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add OpenAI key
Edit app/config.py:
```python
OPENAI_API_KEY = "your-openai-key"
```

### 4. Run the server
```bash
uvicorn app.main:app --reload
```

### 🐳 Docker
```bash
docker build -t llm-service .
docker run -p 8000:8000 llm-service
```
