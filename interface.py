import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from time import sleep
import threading as trd

bot = 'Dahmer'

###########################################################################
###########################################################################
# ROBO
def robo():
    import pyautogui
    from time import sleep
    import os
    def encontrar_imagem(imagem):
        try:
            # Procura a imagem na tela e retorna as coordenadas
            coordenadas = pyautogui.locateOnScreen(imagem, confidence=0.9)
            return coordenadas
        except Exception as e:
            print_robo(f"Erro ao encontrar a imagem")
            return None

    def clicar_no_meio(coordenadas):
        x, y, largura, altura = coordenadas
        ponto_medio_x = x + largura // 2
        ponto_medio_y = y + altura // 2
        pyautogui.click(ponto_medio_x, ponto_medio_y)

    def scroll():
        pyautogui.scroll(-200)

    sleep(2)
    pyautogui.press('win')
    sleep(1)
    pyautogui.write('Google Chrome')
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write('www.youtube.com')
    pyautogui.press('enter')
    sleep(5)
    posicao = encontrar_imagem('imagens/shorts.png')
    clicar_no_meio(posicao)
    
    for x in range(0, qtd_scroll):
        sleep(3)
        print_robo(f'Realizando scroll {x+1}')
        scroll()

    pyautogui.hotkey('alt', 'f4')
    print_robo("Robô executado")

###########################################################################
###########################################################################


###########################################################################
###########################################################################
# INTERFACE
def login():
    global qtd_scroll
    global entry_scroll
    try:
        qtd_scroll = int(entry_scroll.get())
    except:
        qtd_scroll = 20
    #Simula 20 scrolls caso nao seja inserido um numero ou menor que 0
    if qtd_scroll < 1:
        qtd_scroll = 20

    messagebox.showinfo(f"{bot} diz", "Agora deixa comigo! Irei assistir alguns shorts para você")
    clear_widgets()
    open_console()
    print_robo(f"Irei assistir {qtd_scroll} shorts")
    t_robo = trd.Thread(target=robo)
    t_robo.start()


def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()


def open_console():
    global text_output
    text_output = scrolledtext.ScrolledText(root)
    text_output.pack(expand=True, fill="both")


def print_robo(text):
    text_output.insert(tk.END, text + '\n')
    text_output.see(tk.END)  # Rola para baixo para mostrar o novo texto
    root.update_idletasks()  # Atualiza a interface para mostrar a nova mensagem
    sleep(0.1)  # Adiciona um pequeno atraso para visualizar cada número


###########################################################################
###########################################################################

root = tk.Tk()
root.title("Login")

# Calcula o tamanho da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Define o tamanho da janela
window_width = 600
window_height = 400

# Calcula a posição da janela para o canto inferior direito
window_x = screen_width - window_width
window_y = screen_height - window_height - 80

# Define a geometria da janela
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Título centralizado grande
label_title = tk.Label(root, text=f"Olá, eu sou {bot}!", font=("Arial", 20))
label_title.place(relx=0.5, rely=0.1, anchor="center")

subtitle_text = "Instruções"
label_subtitle = tk.Label(root, text=subtitle_text, font=("Arial", 16))
label_subtitle.place(relx=0.5, rely=0.25, anchor="center")

# Texto genérico com instruções
instructions = "Você não poderá mexer no computador enquanto eu estiver sendo executado.\nPreciso que todas as janelas do chrome estejam fechadas.(opcional)\nQualquer mais instrução é só por aqui."

label_instructions = tk.Label(root, text=instructions, justify='left')
label_instructions.place(relx=0.5, rely=0.35, anchor="center")

# Caixa de entrada de login
label_username = tk.Label(root, text="Login:")
label_username.place(relx=0.3, rely=0.5, anchor="e")

entry_username = tk.Entry(root)
entry_username.place(relx=0.5, rely=0.5, anchor="center")

# Caixa de entrada de senha
label_password = tk.Label(root, text="Senha:")
label_password.place(relx=0.3, rely=0.6, anchor="e")

entry_password = tk.Entry(root, show="*")
entry_password.place(relx=0.5, rely=0.6, anchor="center")

# Caixa de entrada de quantidade de shorts a assistir
label_scroll = tk.Label(root, text="qtd shorts:")
label_scroll.place(relx=0.3, rely=0.7, anchor="e")

entry_scroll = tk.Entry(root)
entry_scroll.place(relx=0.5, rely=0.7, anchor="center")

entry_scroll = tk.Entry(root)  # Usar a função de validação
entry_scroll.place(relx=0.5, rely=0.7, anchor="center")

# Botão de login
button_login = tk.Button(root, text="Iniciar processo", command=login)
button_login.place(relx=0.5, rely=0.9, anchor="center")

root.mainloop()
