from ast import operator
import tkinter as tk

app = tk.Tk()
app.title('Calculadora')
app.geometry('250x350')
app.resizable(False,False)
app.configure(bg='#223')

display = tk.Frame(app, bg='#999', width=220)
display.place(x=15, y=20, height=42)

y=100
x=12

teclas = ['C', '( )', '⌫', '÷', '7', '8', '9', 'x', '4', '5', '6', '-', '1', '2', '3', '+', '+/-', '0', '.', '=']
texto_base_display = ''
texto_display = tk.StringVar()
texto_display.set(texto_base_display)

label = tk.Label(display, textvariable=texto_display, bg='#999', width=22)

posicao_x = 120

def func_buttons(tecla):
    global texto_display
    global texto_base_display
    numbers = '0123456789'
    operators = '+-x÷'
    global posicao_x
    print(tecla)
    if tecla in numbers:
        texto_base_display += tecla
    elif tecla in operators:
        if texto_base_display != '' and not texto_base_display[-1] in operators:
            texto_base_display += tecla
    elif tecla == 'C':
        texto_base_display = ''
    elif tecla == '=':
        texto_base_display = texto_base_display.replace('x', '*').replace('÷', '/')
        texto_base_display = str(eval(texto_base_display))
    texto_display.set(texto_base_display)
    label.place(x=posicao_x, y=0, height=42)
    if tecla == '=':
        texto_base_display = ''
    posicao_x -= 1.5


teste =[]

for l in range(0,20,4):
    for c in range(4):
        posicao = l + c
        teste.append(tk.Button(app, text=teclas[posicao], command=lambda posicao=posicao: func_buttons(teclas[posicao])))
        teste[posicao].place(x=x,y=y, width=45, height=45)
        x += 60
    x = 12
    y += 50

tk.mainloop()