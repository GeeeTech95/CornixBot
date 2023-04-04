from urllib import request
import requests
import time

while True :
    #sends an awake request every 30 seconds
    url = "https://www.cornixtradingbot.com"
    request.get(url)
    time.sleep(30)