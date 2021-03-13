import urllib.request as request
import json

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"

with request.urlopen(src) as response:
    data=json.load(response)

clist=data["result"]["results"]

with open("data.txt","w", encoding="utf-8") as file:
    with open("data.txt","w",encoding='utf-8') as file:
        for trip in clist:
            url="http://"+trip["file"].split("http://")[1]
            file.write(trip["stitle"]+" , "+trip["longitude"]+" , "+trip["latitude"]+" , "+url+"\n")