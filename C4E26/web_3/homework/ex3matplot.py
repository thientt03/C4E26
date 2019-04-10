import matplotlib.pyplot as plt 
from ex1connert import db
food_collection=db["customers"]
foodlist=food_collection.find()
ads = []
events = []
wom = []

for i in foodlist:
    if i["ref"]=="ads":
        ads.append(i["ref"])
    elif i["ref"]=="events":
        events.append(i["ref"])
    else:
        wom.append(i["ref"])

a=len(ads)
b=len(events)
c=len(wom)
s=a+b+c
# input data in circle
data = [a/s,b/s,c/s]
title = ["ads", "events", "wom"]
colors = ["red", "green", "blue"]

# draw circle 
plt.pie(data, labels=title, colors=colors, autopct='%1.1f%%', startangle=-90, pctdistance=0.9, labeldistance=1.2)
plt.axis("equal")
plt.show()