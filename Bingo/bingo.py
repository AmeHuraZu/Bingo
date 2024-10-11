import random
import PySimpleGUI as sg

def function():
    num = random.randrange(1,75)
    sg.popup(num)
    print(num)

def GUI():
    layout = [
        [sg.Text('ビンゴ!')],
        [sg.Text('抽選1'), sg.Button('抽選')]
    ]

    window = sg.Window('ビンゴゲーム', layout)

    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '抽選':
            function()

    window.close()

if __name__ == '__main__':
    GUI()