# Algoritmo para fazer o re-envio de notas fiscais no PDV
import pyautogui
import keyboard
from time import sleep
import logging

logging.basicConfig(level=logging.INFO, filename='macro.log', format='%(asctime)s - %(levelname)s - %(message)s')

pyautogui.FAILSAFE = False

verificador = 0

print('Aperte F7 para parar o programa')
def on_press(event):
    global verificador
    if event.name == 'f7':
        verificador = 1
        logging.info(f'notas com erro: {numeroNota}')
        logging.info(f'Loop interrompido com {notasEnviadas} notas enviadas')

keyboard.on_press(on_press)

sleep(3)

numeroNota = 0
notasEnviadas = 0

while verificador == 0:
    # Encontrar a posição de referência na tela
    # (print deve ser tirada toda vez antes de iniciar a execução do código)
    localizacao = pyautogui.locateOnScreen('imagens/referencia.png', confidence=0.8)
    if localizacao:
        logging.info('Referencia encontrada, inciando loop')
        print('Referencia encontrada, inciando loop')
        break
    print('Referencia nao encontrada')
    sleep(1)

while verificador == 0:
    #Tira print da tela utilizando localizacao
    referencia = pyautogui.screenshot(region=(localizacao))

    #Clica na primeira nota da lista (ajustar localização)
    pyautogui.click(685,265,duration=0.5)

    #Aperta seta para baixo para cada nota com rejeição
    pyautogui.press('down', presses=numeroNota)

    #Dá enter para enviar nota
    pyautogui.press('enter', presses=3, interval=0.5)

    #Espera aparecer botão de ok 'ok.png'
    while not pyautogui.locateOnScreen('imagens/ok.png'):
        sleep(0.5)

    #Comparar tela com notificação de nota autorizada, se for normal segue o código, se não adiciona +1 a notasEnviadas
    if pyautogui.locateOnScreen('imagens/autorizada.png'):
        notasEnviadas += 1

    #Enter para dar ok
    pyautogui.press('enter')
    sleep(2)
    #Compara tela com print, se for igual adicionar +1 a numeroNota
    if(pyautogui.locateOnScreen(referencia, confidence=0.9)):
        numeroNota += 1
    print('notas com erro:', numeroNota)