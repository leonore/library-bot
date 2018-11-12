import json
import datetime

file = open('new_data.json', 'r')

parsed_data = json.load(file)
blocks = parsed_data["Groups"]

dict = {}

for element in blocks:
    dict[element["Name"]]= [element["Available"],element["Total"]]

available = str(parsed_data["Available"])
total = str(parsed_data["Total"])

now = datetime.datetime.now()

tweet = now.strftime("%d/%m/%y %H:%M") + " - " + available +"/"+total + " available\n"

for level in sorted(dict.keys()):
    tweet += level + ": " + str(dict.get(level)[0]) + "/" + str(dict.get(level)[1]) + "\n"
