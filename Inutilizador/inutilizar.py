# Algoritmo para inutilizar notas no PDV, 
# só é necessário apertar F7 ao finalizar inutilização de sequência 
# para ir para próxima.
# ATENÇÃO, VERIFICAR SE SERIE ESTÁ CORRETA ANTES DE DAR START
import pyautogui
import keyboard
from time import sleep

sleep(3)

with open('inutilizar.txt', 'r') as arquivo:
    for linha in arquivo:
        inicio = linha.split('-')[0]
        fim = linha.split('-')[1]
        pyautogui.click(552,391,duration=1)
        with pyautogui.hold('ctrl'):
            pyautogui.press(['a'])
        pyautogui.write(inicio)
        pyautogui.click(745,393,duration=1)
        with pyautogui.hold('ctrl'):
            pyautogui.press(['a'])
        pyautogui.write(fim)
        pyautogui.click(623,503,duration=1)
        pyautogui.click(9,64,duration=3)
        pyautogui.click(708,591,duration=4)
        pyautogui.write(inicio + '-' + fim)
        pyautogui.click(993,659,duration=0.5)
        pyautogui.click(1336,35,duration=2)
        while not pyautogui.locateOnScreen('ok.png'):
            sleep(0.5)
        #keyboard.wait('f12')
        pyautogui.click(690,459,duration=1)
        sleep(1)