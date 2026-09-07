import os
from pathlib import Path
from pypdf import PdfReader


# load document in general
def load_document(filepath):
    return PdfReader(filepath)

# get page and text
def get_page_data(filepath):
    reader = PdfReader(filepath)
    dataset = []
    for i in range(len(reader.pages)):
        entry = {}
        entry["title"] = os.path.basename(filepath)
        entry["page"] = i
        entry["text"] = reader.pages[i].extract_text()
        dataset.append(entry)
    return dataset

print(get_page_data("data/How to Improve RAG Applications; 6 Proven Strategies - Jason Liu.pdf"))