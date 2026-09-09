import json


def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        pdfs = json.load(f)
    return pdfs

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

def chunking_all(data_list):
    chunk_size = 30
    overlap = 5
    chunk_id = 0
    chunk_list = []
    for pdf in data_list:
        for page in pdf:
            chunks = chunking(page["text"], chunk_size, overlap)
            for text_chunk in chunks:
                chunk_id += 1
                chunk = {
                    "chunk_id": chunk_id,
                    "title": page["title"],
                    "page": page["page"],
                    "chunk": text_chunk
                }
                chunk_list.append(chunk)
    return chunk_list

def save_as_json(dir_path):
    with open("chunksj.json", "w") as data:
        json.dump(chunking_all(load_data("dataj.json")), data, indent=2)

save_as_json("data")       
