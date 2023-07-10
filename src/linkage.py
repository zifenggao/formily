class Linkage:
    def __init__(self, active_field, passive_field, relationship_type):
        self.active_field = active_field
        self.passive_field = passive_field
        self.relationship_type = relationship_type

    def get_active_field(self):
        return self.active_field

    def get_passive_field(self):
        return self.passive_field

    def get_relationship_type(self):
        return self.relationship_type

    def set_active_field(self, active_field):
        self.active_field = active_field

    def set_passive_field(self, passive_field):
        self.passive_field = passive_field

    def set_relationship_type(self, relationship_type):
        self.relationship_type = relationship_type

    def to_dict(self):
        return {
            'active_field': self.active_field,
            'passive_field': self.passive_field,
            'relationship_type': self.relationship_type
        }