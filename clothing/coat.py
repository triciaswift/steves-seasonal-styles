from .clothing_item import Clothing_Item
from seasons import Cold_Weather


class Coat(Clothing_Item, Cold_Weather):  # Multiple inheritance
    def __init__(self, name, color, price, department):
        Clothing_Item.__init__(self, name, color, price, department)  # Inheritance
        Cold_Weather.__init__(self)  # Mixin

    def __str__(self):  # Combination of two parent strings
        clothing_item_str = Clothing_Item.__str__(self)
        cold_weather_str = Cold_Weather.__str__(self)
        return f"{clothing_item_str}\n{cold_weather_str}"
