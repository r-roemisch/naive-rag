import json


def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        pages = json.load(f)
    return pages

def chunking(text, chunk_size, overlap):
    words = text.split()
    chunks = []
    start = 0
    iterations = len(words) / chunk_size
    for iter in range(int(iterations)):
        chunk_words = words[start:start+chunk_size]
        chunk = " ".join(chunk_words)
        chunks.append(chunk)
        start = start + chunk_size - overlap
    return chunks

def chunking_all(data_list, chunk_size, overlap):
    chunks = []
    for pdf in data_list:
        for page in pdf:
            

        
