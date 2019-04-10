from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "https://dantri.com.vn"
#1 dowload the page

#1.1 open connection
conn = urlopen(url)
#1.2 read data
raw_data = conn.read()

#1.3 decode data 
content = raw_data.decode("utf8")
# print(content)
# mở-ghi-đóng file tải về
f = open("dantri.html", "wb")
f.write(raw_data)
f.close()

#2 find ROi
soup = BeautifulSoup(content, "html.parser")
#find("tên thẻ", clas or các thứ cần miêu tả)
ul_news = soup.find("ul", "ul1 ulnew")
# print(ul_news)

#3 copy n save
li_list = ul_news.find_all("li")
news_list = []
for li in li_list:
    # walking
    h4 = li.h4
    a = h4.a
    link = a["href"]
    title = a.string
    # print(url+link)
    news = OrderedDict({
        "title": title,
        "link": link
    })
    news_list.append(news)
pyexcel.save_as(records = news_list, dest_file_name = "demo.xlsx")
