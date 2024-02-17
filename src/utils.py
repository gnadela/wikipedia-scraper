import json

def read_json(file):
    with open(file, 'r') as json_file:
        contents = json.load(json_file)
    return contents
    
def write_json(contents, json_file):
    with open(json_file, 'w') as file:
        json.dump(contents, file, indent=4)



