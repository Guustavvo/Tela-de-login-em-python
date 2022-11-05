from ast import And, If
from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('reddit')
Layout = [
    [sg.Text('usuario'), sg.Input(key='usuario')],
    [sg.Text('senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('salvar o login')],
    [sg.Button('Entrar')]
]
# Janela
Janela = sg.Window('tela de login', Layout)
# Ler os eventos
while True:
    eventos, valores = Janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'joao victor' and valores['senha'] == '123456':
            print('bem-vindo')
        else:
            print('Nao foi possivel realizar o login')