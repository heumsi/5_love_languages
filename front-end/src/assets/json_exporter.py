import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in '%s': %s" % (cwd, files))


obj_list = []
with open("questions", "r") as f:
    for line in f:
        obj = {}
        obj['statement'] = line[:-3]
        obj['type'] = line[-2]
        obj_list.append(obj)

output_json = []
for i in range(0, len(obj_list), 2):
    output_json.append([obj_list[i], obj_list[i+1]])

#import pprint as pp
#pp.pprint(output_json)

import json
with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(output_json, f, indent="\t")