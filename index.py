from clothing import Coat
from departments import Women

# Create my instances
womens_parka = Coat(
    "Women's Parka Jacket", "gray", 70.00, Women()
)  # invoke the women class & set equal to my department attribute


print(womens_parka)  # Print the string method for Coat
print(womens_parka.sizes())  # Print the sizes for the Coat
