from src.formily_instance import FormilyInstance
from src.field import Field
from src.linkage import Linkage
from src.display import display_linkage_relationship

def main():
    formily_instance = FormilyInstance()

    # Add fields to the form
    field1 = Field("Field1")
    field2 = Field("Field2")
    field3 = Field("Field3")

    formily_instance.add_field(field1)
    formily_instance.add_field(field2)
    formily_instance.add_field(field3)

    # Create linkage relationships
    linkage1 = Linkage(field1, field2, "active")
    linkage2 = Linkage(field2, field3, "passive")

    field1.add_linkage(linkage1)
    field2.add_linkage(linkage2)

    # Display the linkage relationship in json format
    display_linkage_relationship(formily_instance)

if __name__ == "__main__":
    main()