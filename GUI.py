from subprocess import run
import PySimpleGUI as sg
import _thread
from animescript import anime

x = anime()


sg.theme('Dark')

layout = [  [sg.InputText('Search something...'), sg.Button('search'), sg.InputText('Ordinal...', size=(15, 0)), sg.Button('refresh'), sg.InputText('Episode number...', size=(16, 0)), sg.Button('play and get links')],
            [sg.Output(size=(115,20))]]

mainw = sg.Window('Aviewer', layout)

while True:
    event, values = mainw.read()
    if event in (None, 'Cancel'):
        break
    if event in (None, 'play and get links'):
        if hasattr(x, "results") == False:
                print("You have to search before you can get episodes.\n")
        else:
            x.watchinglink(x.results[int(values[1])][1], values[2])
            print(x.adlink)
            if x.cleanlinks:
                print(x.cleanlinks)
                mainw.refresh()
                _thread.start_new_thread(run, ([
                    "mpv",
                    x.cleanlinks[0]
                ],)
                )
            else:
                print("Sorry, I couldn't find the source links :(")
    if event in (None, 'refresh'):
        number = values[1].replace(".", "")
        if anime.helpers.hasNumbers(x, number):
            number = int(number)
            if hasattr(x, "results") == False:
                print("You have to search before you can get episodes.\n")
            elif number > len(x.results)-1:
                print("Your number is too big.\n")
            else:
                x.getepisodes(x.results[number][1])
                print("Show has " + x.episodes + " episodes\n")
        else:
            print("Give a number or ordinal.\n")

    if event in (None, 'search'):
        x.search(values[0])
        j = 0
        print("Search resulted:")
        for i in x.results:
            print(str(j) + ". " + i[0])
            j += 1
        print("\n")

mainw.close()
