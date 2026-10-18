import json
import sys

with open("data.json", "r") as f:
    data = json.load(f)


if __name__ == "__main__":
    
    # data["country"] = "usa"
    # del data["country"]

    with open("data.json", "w") as f:
        json.dump(data, f, indent = 4)

    print(data)
