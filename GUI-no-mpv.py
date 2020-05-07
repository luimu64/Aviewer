import PySimpleGUI as sg

from animescript import anime



x = anime()


sg.theme('DarkRed')

layout = [  [sg.InputText('Search something...'), sg.Button('🔍'), sg.InputText('Ordinal...', size=(15, 0)), sg.Button('⇅'), sg.InputText('Episode number...', size=(16, 0)), sg.Button('ᐅ')],
            [sg.Output(size=(98,20))]]

mainw = sg.Window('Aviewer', layout)

while True:
    event, values = mainw.read()
    if event in (None, 'Cancel'):
        break
    if event in (None, 'ᐅ'):
        if hasattr(x, "results") == False:
                print("You have to search before you can get episodes.\n")
        else:
            x.watchinglink(x.results[int(values[1])][1], values[2])
            print(x.link)
            print(x.adlink)
    if event in (None, '⇅'):
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

    if event in (None, '🔍'):
        x.search(values[0])
        j = 0
        print("Search resulted:")
        for i in x.results:
            print(str(j) + ". " + i[0])
            j += 1
        print("\n")

mainw.close()
