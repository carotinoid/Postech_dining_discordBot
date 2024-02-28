# get menu of Jigok_haksik dining from postech website

import requests
from bs4 import BeautifulSoup

# get response
res = requests.get("https://dining.postech.ac.kr/")
soup = BeautifulSoup(res.text, 'html.parser')

cards = soup.select('.card-content') # 0 조식 1 중식 2 석식

def get_meal(idx):
    regular_meal = cards[idx].select("div.card-content div.content")[0]
    meal_list = str(regular_meal).strip("<div class=\"content\">").strip("</div>").split("<br/><br/>")
    if idx == 0:
        _bread_meal = cards[idx].select("div.card-content div.content")[1]
        meal_list.append("<span OR") #으악 ㅋㅋㅋㅋㅋ
        meal_list.append("<span"+str(_bread_meal).strip("<div class=\"content\">").strip("</div>")) # Super spaghetti

    meal_str_list = []
    for food in meal_list:
        food = food.split('<br/>')[0]
        if '<span' in food:
            food = food.strip()
            food = food.strip("<span style=\"color: \#008000;\">")
            food = food.strip("</span>")
        else:
            food = food.strip()
            if food != '':
                assert(isinstance(food,str))# assert: for debug purpose, if something is false, panic. breakfast is strange output
                food += ' *' # * -> meat
        food = food.strip()
        if food != '':
            meal_str_list.append(food)

    return meal_str_list

def save_cache():
    for i in [0,1,2]:
        with open("meal_cache_"+str(i), "w", encoding='utf8') as f:
            f.write("\n")
            f.write("------------------------------------\n")
            f.write("**["+["아침","점심","저녁"][i]+"]**\n")
            for meal in get_meal(i):
                f.write("- " + meal + "\n")
            f.write("------------------------------------")

if __name__ == "__main__":
    save_cache()

# go to send.py