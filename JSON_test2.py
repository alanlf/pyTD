#Program used to test JSON files
import json

with open("test_json.txt","r") as file:
    test = json.load(file)
    print(test)
