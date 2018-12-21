# -*- coding: utf-8 -*-
from __future__ import division
from math import ceil
import datetime
import json

file = open('/home/ubuntu/leonore/library-bot/new_data.json', 'r')
#file = open('new_data.json', 'r')

parsed_data = json.load(file)
blocks = parsed_data["Groups"]

dict = {}

date = datetime.datetime.now()
today = date.weekday()
hour = date.hour
day = date.day
month = date.month

closed = [[24, 12], [25, 12], [26, 12],
	  [31, 12], [1, 1], [2, 1]]

if [day, month] in closed:
    shut = True

for element in blocks:
    dict[element["Label"]] = [element["Available"]+element["Offline"], element["Total"]]


total = parsed_data["Total"]
available = 0

if hour >= 12 and hour <=17:
    for level in dict:
        dict.get(level)[1] /= 3
        available += round(dict.get(level)[0] + dict.get(level)[1])
else:
    available = parsed_data["Available"] + parsed_data["Offline"]


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

if (today == 5 or today == 6) and (hour > 16):
    ratio = round((available-dict["Reading room"][0]) / (total-dict["Reading room"][1]) * 100)
    rr_closed = True
else:
    ratio = round(available / total * 100)
    rr_closed = False

tweet = str(int(ratio)) + "% available\n"

sorted_names = ["Level 1", "Level 3", "Level 4",
                "Level 5", "Level 6", "Level 7",
                "Level 8", "Level 10", "Reading room"]

for name in sorted_names:
    if name == "Reading room" and rr_closed:
        tweet += name + ": CLOSED\n"
    else:
        av = int(round(dict.get(name)[0]))
        tot = int(round(dict.get(name)[1]))
        if av > (tot/2): # 50% available
            emoji = "✅"
        elif av > (tot/4): # 25% available
            emoji = "🔸"
        else: # less than 25% available
            emoji = "❗"
        tweet += name + ": " + str(av) + "/" + str(tot)+ " " + emoji  + "\n"
    #tweet += emoji + "  " + name + ": " + str(av) + "/" + str(tot) + "\n"

if not shut:
    tweet = tweet.rstrip()
else:
    d = date.strftime("%B %d)
    tweet = "The library is closed today on %s. Happy holidays!" % d 
print(tweet)
