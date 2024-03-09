# get menu of Jigok_haksik dining from postech website

import requests
from bs4 import BeautifulSoup

def get_meal(idx):
    idx_postech = [0,1,2]
    idx_kaist = [3,4,5]
    if idx in idx_postech:
        return get_meal_postech(idx)
    elif idx in idx_kaist:
        return get_meal_kaist(idx)

def get_meal_postech(idx):
    # get response
    res = requests.get("https://dining.postech.ac.kr/")
    soup = BeautifulSoup(res.text, 'html.parser')

    cards = soup.select('.card-content') # 0 조식 1 중식 2 석식

    regular_meal = cards[idx].select("div.card-content div.content")[0]
    meal_list = str(regular_meal).strip("<div class=\"content\">").strip("</div>").split("<br/><br/>")
    if idx == 0:
        _bread_meal = cards[idx].select("div.card-content div.content")[1]
        meal_list.append("<span OR") #으악 ㅋㅋㅋㅋㅋ
        if '<span' in str(_bread_meal): 
            meal_list.append(str(_bread_meal).strip("<div class=\"content\">").strip("</div>")) # Super spaghetti
        else:
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

def get_meal_kaist(idx):
    # get response
    res = requests.get("https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=fclt")
    soup = BeautifulSoup(res.text, 'html.parser')
    
    cards = soup.select("#tab_item_1 td")
    
    def conv(x):
        x = x.replace("<td>","").replace("<ul class=\"list-1st\">","").strip().replace("\r","").replace("\t","").replace("\n","").replace("&amp;","&")
        b_index = x.rfind("(")
        if b_index!=-1:
            x = x[:b_index]
        c_index = x.find("-->")
        if c_index!=-1:
            x = x[c_index+3:]
        return x
    def filt(x):
        print("filtering",x)
        return not ("<" in x or len(x)==0 or x=="kcal" or x.isdigit())
    a = list(filter(filt, map(conv,str(cards[idx-3]).strip().split("<br/>"))))
    print(a)
    return a



def save_cache():
    for i in [0,1,2,3,4,5]:
        with open("meal_cache_"+str(i), "w", encoding='utf8') as f:
            f.write("\n")
            f.write("------------------------------------\n")
            f.write("**["+["아침","점심","저녁"][i%3]+"]**\n")
            for meal in get_meal(i):
                f.write("- " + meal + "\n")
            f.write("------------------------------------")

if __name__ == "__main__":
    save_cache()

# go to send.py