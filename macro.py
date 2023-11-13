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

while verificador == 0:
    pyautogui.keyDown('altleft')
    pyautogui.keyDown('x')
    sleep(1)
    pyautogui.keyUp('x')
    pyautogui.keyUp('altleft')
    sleep(3)        
    pyautogui.press('enter')
    pyautogui.press('down')
    sleep(0.8)






