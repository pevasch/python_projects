import tkinter

def command():
    global str1
    global str_1
    str_1 += "oeriteieir"
    str1.set(str_1)

app = tkinter.Tk()
app.geometry("250x300")
str_1 = ''
app.configure(bg="#fff")
frame = tkinter.Frame(app)
frame.pack()
str1 = tkinter.StringVar()
str1.set(str_1)
label = tkinter.Label(master=frame, textvariable=str1)
bt = tkinter.Button(app, text='Quit', command=command)
label.pack()
bt.pack()
app.mainloop()








'''
def b7():
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
            if texto_display == '':
                texto_display = '7'
            else:
                texto_display += '7'
            contador += 1
        texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
        texto.place(x=x, y=30)

def b8():
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
            if texto_display == '':
                texto_display = '8'
            else:
                texto_display += '8'
            contador += 1
        texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
        texto.place(x=x, y=30)

def b9():
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
            if texto_display == '':
                texto_display = '9'
            else:
                texto_display += '9'
            contador += 1
        texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
        texto.place(x=x, y=30)
'''
'''
def b4():
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
            if texto_display == '':
                texto_display = '4'
            else:
                texto_display += '4'
            contador += 1
        texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
        texto.place(x=x, y=30)

def b5():
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
            if texto_display == '':
                texto_display = '5'
            else:
                texto_display += '5'
            contador += 1
        texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
        texto.place(x=x, y=30)

def b6():
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
            if texto_display == '':
                texto_display = '6'
            else:
                texto_display += '6'
            contador += 1
        texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
        texto.place(x=x, y=30)
'''
'''
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
            if texto_display == '':
                texto_display = '1'
            else:
                texto_display += '1'
            contador += 1
        texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
        texto.place(x=x, y=30)



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
            if texto_display == '':
                texto_display = '2'
            else:
                texto_display += '2'
            contador += 1
        texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
        texto.place(x=x, y=30)

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
           if texto_display == '':
               texto_display = '3'
           else:
               texto_display += '3'
           contador += 1
       texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
       texto.place(x=x, y=30)

'''
'''
def b0():
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
           if texto_display == '':
               texto_display = '0'
           else:
               texto_display += '0'
           contador += 1
       texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
       texto.place(x=x, y=30)
'''
'''
def div():
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
            if texto_display != '' and not texto_display[-1] in '+-x÷':
                texto_display += '÷'
            contador += 1
        texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
        texto.place(x=x, y=30)
'''


'''def multi():
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
            if texto_display != '' and not texto_display[-1] in '+-x÷':
                texto_display += 'x'
            contador += 1
        texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
        texto.place(x=x, y=30)
'''


'''
def menox():
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
            if texto_display != '' and not texto_display[-1] in '+-x÷':
                texto_display += '-'
            contador += 1
        texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
        texto.place(x=x, y=30)
'''

'''
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
            if texto_display != '' and not texto_display[-1] in '+-x÷':
                texto_display += '+'
            contador += 1
        texto = tk.Label(app, Fonte_b, text=texto_display, bg='#999', fg='#fff')
        texto.place(x=x, y=30)
'''

'''
def b_números(num):
    global texto
    global contador
    global texto_display
    try:
        texto.destroy()
    except:
        print('avaliar possível erro.')
    finally:
       if contador < 10:
           if texto_display == '':
               texto_display += num
           else:
               texto_display += num
           contador += 1
       texto = tk.Text(app, Fonte_b, height=1.4, width=12, bg='#999', fg='#fff')
       texto.tag_config('justified',justify='right')
       texto.insert(tk.INSERT, texto_display,'justified')
       texto.grid(pady=20, padx=15)
'''

'''
def b_operadores(op):
    global texto
    global contador
    global texto_display
    try:
        texto.destroy()
    except:
        print('avaliar possível erro.')
    finally:
        if contador < 10:
            if texto_display != '' and not texto_display[-1] in '+-x÷':
                texto_display += op
            contador += 1
        texto = tk.Text(app, Fonte_b, height=1.4, width=12, bg='#999', fg='#fff')
        texto.tag_config('justified',justify='right')
        texto.insert(tk.INSERT, texto_display,'justified')
        texto.grid(pady=20, padx=15)
'''

'''
def b_destroy():
    global contador
    global texto_display
    texto.destroy()
    texto_display = ''
    contador = 0
'''