import pyautogui
import keyboard
from time import sleep

sleep(1)


print('Aperte F6 para iniciar o programa')
def on_press(event):
    if event.name == 'f6':
        verificador = 0
        while verificador < 12:
            pyautogui.press('f2', interval=0.0)
            pyautogui.press('home', interval=0.0)
            pyautogui.press('del', presses=4, interval=0.0)
            pyautogui.press('enter', interval=0.0)
            pyautogui.press('end', interval=0.0)
            verificador += 1
            print(verificador)
    if event.name == 'f8':
        exit()

keyboard.on_press(on_press)
teste = 1
while teste != 0:
    teste

