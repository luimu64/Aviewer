from subprocess import run
import PySimpleGUI as sg
import _thread
from animescript import anime

x = anime()
sg.theme('DarkGrey7')

def refresh():
    number = values["shownum"].replace(".", "")
    if anime.helpers.hasNumbers(x, number):
        number = int(number) - 1
        if hasattr(x, "results") == False:
            print("You have to search before you can get episodes.\n")
        elif number > len(x.results)-1:
            print("Your number is too big.\n")
        else:
            x.getepisodes(x.results[number][1])
            print("Show has " + x.episodes + " episodes.\n")
    else:
        print("Give a number.\n")
    
def search():
    if values["search"] != "" and values["search"] != "Search something":
        x.search(values["search"])
        j = 1
        print("Search resulted:")
        for i in x.results:
            print(str(j) + ". " + i[0])
            j += 1
        print("\n")
    else:
        print("You need to give something to search!")

def play():
    if hasattr(x, "results") == False:
            print("You have to search before you can get episodes.\n")
    elif values["shownum"] != "Show's number":
        x.watchinglink(x.results[int(values["shownum"]) - 1][1], values["epnum"])
        print(x.adlink)
        if x.cleanlinks:
            print(x.cleanlinks)
            mainw.refresh()
            run ([
                "mpv",
                x.cleanlinks[0]
            ],)
        else:
            print("Sorry, I couldn't find the source links :(")
    else:
        print("Please fill the previous fields.")



layout = [  [sg.InputText("Search something", key="search"), sg.Button('search'), sg.InputText("Show's number", size=(15, 0), key="shownum"), sg.Button('refresh'), sg.InputText('Episode number', size=(16, 0), key="epnum"), sg.Button('play and get links')],
            [sg.Output(size=(115,20), key="output")]]

mainw = sg.Window('Aviewer', layout, use_default_focus=False, finalize=True)

mainw["search"].bind("<FocusIn>", "in")
mainw["search"].bind("<FocusOut>", "out")
mainw["shownum"].bind("<FocusIn>", "in")
mainw["shownum"].bind("<FocusOut>", "out")
mainw["epnum"].bind("<FocusIn>", "in")
mainw["epnum"].bind("<FocusOut>", "out")

while True:
    event, values = mainw.read()
    if event in (None, 'Cancel'):
        break

    if event in (None, 'play and get links'):
        _thread.start_new_thread(play, ())

    if event in (None, 'refresh'):
        _thread.start_new_thread(refresh, ())

    if event in (None, 'search0'):
        _thread.start_new_thread(search, ())

    #bindigs for focusing entry fields
    if event in (None, "searchin"):
        if values["search"] == "Search something":
            mainw["search"].update("")
    elif event in (None, "searchout"):
        if values["search"] == "":
            mainw["search"].update("Search something")
    elif event in (None, "shownumin"):
        if values["shownum"] == "Show's number":
            mainw["shownum"].update("")
    elif event in (None, "shownumout"):
        if values["shownum"] == "":
            mainw["shownum"].update("Show's number")
    elif event in (None, "epnumin"):
        if values["epnum"] == "Episode number":
            mainw["epnum"].update("")
    elif event in (None, "epnumout"):
        if values["epnum"] == "":
            mainw["epnum"].update("Episode number")

mainw.close()
