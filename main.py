import pyautogui
import pyperclip
import time

#Encontrar posição do mouse
def ver_posicao():
    time.sleep(5)
    mouse = pyautogui.position()
    print(mouse)

# 1 abrir o chrome
pyautogui.hotkey("win") #hotkey é atalho
pyperclip.copy("chrome")
pyautogui.hotkey("ctrl","v")
time.sleep(2)
pyautogui.press("enter") #press é para clicar
time.sleep(8)

# 2 abrir guia anonima
pyautogui.hotkey("ctrl","shift","n")
time.sleep(1)

# 3 pesquisar pagina de login outlook
pyperclip.copy("https://login.live.com/login.srf")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
time.sleep(3)

# 4 Fazer Login
pyperclip.copy("")# e-mail
pyautogui.hotkey("ctrl","v")
time.sleep(1)
pyautogui.click(x=809, y=506)
time.sleep(2)
pyperclip.copy("")# senha
pyautogui.hotkey("ctrl","v")
time.sleep(1)
pyautogui.click(x=817, y=539)
time.sleep(2)
pyautogui.press("enter")