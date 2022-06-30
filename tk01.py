from tkinter import *


class Master:
    def __init__(self, master):
        self.master = master
        self.master.geometry('640x480')
        # self.master.config(bg='blue')
        self.lb = Label(self.master, text='mudando as cores do quadro',
              font='bold 20', fg='black')
        self.lb.pack(pady=15)

        Button(self.master, width=20, text='pintar de vermelho', command=self.click).pack(pady=35)

        Button(self.master, width=20, text='pintar de verde', command=self.click2).pack(pady=15)

        Button(self.master, width=20, text='pintar de azul', command=self.click3).pack(pady=20)

    def click(self):
        self.master.config(bg='red')
        self.lb.configure(bg='red')

    def click2(self):
        self.master.config(bg='green')
        self.lb.configure(bg='green')

    def click3(self):
        self.master.config(bg='blue')
        self.lb.configure(bg='blue')


if __name__ == '__main__':
    root = Tk()
    Master(root)
    root.mainloop()
