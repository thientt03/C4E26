from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
from input_place import place 
import json

url="https://wind.waqi.info/nsearch/full/{place}?n=4"

conn = urlopen(url)

raw_data = conn.read()

content = raw_data.decode("utf8")

# f = open("air.html", "wb")
# f.write(raw_data)
# f.close()

soup = BeautifulSoup(content, "html.parser")
air_div = soup.find("div", "leaflet-pane leaflet-marker-pane")

p=json.loads(content)
l=p["results"]

for i in l:
    if i["s"]["t"] is not None:
        
        print("location:",i["s"]["n"][0])
        print("time:",i["s"]["t"][0])
        print("AQI:",i["s"]["a"])
        print("*"*30)
# print(air_div)
# news_list = []
# for div in div_list:
#     img = img.div
#     src = img["src"]
#     news = OrderedDict({
#         "so": src,
#     })
#     news_list.append(news)
# print(news_list)


