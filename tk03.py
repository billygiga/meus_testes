from tkinter import *

janela = Tk()


def excluir():
    l.delete(0)


janela.geometry('340x280')
pessoas = ['maria','paulo','joao','tereza','alex']
lb = Label(janela,text='listbox')
lb.pack()
bt = Button(janela,text='Apagar',width=15,height=2,
            bg='cyan',fg='magenta',command=excluir,relief='groove')
bt.pack(side='bottom')

l = Listbox(janela)
for p in pessoas:
    l.insert(0,p)
l.pack()

janela.mainloop()

