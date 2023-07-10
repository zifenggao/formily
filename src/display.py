import json
from src.utils.json_converter import convert_to_json

def display_linkage_relationship(formily_instance):
    linkage_relationships = {}
    for field in formily_instance.field_list:
        linkage_relationships[field.name] = []
        for linkage in field.linkage_list:
            linkage_relationships[field.name].append({
                "active_field": linkage.active_field.name,
                "passive_field": linkage.passive_field.name,
                "relationship_type": linkage.relationship_type
            })
    return convert_to_json(linkage_relationships)