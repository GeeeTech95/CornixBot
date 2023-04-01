import requests
import time

print("starting ..")
while (True):
    requests.get("https://www.cornixtradingbot.com")
    time.sleep(10000)
    print("pinged ... ")
