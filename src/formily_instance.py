from field import Field

class FormilyInstance:
    def __init__(self):
        self.field_list = []

    def add_field(self, field_name, field_value):
        new_field = Field(field_name, field_value)
        self.field_list.append(new_field)

    def remove_field(self, field_name):
        self.field_list = [field for field in self.field_list if field.name != field_name]

    def get_field(self, field_name):
        for field in self.field_list:
            if field.name == field_name:
                return field
        return None

    def get_all_fields(self):
        return self.field_list

    def get_linkage_relationship(self, field_name):
        field = self.get_field(field_name)
        if field:
            return field.linkage_list
        return None