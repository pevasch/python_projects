import tkinter as tk
from fontes import *

def start():
    global app
    app = tk.Tk()
    return app

# função teste para botar no parâmetro command do botão

y = 100

texto_display = str

def lol():
    print('lol')

# variáveis para ajustar coluna e tamanho dos botões
# criei dicionário, pois assim consigo passar os parâmetros na função de alocação do botão

ajuste_botões = {
'col_1' : {'x':12, 'y':y,'width':45,'height':45},
'col_2' : {'x':72, 'y':y,'width':45,'height':45},
'col_3' : {'x':132, 'y':y,'width':45,'height':45},
'col_4' : {'x':192, 'y':y,'width':45,'height':45},
}


def ajuste_y():
    global y
    y += 50
    for c in ajuste_botões.values():
        c['y'] = y

contador = 0
x = 192
valor = 0
texto = tk.Label

def b1():
    global texto
    global contador
    global x
    global texto_display
    try:
        texto.destroy()
    except:
        print('avaliar possível erro.')
    finally:
        if contador < 10:
            if contador > 0:
                x -= 20
            if texto_display == str:
                texto_display = '1'
            else:
                texto_display += '1'
            contador += 1
        texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
        #texto.place(x=x, y=30)
        texto.pack()



def b2():
    global texto
    global contador
    global x
    global texto_display
    try:
        texto.destroy()
    except:
        print('avaliar possível erro.')
    finally:
        if contador < 10:
            if contador > 0:
                x -= 20
            if texto_display == str:
                texto_display = '2'
            else:
                texto_display += '2'
            contador += 1
        texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
        #texto.place(x=x, y=30)
        texto.pack()

def b3():
    global texto
    global contador
    global x
    global texto_display
    try:
        texto.destroy()
    except:
        print('avaliar possível erro.')
    finally:
       if contador < 10:
           if contador > 0:
               x -= 20
           if texto_display == str:
               texto_display = '3'
           else:
               texto_display += '3'
           contador += 1
       texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
       #texto.place(x=x, y=30)
       texto.pack()


def maix():
    global texto
    global contador
    global x
    global texto_display
    try:
        texto.destroy()
    except:
        print('avaliar possível erro.')
    finally:
        if contador < 10:
            if contador > 0:
                x -= 20
            if texto_display != str and not texto_display[-1] in '+-x÷':
                texto_display += '+'
            contador += 1
        texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
        texto.place(x=x, y=30)

def multi():
    global texto_display
    global contador
    global x

    if texto_display != str and not texto_display[-1] in '+-x÷':
        texto_display += 'x'
        texto = tk.Label(app, Fonte_b,text = texto_display,bg='#999', fg = '#fff')

        if contador > 0:
            x -= 20

        if contador < 10:
            texto.place(x=x, y=30)
            contador += 1


def resultado():
    global texto_display
    global contador
    global x
    global texto
    try:
        texto.destroy()
    except:
        print('avaliar possível erro.')
    finally:
        if contador < 10:
            if texto_display != str and texto_display[-2] in '+-x÷':
                texto_display = texto_display.replace('x', '*')
                texto_display = texto_display.replace('÷', '/')

                contador = 0
                x = 192

                texto = tk.Label(app, Fonte_b, text=eval(texto_display), bg='#999', fg='#fff')
                texto.pack()
                texto_display = str