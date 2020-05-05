from animescripti import anime

x = anime()
x.search("railgun")
x.getepisodes("https://www18.gogoanime.io/category/jojo-no-kimyou-na-bouken-part-3-stardust-crusaders-2nd-season-dub")
x.watch(x.results[0][1], "4")
print(x.adlink)
print(x.results)
print(x.episodes)
print(x.link)
