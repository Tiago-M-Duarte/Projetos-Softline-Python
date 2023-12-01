import pyautogui
import keyboard
from time import sleep

sleep(1)

verificador = 0

print('Aperte F7 para parar o programa')
def on_press(event):
    global verificador
    if event.name == 'f7':
        verificador = 1
        print('Programa parado')

keyboard.on_press(on_press)

while verificador == 0:
    pyautogui.press('delete')
    pyautogui.press('enter')
    sleep(0.1)