from pinecone import Pinecone, ServerlessSpec, CloudProvider, AwsRegion
from config.settings import PINECONE_KEY, INDEX_NAME
import os
from ingestions import parse_file
from .preparation import prepare_chunks_for_indexing, split_texts

pc = Pinecone(api_key=PINECONE_KEY)


def init_index(dimension=1024):
    if INDEX_NAME not in [idx["name"] for idx in pc.list_indexes()]:
        pc.create_index(
            name=INDEX_NAME,
            dimension=dimension,
            metric="cosine",
            spec=ServerlessSpec(
                cloud=CloudProvider.AWS,
                region=AwsRegion.US_EAST_1
            )
        )
    return pc.Index(INDEX_NAME)


def upsert_vectors(index, namespace, vectors):
    index.upsert(vectors=vectors, namespace=namespace)


def process_all_files(data_dir, index):
    for filename in os.listdir(data_dir):
        path = os.path.join(data_dir, filename)

        if filename.startswith(".") or not os.path.isfile(path):
            continue

        try:
            print(f"\n Processing file: {filename}")
            texts = parse_file(path)
            chunks = split_texts(texts)
            vectors = prepare_chunks_for_indexing(chunks, index)
            namespace = 'customer_support'
            upsert_vectors(index, namespace, vectors)
            print(f"Uploaded {len(vectors)} new vectors from {filename}")
        except Exception as e:
            print(f"Error while processing {filename}: {e}")
