class Cold_Weather:
    def __init__(self):
        self.temperature_range = "30°F to 50°F"
        self.months = ["December", "January", "February"]
        self.cold_weather_items = set()  # List to add clothing items for Cold Weather

    def __str__(self):
        cold_string = f"It is usually worn in the winter in {self.temperature_range} weather and is sold during the months: \n"
        for month in self.months:
            cold_string += f"\t* {month}\n"
        return cold_string

    def add_cold_item(self, item):  # How I add the items to the list
        self.cold_weather_items.append(item)
        print(f"{item} is sold during {self.months}")
