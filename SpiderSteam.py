import requests
from bs4 import BeautifulSoup
import re

index=0
def spider():
    while True:
        global index

        url = "https://store.steampowered.com/search/?filter=topsellers&specials=1&start="+str(index)+"&count=50"

        res=requests.get(url).text
        soup = BeautifulSoup(res, "html.parser")

        contents = soup.find(id="search_resultsRows").find_all('a')

        for content in contents:

            name = content.find(class_="title").string.strip()
            name=re.sub(","," ",name)
            sellers=content.find(class_="col search_discount responsive_secondrow").span.string.strip()
            oldPlace=content.find(class_="col search_price discounted responsive_secondrow").span.strike.string.strip()
            price = content.find(class_="col search_price discounted responsive_secondrow").text
            price=re.sub("\n","",price)
            price=re.sub("¥ \d+","",price,1)

            gameInfo = name + "," + \
                        sellers + "," + \
                        oldPlace + "," + \
                        price + "\n"
            print(gameInfo)
            forSave(gameInfo)
        index+=50

def forSave(gameInfo):
    file = open("优惠列表.csv", "a", encoding="utf-8-sig")
    file.write(gameInfo)

def creatFile():
    file = open("优惠列表.csv", "w", encoding="utf-8-sig")
    column_name = "游戏名,折扣,原价,现价\n"
    file.write(column_name)

if __name__ == '__main__':
    creatFile()
    spider()
