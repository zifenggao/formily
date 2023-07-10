class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.linkage_list = []

    def add_linkage(self, linkage):
        self.linkage_list.append(linkage)

    def remove_linkage(self, linkage):
        self.linkage_list.remove(linkage)

    def get_linkages(self):
        return self.linkage_list

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
        for linkage in self.linkage_list:
            if linkage.active_field == self:
                linkage.passive_field.set_value(value)