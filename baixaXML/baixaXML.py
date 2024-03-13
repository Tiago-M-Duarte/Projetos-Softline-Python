# Algoritmo para baixar xmls pelo Fsist utilizando chaves NFe colocadas no arquivo "baixaXML.txt"
import pyautogui
from time import sleep

sleep(3)
with open('baixaXML/baixaXML.txt', 'r') as arquivo:
    for chaveNFE in arquivo:
        #Clicar e preencher o campo da chave
        pyautogui.click(456,170,duration=1)
        with pyautogui.hold('ctrl'):
            pyautogui.press(['a'])
        pyautogui.write(chaveNFE)
        #Consultar
        #pyautogui.click(801,378,duration=1)
        #Não sou robô
        pyautogui.click(287,445,duration=2)
        #Download XML
        pyautogui.click(831,317,duration=3)
        #Nome do arquivo
        pyautogui.click(402,625,duration=1)
        pyautogui.click(402,625,duration=0.5)
        pyautogui.write("-nfe")
        #Salvar
        pyautogui.click(1190,689,duration=1)