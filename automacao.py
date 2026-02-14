import pyautogui
import pandas
import time
pyautogui.PAUSE = 2

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
#PASSO1: entrar no sistema
#abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(7)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(4)

#PASSO2: fazer login
#clica no campo de email
pyautogui.click(x=764, y=519)
pyautogui.write("sla.cursomaneiro@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhairada123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

#PASSO3: Abrir base de dados (importar arquivos)
tabela = pandas.read_csv("produtos.csv")
print(tabela)

#PASSO 4: Cadastrar 1 produto /PASSO5: repetir isso até acabar os itens
for linha in tabela.index:
    #código
    pyautogui.click(x=1008, y=377)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #preco_unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linha, "obs"])
    pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    #volta para o início da tela 
    pyautogui.scroll(5000)  