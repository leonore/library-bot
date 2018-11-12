import json
from __future__ import division

file = open('new_data.json', 'r')

parsed_data = json.load(file)
blocks = parsed_data["Groups"]

dict = {}

for element in blocks:
    dict[element["Name"]]= [element["Available"],element["Total"]]

available = parsed_data["Available"]
total = parsed_data["Total"]

print(available, total)
tweet = str(available/total) + "% available\n"

print(tweet)
for level in sorted(dict.keys()):
    tweet += level + ": " + str(dict.get(level)[0]) + "/" + str(dict.get(level)[1]) + "\n"
