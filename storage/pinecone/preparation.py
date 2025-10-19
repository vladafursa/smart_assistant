from langchain_text_splitters import RecursiveCharacterTextSplitter
from ml import extract_entities
import hashlib
from tqdm import tqdm
from ml import get_embeddings


def split_texts(text_records, chunk_size=500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    chunks = []
    for i, record in enumerate(text_records):
        text = record["text"]
        source = record["source"]
        for chunk_idx, chunk in enumerate(splitter.split_text(text)):
            entities_raw = extract_entities(chunk)
            chunks.append({
                "text": chunk,
                "metadata": {
                    "source_index": i,
                    "chunk_index": chunk_idx,
                    "source": source,
                    "entities": entities_raw
                }
            })
    return chunks


def hash_text(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def prepare_chunks_for_indexing(chunks, index):
    vectors = []

    chunk_ids = [hash_text(chunk["text"]) for chunk in chunks]
    existing = index.fetch(ids=chunk_ids)
    existing_ids = set(existing.vectors.keys())

    for chunk in tqdm(chunks):
        chunk_id = hash_text(chunk["text"])
        if chunk_id in existing_ids:
            continue

        emb = get_embeddings([chunk["text"]])[0]
        vectors.append({
            "id": chunk_id,
            "values": emb,
            "metadata": {**chunk["metadata"], "text": chunk["text"]}
        })

    return vectors




