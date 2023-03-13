import json

def read():
    try:
        with open('notes.json') as data:
            notes = json.loads(data.read())
        return notes
    except:
        return []


def save(notes):
    with open('notes.json', 'w') as data:
        json.dump(notes, data, indent=4)