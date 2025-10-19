from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_KEY = os.getenv("PINECONE_KEY")
HUGGINGFACE_KEY = os.getenv("HUGGINGFACE_KEY")
LLM_KEY = os.getenv("LLM_KEY")

INDEX_NAME = "smart_support"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100