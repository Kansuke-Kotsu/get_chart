import csv
import numpy as np
import requests
import pandas as pd
import time
import datetime
import streamlit as st

def get_ticker():
    EP   = 'https://api.coin.z.com/public/v1/ticker?symbol=' + "BTC"
    res  = requests.get(EP)
    return res.json()

while True:
    try:
        # ビットコイン購入価格
        ask = get_ticker()["data"][0]["ask"]
        bid = get_ticker()["data"][0]["bid"]
        with open('btc.csv', 'a') as f:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerow([datetime.datetime.now(), ask, bid])
        time.sleep(5*60)

    except Exception as e:
        print(e)