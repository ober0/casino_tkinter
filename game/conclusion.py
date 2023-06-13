import random
import time

import pickle
from tkinter import Tk, Button
from PIL import ImageTk
from tkinter import Tk, Label, Button, mainloop
from tkinter import *
from threading import Thread
import tkinter as tk
from warn import warn, warn1


class Deposit(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x300')
        self.procent = 0
        self.resizable(width=False, height=False)
        Label(self, text='Введите сумму вывода', fg='blue',  font=('Comic Sans MS', 20, 'bold')).place(x=90,y=10)
        Label(self, text='Вывести',  font=('Comic Sans MS', 16, 'bold')).place(x=130,y=100)
        self.summaEntry = Entry(self,
                           background='white',
                           justify='center',
                           width=6,
                           font=('Comic Sans MS', 11, 'bold'))
        self.summaEntry.place(x=240,y=108)
        Label(self, text='$', font=('Comic Sans MS', 16, 'bold')).place(x=290, y=100)
        self.sendMoneyBtn = Button(self,
                                     font=('Comic Sans MS', 12, 'bold'),
                                     bg='gray',
                                     fg='white',
                                     text='Запросить.',
                                     borderwidth=1,
                                     relief="sunken",
                                     underline=-1,
                                     width=9,
                                     pady=1,
                                     command=self.send
                                     )
        self.sendMoneyBtn.place(x=140, y=150)

        self.x = 0
        self.labelZagruzka = Label(self, text='Загрузка {} %'.format(self.procent), font=('Comic Sans MS', 16, 'bold'))


    def send(self):
        if self.x == 1:
            warn1(0, 'Вывод успешный, перезапустите приложение!')
            quit()
        global deposit
        deposit = int(self.summaEntry.get())
        try:
            self.labelZagruzka.place(x=172, y=210)
        except:
            pass
        self.procent += 5
        if self.procent <= 100:
            if self.procent <= 100:
                self.labelZagruzka.configure(text='Загрузка {} %'.format(self.procent))

        elif self.procent > 100:
                with open('balance.txt', 'rb') as file:
                    balance = float(pickle.load(file))
                if deposit > balance:
                    warn(119, 'Недостаточно средств для вывода')
                    return
                balance -= deposit
                with open('balance.txt', 'wb') as file2:
                    pickle.dump(str(balance), file2)
                self.x = 1
        self.after(100,self.send)

def maiin():
    appDep = Deposit()
    appDep.mainloop()
def conclusson():
    maiin()