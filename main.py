import re

import eel
import requests as rq
from bs4 import BeautifulSoup as bs


class anime:
    def __init__(self):
        pass

    def search(self, keyword):
        source = rq.get("https://www18.gogoanime.io//search.html?keyword=" + keyword).text
        soup = bs(source, "lxml")
        titles = soup.find_all("p", class_="name")
        self.results = []
        del self.results[:]
        for i in titles:
            title = i.a["title"]
            link = "https://www18.gogoanime.io" + i.a["href"]
            self.results.append((title, link))

    def getepisodes(self, link):
        source = rq.get(link).text
        soup = bs(source, "lxml")
        eps = soup.find("ul", id="episode_page")
        self.episodes = (eps.li.a["ep_start"], eps.li.a["ep_end"])

    

x = anime()
x.search("jojo")
x.getepisodes("https://www18.gogoanime.io/category/jojo-no-kimyou-na-bouken-part-3-stardust-crusaders-2nd-season-dub")
print(x.episodes)


#link = rq.get("https://www18.gogoanime.io/to-aru-kagaku-no-railgun-episode-15").text
#soup = bs(link, "lxml")
#streamlink = re.search(r'"//vidstreaming.io/streaming.php\?\S+"', link).group(0).replace('"', "")
#print("https:" + streamlink)
