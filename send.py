import os
import time
import request
import requests
import datetime

def send_discord(idx):
    cache_path = "meal_cache_"+str(idx)

    # check if cache exists
    
    last_cache_datetime = datetime.datetime.strptime(time.ctime(os.path.getmtime(cache_path)),"%a %b %d %H:%M:%S %Y")
    today_datetime = datetime.datetime.today()
    today_datetime = today_datetime.replace(hour=0,minute=0,second=0,microsecond=0)

    # print(last_cache_datetime, today_datetime)
    if last_cache_datetime < today_datetime:
        print("saving cache")
        request.save_cache()
    
    with open("webhook", "r") as f:
        _webhook = f.readline()
    with open(cache_path, "r", encoding='utf8') as f:
        content = "> ".join(f.readlines())

        requests.post(_webhook,
        json={'content' : content}
        )

if __name__=="__main__":
    now = datetime.datetime.now()
    print("sending, ",now)

    if now.hour < 10:
        idx = 0
    elif now.hour < 16:
        idx = 1
    else:
        idx = 2

    send_discord(idx)
