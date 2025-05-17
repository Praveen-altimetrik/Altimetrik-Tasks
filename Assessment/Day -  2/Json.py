import json

data = {
    "name":"Bob",
    "age":22,
    "subjects":["English","History"]
}

with open('data.json','w') as file:
    json.dump(data, file, indent=4)

with open('data.json','r') as file:
    data = json.load(file)
    print(data)
    print(f"Name: {data['name']}, Age: {data['age']}")