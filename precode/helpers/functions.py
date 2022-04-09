import json

def read_json(name: str) -> dict:
    with open(name, "r", encoding='utf-8') as file:
        return json.load(file)
