import PySimpleGUIQt as sg

layout = [
    [sg.Text("Nome:"), sg.Input(key="nome")],
    [sg.Text("Idade:"), sg.Input(key="idade")],
    [sg.Button("Enviar"), sg.Button("Cancelar")]
]

window = sg.Window("Cadastro", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Cancelar"):
        break
    if event == "Enviar":
        sg.popup(f"Nome: {values['nome']}\nIdade: {values['idade']}")

window.close()