import eel

from animescripti import anime

eel.init("web")
eel.start("main.html", cmdline_args=["--disable-web-security", "--user-data-dir='-'"])
x = anime()
@eel.expose
def search_py(kw):
    x.search(kw)
    return x.results
#@eel.expose
#def updatesearch():
 #   eel.gets()(search)
