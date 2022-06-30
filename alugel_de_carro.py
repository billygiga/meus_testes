from tkinter import *

lista_de_carros = [
    'sedan','corsa','celta','ford ka','nisan',
    'hb 20','hilux','citroen','troler','del rey'
]

janela = Tk()
janela.config(bg='#CD853F')
janela.geometry('580x400')


def click():
    f = Tk()
    f.title('comprovante')
    f.config(bg='#ffdead')
    f.geometry('250x150')
    for i,carro in enumerate(lista_de_carros):
        if en4.get() == carro:
            if lista_de_carros[i] == carro:
                lt.delete(i)
    l = Label(f,text=f'nome: {en2.get()} \ntelefone: {en3.get()} \ncarro: {en4.get()}',
              bg='#ffdead',font='Arial 15 italic')
    l.pack()
    f.mainloop()


lb1 = Label(janela,text='Carros Disponiveis',font='Helvetica 15',bg='#CD853F')
lb1.place(x=20,y=20)

lt = Listbox(janela,font='Arial 15',bd=3,bg='#ccc')
for i in lista_de_carros:
    lt.insert(END,i)

lt.place(x=20,y=50)
lb2 = Label(janela,text='Nome',font='Helvetica 15',bg='#CD853F')
lb2.place(x=360,y=40)
en2 = Entry(janela,width=30,font='bold 13')
en2.place(x=260,y=80)

lb3 = Label(janela,text='Telefone',font='Helvetica 15',bg='#CD853F')
lb3.place(x=360,y=120)
en3 = Entry(janela,width=30,font='bold 13')
en3.place(x=260,y=180)

lb4 = Label(janela,text='Carro',font='Helvetica 15',bg='#CD853F')
lb4.place(x=360,y=220)
en4 = Entry(janela,width=30,font='bold 13')
en4.place(x=260,y=275)

bt = Button(janela,text='Confirmar',font='bold 13 bold',
            bg='#3c3c3c',fg='red',command=click,width=20,relief='groove')
bt.place(x=30,y=340)

janela.mainloop()