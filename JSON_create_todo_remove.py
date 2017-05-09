#JSON help program, used for initial creation of json files
import json

test = {"TILE_SIZE":40,"MAX_TERRAIN_SIZE":[15,15]}

print (json.dumps(test))

with open("output_json.txt","w") as file:
    json.dump(test,file,indent=1)

#Use json.load(file) to load
