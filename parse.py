# -*- coding: utf-8 -*-
from __future__ import division
from math import ceil
import datetime
import json
from emojis import standard, valentines

#file = open('/home/ubuntu/leonore/library-bot/new_data.json', 'r')
file = open('new_data.json', 'r')

parsed_data = json.load(file)
blocks = parsed_data["Groups"]

dict = {}

date = datetime.datetime.now()
today = date.weekday()
hour = date.hour

# BUSY IS:
# february
# march till 15th
# april from 14th till may 17th TO IMPROVE
busy_months = [(2, 0), 3, 4, 5]
busy = False

if hour > 10 and hour < 18:
    if date.month is 2:
        busy = True
    elif date.month in [3, 5] and date.day < 17:
        busy = True
    elif date.month is 4 and date.day > 14:
        busy = True

if busy:
    for element in blocks:
        dict[element["Label"]] = [element["Available"], element["Total"]]

    available = parsed_data["Available"]
    total = parsed_data["Total"]
else:
    for element in blocks:
        dict[element["Label"]] = [element["Available"]+element["Offline"]*0.85, element["Total"]]

    total = parsed_data["Total"]
    available = parsed_data["Available"] + parsed_data["Offline"]*0.85

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

if date.day == 14 and date.month == 2:
    emojis = valentines
else:
    emojis = standard

for name in sorted_names:
    if name == "Reading room" and rr_closed:
        tweet += name + ": CLOSED\n"
    else:
        av = int(round(dict.get(name)[0]))
        tot = int(round(dict.get(name)[1]))
        if av > (tot/2): # 50% available
            emoji = emojis[0]
        elif av > (tot/4): # 25% available
            emoji = emojis[1]
        else: # less than 25% available
            emoji = emojis[2]
        tweet += name + ": " + str(av) + "/" + str(tot)+ " " + emoji  + "\n"
    #tweet += emoji + "  " + name + ": " + str(av) + "/" + str(tot) + "\n"

tweet = tweet.rstrip()
print(tweet)
