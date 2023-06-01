print("hello world!")
print("goodbye world!")
print("let me push")

import requests

def trace(*args):
  print (*args)
  pass

barcode = input("Give me barcode:")
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

product = data["product"]
print (product["allergens_hierarchy"])
print(f"Always check the allergen information before consuming a new product for your wellbeing.")
print(f"Here are allergens: {data['allergens_hierarchy']}")

#602652207020