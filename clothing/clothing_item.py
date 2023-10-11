# Parent Class
class Clothing_Item:
    def __init__(
        self, name, color, price, department
    ):  # attributes of all clothing items
        self.name = name
        self.color = color
        self.price = price
        self.department = (
            department  # maybe composition as I invoke the class in my instance
        )

    def __str__(self):
        return f"This {self.color} {self.name} costs ${self.price} and can be found in the {self.department.name}."

    def sizes(self):
        size_string = f"The {self.name} comes in the following sizes:\n"
        for size in self.department.sizes:
            size_string += f"\t* {size}\n"
        return size_string
