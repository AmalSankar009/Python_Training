import json

x = '{ "name":"Amal", "age":22, "city":"Blr"}'
y = json.loads(x)

print(y)
print(y["age"])