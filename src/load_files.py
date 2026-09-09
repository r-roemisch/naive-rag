import os
import json
from pathlib import Path
from pypdf import PdfReader



def get_page_data(filepath):
    reader = PdfReader(filepath)
    dataset = []
    for i in range(len(reader.pages)):
        entry = {}
        entry["title"] = os.path.basename(filepath)
        entry["page"] = i + 1
        entry["text"] = reader.pages[i].extract_text()
        dataset.append(entry)
    return dataset


def get_data(dir_path):
    files = os.listdir(dir_path)
    database = []
    for file in files:
        database.append(get_page_data("data/" + file))
    return database

def save_as_json(dir_path):
    with open("dataj.json", "w") as data:
        json.dump(get_data(dir_path), data, indent=2)

save_as_json("data")