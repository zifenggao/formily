import json

def convert_to_json(linkage_relationship):
    json_data = json.dumps(linkage_relationship, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    return json_data