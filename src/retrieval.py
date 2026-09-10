import json
import heapq
from cosine_similarity import get_similarity_scores, load_data


test_string_retrieval = "What should i do, if i am new to the topic?"
k = 4


def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def retrieve(query, embeddings, k):

    scores = get_similarity_scores(query, embeddings)
    top_chunks_indices = heapq.nlargest(k, range(len(scores)), key=scores.__getitem__)

    chunk_data = load_data("chunksj.json")
    retrieved_texts = []
    for i in range(k):
        print(chunk_data[top_chunks_indices[i]])
        retrieved_texts.append(chunk_data[top_chunks_indices[i]]["chunk"])
    return retrieved_texts