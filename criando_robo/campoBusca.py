# pegando a posicao de um elemento
import time

import pyautogui

for i in range(5):
    print(f"pegando posicao em {5 - i} segundos")
    time.sleep(1)

print(pyautogui.position())
