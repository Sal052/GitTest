import requests

def trace(*args):
  print (*args)
  pass

#Barcode is used by webapi to find product information
barcode = input("Give me barcode:")

#Establishes webapi
URL = "https://world.openfoodfacts.org/api/v0/product/" + barcode + ".json"

#trace ("Calling", URL)
response = requests.get(URL)
response.raise_for_status()
data = response.json()

#trace ("\nText returned:", response.text)

print("\n" + f"Always check the allergen information before consuming a new product for your wellbeing.")

#Creates variable storing the product information
products = data["product"]["allergens_hierarchy"]

#Remove extra characters from list items
products = map(lambda item: item[3:], products)

#Product information is scanned for allergen information and returns it
for product in products:
  print(product + ", ")

#602652207020