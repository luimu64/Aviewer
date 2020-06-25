import sys
from subprocess import run
from animescript import anime

x = anime()

if sys.argv[1] == "search":
    x.search(sys.argv[2])
    j = 1
    for i in x.results:
            print(i[0] + "\n" + i[1])
            j += 1

elif sys.argv[1] == "episodes":
    x.getepisodes(sys.argv[2])
    print(x.episodes)

elif sys.argv[1] == "play":
    x.watchinglink(sys.argv[2], sys.argv[3])
    print(x.adlink)
    if x.cleanlinks:
        print(x.cleanlinks)
        run ([
            "mpv",
            x.cleanlinks[0]
        ],)
    else:
        print("Sorry, I couldn't find the source links :(")