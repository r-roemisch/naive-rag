import json
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed_text(data, model) -> list:
    vector_list = []
    for chunk in data:
        vector_list.append(model.encode(chunk["chunk"]).tolist())
    return vector_list

def save_embeddings():
    with open("chunksj.json", "r", encoding="utf-8") as f:
        chunk_data = json.load(f)

    vector_list = embed_text(chunk_data, model)

    with open("vectors.json", "w") as data:
        json.dump(vector_list, data, indent=2)

save_embeddings()