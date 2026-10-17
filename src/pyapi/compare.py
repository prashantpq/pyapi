import json

with open("data.json") as f:
    data = json.load(f)

if __name__ == "__main__":
    print(data)
