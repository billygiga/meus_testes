from tkinter import *


class Master:
    def __init__(self,master):
        self.master = master
        self.master.geometry('333x300')
        self.master.title('Calculadora')
        self.var = StringVar()
        self.msn = ''
        self.en = Entry(self.master,width=22,font='Arial 20',justify='right',bd=2,bg='grey',textvariable=self.var)
        self.en.grid(row=0,column=0,columnspan=4)
        self.bt1 = Button(self.master,text='%',width=10,height=2,font='bold 9 bold',bg='black',fg='white')
        self.bt1.grid(row=1, column=0)
        self.bt2 = Button(self.master, text='CE', width=10,height=2,font='bold 9 bold',bg='black',fg='white')
        self.bt2.grid(row=1, column=1)
        self.bt3 = Button(self.master, text='C', width=10,height=2,font='bold 9 bold',
                          bg='black',fg='white',command=self.clear)
        self.bt3.grid(row=1, column=2)
        self.bt4 = Button(self.master, text='<<', width=10,height=2,font='bold 9 bold',bg='black',fg='white')
        self.bt4.grid(row=1, column=3)
        self.bt5 = Button(self.master, text='1/x', width=10, height=2,font='bold 9 bold',bg='black',fg='white')
        self.bt5.grid(row=2, column=0)
        self.bt6 = Button(self.master, text='x2', width=10, height=2,font='bold 9 bold',bg='black',fg='white')
        self.bt6.grid(row=2, column=1)
        self.bt7 = Button(self.master, text='√2', width=10, height=2,font='bold 9 bold',bg='black',fg='white')
        self.bt7.grid(row=2, column=2)
        self.bt8 = Button(self.master, text='/', width=10, height=2,font='bold 9 bold',
                          bg='black',fg='white',command=self.div)
        self.bt8.grid(row=2, column=3)
        self.bt9 = Button(self.master, text='7', width=10, height=2, font='bold 9 bold',
                          bg='black', fg='white',command=self.num7)
        self.bt9.grid(row=3, column=0)
        self.bt10 = Button(self.master, text='8', width=10, height=2, font='bold 9 bold',
                           bg='black', fg='white',command=self.num8)
        self.bt10.grid(row=3, column=1)
        self.bt11 = Button(self.master, text='9', width=10, height=2, font='bold 9 bold',
                           bg='black', fg='white',command=self.num9)
        self.bt11.grid(row=3, column=2)
        self.bt12 = Button(self.master, text='X', width=10, height=2, font='bold 9 bold',
                           bg='black', fg='white',command=self.mult)
        self.bt12.grid(row=3, column=3)
        self.bt13 = Button(self.master, text='4', width=10, height=2, font='bold 9 bold',
                           bg='black', fg='white',command=self.num4)
        self.bt13.grid(row=4, column=0)
        self.bt14 = Button(self.master, text='5', width=10, height=2, font='bold 9 bold',
                           bg='black', fg='white',command=self.num5)
        self.bt14.grid(row=4, column=1)
        self.bt15 = Button(self.master, text='6', width=10, height=2, font='bold 9 bold',
                           bg='black', fg='white',command=self.num6)
        self.bt15.grid(row=4, column=2)
        self.bt16 = Button(self.master, text='-', width=10, height=2, font='bold 9 bold',
                           bg='black', fg='white',command=self.sub)
        self.bt16.grid(row=4, column=3)
        self.bt17 = Button(self.master, text='1', width=10, height=2, font='bold 9 bold',
                           bg='black', fg='white',command=self.num1)
        self.bt17.grid(row=5, column=0)
        self.bt18 = Button(self.master, text='2', width=10, height=2, font='bold 9 bold',
                           bg='black', fg='white',command=self.num2)
        self.bt18.grid(row=5, column=1)
        self.bt19 = Button(self.master, text='3', width=10, height=2, font='bold 9 bold',
                           bg='black', fg='white',command=self.num3)
        self.bt19.grid(row=5, column=2)
        self.bt20 = Button(self.master, text='+', width=10, height=2, font='bold 9 bold',
                           bg='black', fg='white',command=self.add)
        self.bt20.grid(row=5, column=3)
        self.bt21 = Button(self.master, text='+/-', width=10, height=2, font='bold 9 bold', bg='black', fg='white')
        self.bt21.grid(row=6, column=0)
        self.bt22 = Button(self.master, text='0', width=10, height=2, font='bold 9 bold',
                           bg='black', fg='white',command=self.zero)
        self.bt22.grid(row=6, column=1)
        self.bt23 = Button(self.master, text=',', width=10, height=2, font='bold 9 bold',
                           bg='black', fg='white',command=self.ponto)
        self.bt23.grid(row=6, column=2)
        self.bt24 = Button(self.master, text='=', width=10, height=2, font='bold 9 bold',
                           bg='black', fg='white',command=self.equal)
        self.bt24.grid(row=6, column=3)

    def num1(self):
        self.msn += '1'
        self.var.set(self.msn)

    def num2(self):
        self.msn += '2'
        self.var.set(self.msn)

    def num3(self):
        self.msn += '3'
        self.var.set(self.msn)

    def num4(self):
        self.msn += '4'
        self.var.set(self.msn)

    def num5(self):
        self.msn += '5'
        self.var.set(self.msn)

    def num6(self):
        self.msn += '6'
        self.var.set(self.msn)

    def num7(self):
        self.msn += '7'
        self.var.set(self.msn)

    def num8(self):
        self.msn += '8'
        self.var.set(self.msn)

    def num9(self):
        self.msn += '9'
        self.var.set(self.msn)

    def zero(self):
        self.msn += '0'
        self.var.set(self.msn)

    def clear(self):
        self.msn = ''
        self.var.set(self.msn)

    def add(self):
        self.msn += '+'
        self.var.set(self.msn)

    def sub(self):
        self.msn += '-'
        self.var.set(self.msn)

    def mult(self):
        self.msn += '*'
        self.var.set(self.msn)

    def div(self):
        self.msn += '/'
        self.var.set(self.msn)

    def ponto(self):
        self.msn += '.'
        self.var.set(self.msn)

    def equal(self):
        try:
            self.r = eval(self.msn)
            self.mensagem = str(self.r)
            self.var.set(self.mensagem)
        except:
            self.var.set('ERROR!!!')


if __name__ == '__main__':
    root = Tk()
    Master(root)
    root.mainloop()