class Women:
    def __init__(self):
        self.name = "Women's Department"
        self.sizes = [
            "Women's S",
            "Women's M",
            "Women's L",
            "Women's XL",
            "Women's XXL",
        ]

    def __str__(self):
        print(
            f"{self} can be found in the Women's Department in these sizes: \n{self.size}"
        )
