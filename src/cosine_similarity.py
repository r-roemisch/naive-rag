import numpy as np
from sentence_transformers import SentenceTransformer
import json
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        vectors = json.load(f)
    return vectors

def cosine_similarity(vector_A, vector_B):
    dot_product = np.dot(vector_A, vector_B)
    length_a = np.linalg.norm(vector_A)
    length_b = np.linalg.norm(vector_B)
    return dot_product / (length_a * length_b)

def get_similarity_scores(query, embeddings) -> list:
    query_embedding = model.encode(query)
    scores = []
    for i in range(len(embeddings)):
        embeddings_vec = np.array(embeddings[i])
        score = cosine_similarity(query_embedding, embeddings_vec)
        scores.append(score)

    return scores


    