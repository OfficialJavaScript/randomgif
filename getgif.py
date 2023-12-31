#!/usr/bin/env python3

import requests

def getimage():
    with open('apikey.txt') as f:
        api_key = f.readlines()
        if not api_key:
            return "nokey"
        else:
            api_key = api_key[0]
    if api_key == "REPLACE ALL THIS TEXT WITH YOUR API KEY\n":
        return "nokey"
    elif "\n" in api_key:
        return "nokey"
    url = "https://api.giphy.com/v1/gifs/random"
    params = {'api_key': api_key, 'rating': 'g'}

    response = requests.get(url, params=params)
    if response.status_code == 401:
        return ("nokey")
    response = response.json()
    response = response["data"]["images"]["original"]["url"]
    return response

if __name__ == "__main__":
   print("Don't run this! Run main.py")
