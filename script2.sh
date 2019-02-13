#!/bin/bash

curl https://labstats.campus.gla.ac.uk/api/public/GetPublicApiData/1001 -o /home/ubuntu/leonore/library-bot/new_data.json
python3 /home/ubuntu/leonore/library-bot/parse2.py
python3 /home/ubuntu/leonore/library-bot/bot2.py
