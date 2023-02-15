import json

x = {
  "name": "Amal",
  "age": 22,
  "city": "Blr"
}


print(json.dumps(x))
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))
