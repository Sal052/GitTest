import requests

def trace(*args):
  print (*args)
  pass

#Barcode is used by webapi to find product information
barcode = input("Give me barcode:")

#Establishes webapi
URL = "https://world.openfoodfacts.org/api/v0/product/" + barcode + ".json"
print (URL)

trace ("Calling", URL)
response = requests.get(URL)
response.raise_for_status()
data = response.json()

#trace ("\nText returned:", response.text)

trace("\nHere are all the key/value paurs in the JSON response:")
for key, value in data.items():
  trace ("\n" + key)

print(f"Always check the allergen information before consuming a new product for your wellbeing.")

#Creates variable storing the product information
product = data["product"]

#Product information is scanned for allergen information and returns it
print (product["allergens_hierarchy"])


#602652207020