from fastapi import FastAPI, Request
from pydantic import BaseModel
from ml import query_index, generate_answer, classify
from storage import init_index, process_all_files
from typing import List
from fastapi.responses import StreamingResponse
import asyncio
import json

api = FastAPI()

index = init_index()


class ChunkMetadata(BaseModel):
    text: str
    source: str
    category: str
    entities: List[str]


class QueryResponse(BaseModel):
    answer: str
    chunks: List[ChunkMetadata]


class QueryRequest(BaseModel):
        question: str


async def generate_stream(context: str, question: str):
    for token in generate_answer(context, question):
        yield token
        await asyncio.sleep(0.01)


async def generate_stream_with_chunks(context_chunks, context_text, question):
    chunks_json = json.dumps(context_chunks, ensure_ascii=False)
    yield f"{chunks_json}\n\n---\n\n"

    async for token in generate_stream(context_text, question):
        yield token
        await asyncio.sleep(0)


@api.post("/rag", response_model=QueryResponse)
def rag_endpoint(request: QueryRequest):
    category = classify(request.question)
    context_chunks = query_index(index, request.question, category)
    context_text = "\n\n".join([chunk["text"] for chunk in context_chunks])
    answer = generate_answer(context_text, request.question)
    return QueryResponse(answer=answer, chunks=context_chunks)

'''
@api.post("/rag-stream")
async def rag_stream_endpoint(request: QueryRequest):
    category = classify(request.question)
    context_chunks = query_index(index, request.question, category)
    context_text = "\n\n".join([chunk["text"] for chunk in context_chunks])
    return StreamingResponse(
        generate_stream_with_chunks(context_chunks, context_text, request.question),
        media_type="text/plain"
    )
'''





