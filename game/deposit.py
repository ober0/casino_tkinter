import random
import time

import pickle
from tkinter import Tk, Button
from PIL import ImageTk
from tkinter import Tk, Label, Button, mainloop
from tkinter import *
from threading import Thread
import tkinter as tk



class Deposit(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x300')
        self.procent = 0
        self.resizable(width=False, height=False)
        Label(self, text='Введите сумму депозита', fg='blue',  font=('Comic Sans MS', 20, 'bold')).place(x=90,y=10)
        Label(self, text='Пополнить на',  font=('Comic Sans MS', 16, 'bold')).place(x=130,y=100)
        self.summaEntry = Entry(self,
                           background='white',
                           justify='center',
                           width=6,
                           font=('Comic Sans MS', 11, 'bold'))
        self.summaEntry.place(x=295,y=108)
        Label(self, text='$', font=('Comic Sans MS', 16, 'bold')).place(x=355, y=100)
        self.sendMoneyBtn = Button(self,
                                     font=('Comic Sans MS', 12, 'bold'),
                                     bg='gray',
                                     fg='white',
                                     text='Пополнить.',
                                     borderwidth=1,
                                     relief="sunken",
                                     underline=-1,
                                     width=9,
                                     pady=1,
                                     command=self.send
                                     )
        self.sendMoneyBtn.place(x=200, y=150)


        self.labelZagruzka = Label(self, text='Загрузка {} %'.format(self.procent), font=('Comic Sans MS', 16, 'bold'))


    def send(self):
        x = 0
        global deposit
        try:
            self.labelZagruzka.place(x=172, y=210)
        except:
            pass
        self.procent += 5
        if self.procent <= 100:
            if self.procent <= 100:
                self.labelZagruzka.configure(text='Загрузка {} %'.format(self.procent))
                x = 1

        elif self.procent > 100:
            self.after(2250, self.send)
            if self.summaEntry.get() != '':
                self.labelZagruzka.configure(text='Пополнение успешно. \n Перезапустите приложение')
                self.labelZagruzka.place(x=105, y=210)
                dep = self.summaEntry.get()
                self.quit()
                with open('balance.txt', 'rb') as file:
                    balance = float(pickle.load(file))
                with open('balance.txt', 'wb') as file2:
                    pickle.dump(str(float(balance)+float(dep)/2), file2)
                return False
            else:
                self.labelZagruzka.configure(text='Сумма должна быть больше 0')
                self.labelZagruzka.place(x=150, y=210)
        if x == 1:
            self.after(100, self.send)
        else:
            self.after(1000, self.send)




def maiin():
    appDep = Deposit()
    appDep.mainloop()

def deposit():
    maiin()