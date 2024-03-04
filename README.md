# Postech_dining_discordBot

## Intro

[postech icon here] [hak-sik icon here]
~~..So tired.. Please give me pull request for icons~~

Personal project for Hak-sik crawler and automatic sender.

Nobody can use this rather than POSTECHIAN. (maybe... KAISTian can use... But why?)

## Features
- automatic crawling hak-sik
- automatic discord message sending, containing information of today's haksik

## Requirements

This project requires `Python 3.*`, *requests*, *beautifulsoup4* for running.

## How to set

1. wget or Download & unzip on your server.
    - you can use `git clone https://github.com/carotinoid/Postech_dining_discordBot.git`


2. Create the file named `webhook`, and paste the webhook token(URL) of your own discord server. Then this program send message to your own discord server.

3. Use schedule program such as `crontab` on server for sending automatically.
    - Running `request.py` gathers information from Postech Dining site and save to the cache file.
    - Running `send.py` updates the cache and sends the message to the discord server. Cache file has to exist initially.

## Contribution
This project is open to contribution, you are welcome to make a pull request :)

## Special Thanks
Thanks,
- [JJT](https://github.com/Powering111) (he is god!)
- [Quasar-Kim](https://github.com/Quasar-Kim)

---

Support me: [!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/carotinoid)

Thankyou.
