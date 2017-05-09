#Program used to test JSON files #@todo remove
import json

test = {"Rat":{"HP":10},"Mouse":{"HP":5}}

print (json.dumps(test))

with open("test_json.txt","w") as file:
    json.dump(test,file,indent=1)

#Use json.load(file) to load
