#Program used to test JSON files #@todo remove
import json

with open("output_json.txt","r") as file:
    test = json.load(file)
    print(test)
