import tkinter as tk
from calc_fonts import *

'''
Funcões utilizadas para iniciar o programa, posicionar os botões e dar funcionalidade para eles.
'''
# VARIÁVEIS

# para controlar o número de elementos na expressão matemática
contador = 0

sep_contador = 0

# 
texto = tk.Label
texto_display = ''
y = 100

# variáveis para ajustar coluna e tamanho dos botões
# criei dicionário, pois assim consigo passar os parâmetros na função de alocação do botão

ajuste_botões = {
'col_1' : {'x':12, 'y':y,'width':45,'height':45},
'col_2' : {'x':72, 'y':y,'width':45,'height':45},
'col_3' : {'x':132, 'y':y,'width':45,'height':45},
'col_4' : {'x':192, 'y':y,'width':45,'height':45},
}

def start():
    global app
    app = tk.Tk()
    return app


def ajuste_y():
    global y
    y += 50
    for c in ajuste_botões.values():
        c['y'] = y

# BOTÕES ESPECIAIS

def b_especiais(esp):
    global texto
    global contador
    global texto_display
    global sep_contador

    try:
            texto.destroy()
    except:
        print('avaliar possível erro.')
    finally:
        if esp == '( )':
            if contador < 10:
                if texto_display != '' and not texto_display[-1] in '+-x÷':
                    texto_display += '('
                contador += 1
        elif esp == '⌫':
            if texto_display != '':
                    texto_display = texto_display[:-1]
                    contador -= 1
        elif esp == '+/-':
            if contador < 10:
                if texto_display != '' and texto_display[-1] in '+-x÷':
                    texto_display += '(-'
                contador += 1
        elif esp == '.':
            if contador < 10:
                if texto_display == '':
                    texto_display = '0,'
                elif sep_contador == 0:
                    texto_display += '.'
                    sep_contador += 1
                contador += 1
        elif esp == '=':
            if contador < 10:
                if texto_display != '':
                    texto_display = texto_display.replace('x', '*')
                    texto_display = texto_display.replace('÷', '/')
                    contador = 0
                    texto_display = str(eval(texto_display))
    texto = tk.Text(app, Fonte_b, height=1.4, width=12, bg='#999', fg='#fff')
    texto.tag_config('justified',justify='right')
    texto.insert(tk.INSERT, texto_display,'justified')
    texto.grid(pady=20, padx=15)
    if esp == '=':
        texto_display = ''

# TESTES

def buttons(button):
    global contador
    global texto_display
    global texto
    numbers = '0123456789'
    operators = '+-x÷'
    if button == 'C':
        #texto.destroy()
        texto_display = ''
        contador = 0
    else:
        try:
            texto.destroy()
        except:
            print('avaliar pssível erro.')
        finally:
            if contador <= 10:
                if button in numbers:
                    texto_display += button
                    print('lol1')
                if button in operators:
                    print('lol2')
                    if texto_display != '' and not texto_display[-1] in operators:
                        print('lol3')
                        texto_display += button
                contador += 1
        texto = tk.Text(app, Fonte_b, height=1.4, width=12, bg='#999', fg='#fff')
        texto.tag_config('justified', justify='right')
        texto.insert(tk.INSERT, texto_display, 'justified')
        texto.grid(pady=20,padx=15)
