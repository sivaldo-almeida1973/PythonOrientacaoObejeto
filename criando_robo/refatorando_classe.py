# ### Refatorando com classe

# In[43]:


import time
import pyautogui
import pyperclip

class Controlador():
    def __init__(self):
        pyautogui.PAUSE = 1

    def abrir_programa(self, nome_programa):
        pyautogui.press("win")
        pyautogui.write(nome_programa)
        pyautogui.press("enter")

    def escrever(self, texto):
        pyperclip.copy(texto)
        pyautogui.hotkey("ctrl", "v")

    def escrever_e_enter(self, texto):
        self.escrever(texto)
        pyautogui.press("enter")

    def entrar_site(self, site, espera=3):
        self.escrever_e_enter(site)
        self.aguardar(espera)

    def aguardar(self, tempo=3):
        time.sleep(tempo)

    def clicar(self, pos_x, pos_y, botao="left"):
        pyautogui.click(pos_x, pos_y, button=botao)

    def pegar_posicao(self):
        for i in range(5):
            print(f"pegando posicao em {5 - i} segundos")
            time.sleep(1)
        print(pyautogui.position())

    def extrair_link(self, pos_x, pos_y, posicao_link_menu=2):
        self.clicar(pos_x, pos_y, botao="right")
        for i in range(posicao_link_menu):
            pyautogui.press("up")
        pyautogui.press("enter")
        texto = pyperclip.paste()
        print(texto)


# In[44]:


controlador = Controlador()
controlador.abrir_programa("chrome")
controlador.entrar_site("https://www.hashtagtreinamentos.com/blog")
controlador.clicar(1469, 589)
controlador.escrever_e_enter("classe")
controlador.aguardar()
controlador.clicar(749, 699)
controlador.aguardar()
controlador.extrair_link(390, 789)


# In[39]:


controlador.pegar_posicao()


# In[ ]:


