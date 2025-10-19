from config import HUGGINGFACE_KEY
import requests
import os

API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {HUGGINGFACE_KEY}",
    "Content-Type": "application/json"
}

def summarize_question(question):
    system_prompt = "You are a support assistant who briefly summarizes the essence of a question while preserving its key meaning. When rewriting, avoid first-person language — replace 'I' with 'the client' or a neutral third-person form. The result should be formal and concise."
    user_prompt = f"Summarize and rephrase the following question formally, avoiding first-person language:\n\n{question}"

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2:featherless-ai",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 128,
        "top_p": 0.9
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        print("Response text:", response.text)
    except (KeyError, IndexError):
        print("Unexpected response format:")
        print(response.text)


def extract_entities(question):
    system_prompt = (
        "You are a support assistant who extracts key entities from text. "
        "Entities include people, organizations, places, dates, technologies, and other important elements. "
        "Return only the raw entity names as a plain list. Do not include explanations, categories, types, or any text in parentheses."
    )

    user_prompt = f"Extract key entities from the following question:\n\n{question}\n\nFormat: plain list of entity names only. No parentheses, no descriptions, no types."

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2:featherless-ai",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 256
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        response.raise_for_status()
        raw = response.json()["choices"][0]["message"]["content"].strip()
        try:
            import json
            entities = json.loads(raw)
            if isinstance(entities, list):
                return [e.strip() for e in entities if isinstance(e, str)]
        except Exception:
            # fallback: strip bullets manually
            return [line.lstrip("-•* ").strip() for line in raw.split("\n") if line.strip()]
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        print("Response text:", response.text)
    except (KeyError, IndexError):
        print("Unexpected response format:")
        print(response.text)



