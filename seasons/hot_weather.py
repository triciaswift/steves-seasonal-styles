class Hot_Weather:
    def __str__(self):
        def __init__(self):
            self.temperature_range = "70°F to 100°F"
            self.months = ["June", "July", "August"]
            self.cold_weather_items = set()

    def __str__(self):
        print(f"{self} and can be worn in {self.temperature_range} weather")

    def add_cold_item(self, item):
        self.cold_weather_items.append(item)
        print(f"{item} is sold during {self.months}")
