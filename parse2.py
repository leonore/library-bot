# -*- coding: utf-8 -*-
from __future__ import division
import json
from math import ceil
import datetime

file = open('/home/ubuntu/leonore/library-bot/new_data.json', 'r')

parsed_data = json.load(file)
blocks = parsed_data["Groups"]

dict = {}

for element in blocks:
    dict[element["Label"]] = [element["Available"], element["Total"]]

available = parsed_data["Available"]
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

date = datetime.datetime.now()
today = date.weekday()
hour = date.hour

if (today == 5 or today == 6) and (hour > 16):
    ratio = int(ceil((available-dict["Reading room"][0]) / (total-dict["Reading room"][1]) * 100))
    rr_closed = True
else:
    ratio = int(ceil(available / total * 100))
    rr_closed = False

tweet = str(ratio) + "% available\n"

sorted_names = ["Level 1", "Level 3", "Level 4",
                "Level 5", "Level 6", "Level 7",
                "Level 8", "Level 10", "Reading room"]

for name in sorted_names:
    if name == "Reading room" and rr_closed:
        tweet += name + ": CLOSED\n"
    else:
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
