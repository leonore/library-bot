#!/bin/bash

curl https://labstats.campus.gla.ac.uk/api/public/GetPublicApiData/1001 -o new_data.json
python bot.py
