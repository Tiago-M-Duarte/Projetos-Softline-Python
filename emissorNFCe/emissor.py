# Algoritmo para emitir NFCe pelo PDV utilizando numerações de vendas colocadas no arquivo "emissor.txt"
import pyautogui
from time import sleep

sleep(3)
with open('emissor.txt', 'r') as arquivo:
    for venda in arquivo:
        pyautogui.write(venda)
        pyautogui.press(['enter'])
        pyautogui.press(['F10'])
        pyautogui.press(['enter'])
        #Espera aparecer botão de ok 'ok.png'
        while not pyautogui.locateOnScreen('ok.png'):
            sleep(0.5)
        pyautogui.press(['enter'])
            