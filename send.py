import os
import time
import request
import requests
import datetime

# feature control
webhook_postech = "webhook"
feature_postech = os.path.isfile(webhook_postech)
idx_postech = [0,1,2]

webhook_kaist = "webhook2"
feature_kaist = os.path.isfile(webhook_kaist)
idx_kaist = [3,4,5]

def send_discord(idx):
    # determine the request type
    if idx in idx_postech and feature_postech:
        webhook_path = webhook_postech
    elif idx in idx_kaist and feature_kaist:
        webhook_path = webhook_kaist
    else:
        print("Error: feature is not enabled.")
        return
    
    # check if cache exists
    cache_path = "meal_cache_"+str(idx)
    
    last_cache_datetime = datetime.datetime.strptime(time.ctime(os.path.getmtime(cache_path)),"%a %b %d %H:%M:%S %Y")
    today_datetime = datetime.datetime.today()
    today_datetime = today_datetime.replace(hour=0,minute=0,second=0,microsecond=0)

    # print(last_cache_datetime, today_datetime)
    if last_cache_datetime < today_datetime:
        print("saving cache")
        request.save_cache()
    
    with open(webhook_path, "r") as f:
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

    # POSTECH
    send_discord(idx)
    # KAIST
    send_discord(idx+3)
