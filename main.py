import pyautogui
import pyperclip
import time
import requests
import sys 
import os

#Encontrar posição do mouse
def ver_posicao():
    time.sleep(5)
    mouse = pyautogui.position()
    print(mouse)

try:
    db = sys.argv[1]
    dl = sys.argv[2]
except Exception:
    #Caso queira mudar a db e o delimitador
    db = "db.txt"
    dl = "|"

    f = open(db,'r').readlines()

    for i in range(len(f)):
        email = f[i].split()[0].split(dl)[0]
        senha = f[i].split()[0].split(dl)[1]

        print(email+"|"+senha)


        # 1 abrir o chrome
        pyautogui.hotkey("win") #hotkey é atalho
        pyperclip.copy("chrome")
        pyautogui.hotkey("ctrl","v")
        time.sleep(5)
        pyautogui.press("enter") #press é para clicar
        time.sleep(15)

        # 2 abrir guia anonima
        pyautogui.hotkey("ctrl","shift","n")
        time.sleep(2)

        # 3 pesquisar pagina de login outlook
        pyperclip.copy("https://login.live.com/login.srf")
        pyautogui.hotkey("ctrl","v")
        pyautogui.press("enter")
        time.sleep(5)

        # 4 Fazer Login
        pyperclip.copy(email)# e-mail
        pyautogui.hotkey("ctrl","v")
        time.sleep(1)
        pyautogui.click(x=809, y=506)
        time.sleep(2)
        pyperclip.copy(senha)# senha
        pyautogui.hotkey("ctrl","v")
        time.sleep(1)
        pyautogui.click(x=817, y=539)
        time.sleep(2)
        pyautogui.press("enter")