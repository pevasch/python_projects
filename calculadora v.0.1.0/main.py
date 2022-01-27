from ajustes import *

# inicializa o programa
app = start()

# título; tamanho da janela; cor de fundo
app.title('Calculadora')
app.geometry('250x350')
app.resizable(False,False)
app.configure(bg='#000')

# dispaly
display = tk.Label(app, Fonte_b,bg='#999',width = 12)
display.place(x=10,y=20, height = 60)

# botões da linha 1
b_on = tk.Button(app, Fonte_a, text='C', command = lol)
b_on.place(ajuste_botões['col_1'])

b_af = tk.Button(app, Fonte_a, text='( )')
b_af.place(ajuste_botões['col_2'])

b_porc = tk.Button(app, Fonte_a, text='%')
b_porc.place(ajuste_botões['col_3'])

b_div = tk.Button(app, Fonte_b, text='÷')
b_div.place(ajuste_botões['col_4'])

# botões da linha 2

ajuste_y()

b_7 = tk.Button(app, Fonte_a, text='7')
b_7.place(ajuste_botões['col_1'])


b_8 = tk.Button(app, Fonte_a, text='8')
b_8.place(ajuste_botões['col_2'])

b_9 = tk.Button(app, Fonte_a, text='9')
b_9.place(ajuste_botões['col_3'])

b_x = tk.Button(app, Fonte_a, text='x', command = multi)
b_x.place(ajuste_botões['col_4'])

# botões da linha 3
ajuste_y()

b_4 = tk.Button(app, Fonte_a, text='4')
b_4.place(ajuste_botões['col_1'])

b_5 = tk.Button(app, Fonte_a, text='5')
b_5.place(ajuste_botões['col_2'])

b_6 = tk.Button(app, Fonte_a, text='6')
b_6.place(ajuste_botões['col_3'])

b_menos = tk.Button(app, Fonte_b, text='-')
b_menos.place(ajuste_botões['col_4'])

# botões da linha 4
ajuste_y()

b_1 = tk.Button(app, Fonte_a, text='1', command = b1)
b_1.place(ajuste_botões['col_1'])

b_2 = tk.Button(app, Fonte_a, text='2',command = b2)
b_2.place(ajuste_botões['col_2'])

b_3 = tk.Button(app, Fonte_a, text='3', command = b3)
b_3.place(ajuste_botões['col_3'])

b_mais = tk.Button(app, Fonte_b, text='+', command = maix)
b_mais.place(ajuste_botões['col_4'])

# botões da linha 5
ajuste_y()

b_maismenos = tk.Button(app, Fonte_a, text='+/-')
b_maismenos.place(ajuste_botões['col_1'])

b_0 = tk.Button(app, Fonte_a, text='0')
b_0.place(ajuste_botões['col_2'])

b_separador = tk.Button(app, Fonte_b, text=',')
b_separador.place(ajuste_botões['col_3'])

b_igual = tk.Button(app, Fonte_a, text='=', command = resultado)
b_igual.place(ajuste_botões['col_4'])


# mantém o programa rodando
tk.mainloop()

