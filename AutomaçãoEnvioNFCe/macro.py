import pyautogui
import keyboard
from time import sleep

verificador = 0

def on_press(event):
    global verificador
    if event.name == 'f7':
        verificador = 1
        print('Loop interrompido.')

keyboard.on_press(on_press)

sleep(3)

numeroNota = 0
#utilizar referência para achar as posições corretas (print deveria ser tirada toda vez antes de iniciar a execução do código)
localizacao = pyautogui.locateOnScreen('referencia.png')

while verificador == 0:
    #Tira print da tela utilizando localizacao
    referencia = pyautogui.screenshot(region=(localizacao))

    #Clica na primeira nota da lista (ajustar localização)
    pyautogui.click(685,265,duration=0.5)

    #Aperta seta para baixo para cada nota com rejeição
    pyautogui.press('down', presses=numeroNota)

    #Dá enter para enviar nota
    pyautogui.press('enter', presses=2)

    #Espera aparecer botão de ok 'ok.png'
    while not pyautogui.locateOnScreen('ok.png'):
        sleep(1)

    #Comparar tela com notificação de nota autorizada, se for normal segue o código, se não adiciona +1 a numeroNota
    if not pyautogui.locateOnScreen('autorizada.png'):
        numeroNota += 1

    #Enter para dar ok
    pyautogui.press('enter', presses=numeroNota)

    #Compara tela com print, se for igual adicionar +1 a numeroNota
    if(pyautogui.locateOnScreen(referencia)):
        numeroNota += 1

    #Descanso para usuário poder pausar o código
    sleep(0.5)