from func_buttons import *

'''
Aqui vai ser posto o que vai fazer a calculadora funcionar e majoritariamente a parte de front como os botões, o display etc
'''

# inicializa o programa
app = start()

# título
app.title('Calculadora')

# ajusta o tamanho da janela
app.geometry('250x350')

# não deixa a janela ser redimensionada
app.resizable(False,False)

# cor de fundo da janela
app.configure(bg='#223')

# cria o display e ajusta sua posição
display = tk.Frame(app, bg='#999',width = 220)
display.place(x=15,y=20, height = 42)

'''
Criação dos botões e seus ajustes. Com o parâmetro command é possível atribuir funções a esses botões.
'''

testezinho = b_especiais

# BOTÕES DA LINHA 1

tk.Button(app, Fonte_a, text='C', command = buttons('C')).place(ajuste_botões['col_1'])

b_af = tk.Button(app, Fonte_a, text='( )', command=lambda : testezinho('( )'))
b_af.place(ajuste_botões['col_2'])

b_porc = tk.Button(app, Fonte_c, text='⌫', command=lambda : b_especiais('⌫'))
b_porc.place(ajuste_botões['col_3'])

b_div = tk.Button(app, Fonte_b, text='÷', command= lambda : buttons('÷'))
b_div.place(ajuste_botões['col_4'])

# função para ajustar a altura dos próximos botões (y)
ajuste_y()

# BOTÕES DA LINHA 2

b_7 = tk.Button(app, Fonte_a, text='7', command=lambda : buttons('7'))
b_7.place(ajuste_botões['col_1'])

b_8 = tk.Button(app, Fonte_a, text='8', command=lambda : buttons('8'))
b_8.place(ajuste_botões['col_2'])

b_9 = tk.Button(app, Fonte_a, text='9', command=lambda : buttons('9'))
b_9.place(ajuste_botões['col_3'])

b_x = tk.Button(app, Fonte_a, text='x', command= lambda : buttons('x'))
b_x.place(ajuste_botões['col_4'])

ajuste_y()

# BOTÕES DA LINHA 3

b_4 = tk.Button(app, Fonte_a, text='4',command=lambda : buttons('4'))
b_4.place(ajuste_botões['col_1'])

b_5 = tk.Button(app, Fonte_a, text='5',command=lambda : buttons('5'))
b_5.place(ajuste_botões['col_2'])

b_6 = tk.Button(app, Fonte_a, text='6',command=lambda : buttons('6'))
b_6.place(ajuste_botões['col_3'])

b_menos = tk.Button(app, Fonte_b, text='-', command= lambda : buttons('-'))
b_menos.place(ajuste_botões['col_4'])

ajuste_y()

# BOTÔES DA LINHA 4

b_1 = tk.Button(app, Fonte_a, text='1', command=lambda : buttons('1'))
b_1.place(ajuste_botões['col_1'])

b_2 = tk.Button(app, Fonte_a, text='2',command=lambda : buttons('2'))
b_2.place(ajuste_botões['col_2'])

b_3 = tk.Button(app, Fonte_a, text='3', command=lambda : buttons('3'))
b_3.place(ajuste_botões['col_3'])

b_mais = tk.Button(app, Fonte_b, text='+', command= lambda : buttons('+'))
b_mais.place(ajuste_botões['col_4'])

ajuste_y()

# BOTÕES DA LINHA 5

b_maismenos = tk.Button(app, Fonte_a, text='+/-', command=lambda : b_especiais('+/-'))
b_maismenos.place(ajuste_botões['col_1'])

b_0 = tk.Button(app, Fonte_a, text='0', command=lambda : buttons('0'))
b_0.place(ajuste_botões['col_2'])

b_separador = tk.Button(app, Fonte_b, text='.', command=lambda : b_especiais('.'))
b_separador.place(ajuste_botões['col_3'])

b_igual = tk.Button(app, Fonte_a, text='=', command=lambda : b_especiais('='))
b_igual.place(ajuste_botões['col_4'])


# mantém o programa rodando
tk.mainloop()

