import pyautogui
import keyboard
from time import sleep

sleep(1)


print('Aperte F7 para iniciar o programa')
def on_press(event):
    if event.name == 'f7':
        verificador = 0
        while verificador < 8:
            pyautogui.press('enter', interval=0.0)
            pyautogui.press('end', interval=0.0)
            pyautogui.press('enter', interval=0.0)
            pyautogui.press('end', interval=0.0)
            pyautogui.hotkey('ctrl', 'a', interval=0.0)
            pyautogui.hotkey('ctrl', 'x', interval=0.0)
            pyautogui.press('backspace', interval=0.0)
            pyautogui.hotkey('ctrl', 'v', interval=0.0)
            pyautogui.press('backspace', interval=0.0)
            pyautogui.press('up', interval=0.0)
            verificador += 1
            print(verificador)
    if event.name == 'f8':
        exit()

keyboard.on_press(on_press)
teste = 1
while teste != 0:
    teste

