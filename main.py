import PySimpleGUI as sg
import pyshorteners

def janela_inicio():
    sg.theme('DarkAmber')

    layout = [
        [sg.Text('Bem vindo ao encurtador de links °3°')],
        [sg.Text('Cole sua url no espaço abaixo para ser encurtada pelo nosso programa')],
        [sg.Input(key='url')],
        [sg.Button('Encurtar', key='short_url')]
    ]

    janela = sg.Window('Janela de inico', layout)

    while True:

        event, value = janela.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'short_url':
            url = value['url']
            encurtador(url)
            break

def encurtador(url):
    link = pyshorteners.Shortener()
    url_curta = link.tinyurl.short(url)
    resultado(url_curta)

def resultado(url_curta):
    layout = [
        [sg.Text('Sua url foi encurtada com sucesso UwU')],
        [sg.Input(url_curta)],
        [sg.Button('Sair', key='close')]
    ]

    janela_resultado = sg.Window('Resultado', layout)

    while True:

        event, alue = janela_resultado.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'close':
            sg.popup('Obrigado por me usar ( ͡° ͜ʖ ͡°)')
            break

def main():
    janela_inicio()

if __name__ == '__main__':
    main()