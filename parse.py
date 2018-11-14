# -*- coding: utf-8 -*-
from __future__ import division
import json
from math import ceil

file = open('new_data.json', 'r')

parsed_data = json.load(file)
blocks = parsed_data["Groups"]

dict = {}

for element in blocks:
    dict[element["Label"]] = [element["Available"]+element["Offline"], element["Total"]]

available = parsed_data["Available"] + parsed_data["Offline"]
total = parsed_data["Total"]

# Final tweet format
# % available
# Level 1:
# Level 3:
# Level 4:
# Level 5:
# Level 6:
# Level 7:
# Level 8:
# Level 10:
# Reading Room:

ratio = int(ceil(available / total * 100))

tweet = str(ratio) + "% available\n"

sorted_names = ["Level 1", "Level 3", "Level 4",
                "Level 5", "Level 6", "Level 7",
                "Level 8", "Level 10", "Reading room"]

for name in sorted_names:
    av = dict.get(name)[0]
    tot = dict.get(name)[1]
    if av > (tot/2): # 50% available
        emoji = "✅"
    elif av > (tot/4): # 25% available
        emoji = "🔸"
    else: # less than 25% available
        emoji = "❗"
    tweet += name + ": " + str(av) + "/" + str(tot)+ " " + emoji  + "\n"
    #tweet += emoji + "  " + name + ": " + str(av) + "/" + str(tot) + "\n"

tweet = tweet.rstrip()
print(tweet)
