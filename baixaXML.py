import pyautogui
import keyboard
from time import sleep

sleep(3)
with open('baixaXML.txt', 'r') as arquivo:
    for chaveNFE in arquivo:
        #Clicar e preencher o campo da chave
        pyautogui.click(607,327,duration=1)
        with pyautogui.hold('ctrl'):
            pyautogui.press(['a'])
        pyautogui.write(chaveNFE)
        #Consultar
        #pyautogui.click(801,378,duration=1)
        #Não sou robô
        pyautogui.click(295,474,duration=2)
        #Download XML
        pyautogui.click(795,408,duration=3)
        #Nome do arquivo
        pyautogui.click(404,404,duration=1)
        pyautogui.click(404,404,duration=0.5)
        pyautogui.write("-nfe")
        #Salvar
        pyautogui.click(508,482,duration=1)