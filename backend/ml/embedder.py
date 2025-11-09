import requests
import os
from config import HUGGINGFACE_KEY

API_URL = "https://router.huggingface.co/hf-inference/models/intfloat/multilingual-e5-large/pipeline/feature-extraction"
headers = {
    "Authorization": f"Bearer {HUGGINGFACE_KEY}",
}


def get_embeddings(texts):
    if isinstance(texts, str):
        texts = [texts]

    payload = {"inputs": texts}
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        print("Response text:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError:
        print("Failed to decode JSON. Raw response:")
        print(response.text)

print(get_embeddings("hello"))