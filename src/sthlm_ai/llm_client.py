import json
import os

import httpx
from dotenv import load_dotenv

load_dotenv()  # reads the .env file

API_KEY = os.getenv("GROQ_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1"

def ask_structured(system: str, user: str) -> dict:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
      "model": "openai/gpt-oss-20b",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.2,
    }
    r = httpx.post(f"{BASE_URL}/chat/completions", headers=headers, json=payload, timeout=30)
    r.raise_for_status()
    content = r.json()["choices"][0]["message"]["content"]
    return json.loads(content)