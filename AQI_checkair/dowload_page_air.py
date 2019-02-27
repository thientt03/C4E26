from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict

url = "http://aqicn.org/"

conn = urlopen(url)

raw_data = conn.read()

content = raw_data.decode("utf8")

f = open("air.html", "wb")
f.write(raw_data)
f.close()

soup = BeautifulSoup(content, "html.parser")
air_div = soup.find("div", "leaflet-pane leaflet-marker-pane")

print(air_div)
# news_list = []
# for div in div_list:
#     img = img.div
#     src = img["src"]
#     news = OrderedDict({
#         "so": src,
#     })
#     news_list.append(news)
# print(news_list)


