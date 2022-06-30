from tkinter import *
import os


class Master:
    def __init__(self,master):
        self.master = master
        self.master.configure(bg='#b0c4de')
        self.master.geometry('640x480')
        self.lb = Label(master,text='Cadastro de Alunos',font='bold 20 bold',fg='green',bg='#b0c4de')
        self.lb.pack()
        self.lb1 = Label(master,text='Nome',font='bold 20 bold',fg='grey',bg='#b0c4de')
        self.lb1.place(x=30,y=100)
        self.en1 = Entry(master,width=40,font='bold 15 italic',bd=2)
        self.en1.place(x=150,y=110)
        self.lb2 = Label(master,text='Serie',font='bold 20 bold',fg='grey',bg='#b0c4de')
        self.lb2.place(x=30,y=150)
        self.en2 = Entry(master, width=20, font='bold 15 italic',bd=2)
        self.en2.place(x=150, y=160)
        self.lb3 = Label(master, text='Turno', font='bold 20 bold', fg='grey',bg='#b0c4de')
        self.lb3.place(x=30, y=200)
        self.en3 = Entry(master, width=20, font='bold 15 italic',bd=2)
        self.en3.place(x=150, y=200)
        self.lb4 = Label(master, text='Sala', font='bold 20 bold', fg='grey',bg='#b0c4de')
        self.lb4.place(x=30, y=250)
        self.en4 = Entry(master, width=20, font='bold 15 italic',bd=2)
        self.en4.place(x=150, y=250)
        self.bt = Button(master,text='Cadastrar',font='bold 20 bold',
                         fg='red',bg='grey',relief='groove',command=self.salvar)
        self.bt.place(x=460,y=400)

    def salvar(self):
        #os.mkdir('pasta_alunos')
        with open('pasta_alunos/aluno01.txt','a+') as f:
            f.write(f'Nome :{self.en1.get()}\n')
            f.write(f'Serie :{self.en2.get()}\n')
            f.write(f'Turno :{self.en3.get()}\n')
            f.write(f'Sala :{self.en4.get()}\n')
            f.write(f'{"====================="}\n')
        self.master.destroy()


if __name__ == '__main__':
    root = Tk()
    Master(root)
    root.mainloop()
