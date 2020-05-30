import re
import requests as rq
from bs4 import BeautifulSoup as bs


class anime:
    class helpers:
        def hasNumbers(self, inputString):
            return any(char.isdigit() for char in inputString)
    def __init__(self):
        pass

    def getepisodes(self, link):
        source = rq.get(link).text
        soup = bs(source, "lxml")
        eps = soup.find("ul", id="episode_page")
        listofeps = []
        del listofeps[:]
        for i in eps.descendants:
            if i == "\n":
                pass
            else:
                listofeps.append(i.string)
        self.episodes = listofeps[-1].split("-")[1]

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

    def watchinglink(self, link, ep):
        link = link.replace("category/", "")
        link = link + "-episode-" + ep
        source = rq.get(link).text
        self.adlink = "https:" + re.search(r'"//vidstreaming.io/streaming.php\?\S+"', source).group(0).replace('"', "")
        source = rq.get(self.adlink).text
        links = re.findall(r"sources:\[{file:\s\S+", source)
        self.cleanlinks = []
        for i in links:
            link = i.split("'")
            self.cleanlinks.append(link[1])



#from animescripti import anime

#x = anime()
#x.search("jojo")
#x.getepisodes(x.results[0][1])
#x.watchinglink(x.results[0][1], "1")
#print(x.results)
#print(x.episodes)
#print(x.cleanlinks)
#print(x.adlink)