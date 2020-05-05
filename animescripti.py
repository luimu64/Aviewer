import re
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

    def watchinglink(self, link, ep):
        link = link.replace("category/", "")
        link = link + "-episode-" + ep
        source = rq.get(link).text
        self.adlink = "https:" + re.search(r'"//vidstreaming.io/streaming.php\?\S+"', source).group(0).replace('"', "")
        source = rq.get(self.adlink).text
        self.link = re.search(r"https://hls..xx.cdnfile.info.*,", source).group(0).split("'")
        self.link = self.link[0]


#from animescripti import anime

#x = anime()
#x.search("jojo")
#x.getepisodes("https://www18.gogoanime.io/category/jojo-no-kimyou-na-bouken-part-3-stardust-crusaders-2nd-season-dub")
#x.watchinglink(x.results[0][1], "4")
#print(x.results)
#print(x.episodes)
#print(x.link)
#print(x.adlink)
