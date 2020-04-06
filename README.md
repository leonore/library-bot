# 🏛 UofG Library bot (discontinued)

## Example tweet

```
41% available
Level 1: 12/30 🔸
Level 3: 76/183 🔸
Level 4: 83/223 🔸
Level 5: 12/42 🔸
Level 6: 57/107 ✅
Level 7: 8/14 ✅
Level 8: 6/43 ❗
Level 10: 14/56 ❗
Reading room: 62/102 ✅
```

## Background
The UofG library bot was a project meant to help students easily know about busy times at the library. The University of Glasgow library regularly updates available/taken computers by making requests to their own API service. (For UofG students, this should be available [here](https://www.gla.ac.uk/sapp/PC/index.html)). This API _and_ information can only be accessed from within the University's network. As a third year student I had access to a virtual machine within that network, and I wanted to build a Twitter bot, so I thought I would attempt to condense this information in a useful way for students.

**I can no longer maintain this :(**

## Technologies

* Twitter API with tweepy
* crontab (https://crontab.guru is very useful)

The bot updated every day at different times, which was set with crontab. During more busy times of the year (exams) these times were different.
