import random
from tkinter import *
import tkinter as tk
import pickle
from PIL import ImageTk
import deposit
import sys

from warn import warn

xxx = 0
print(xxx)
class Vibor(Tk):
    def __init__(self):

        super().__init__()
        # self.imgDEPOSIT = ImageTk.PhotoImage(file="../crash/img/btn_deposit.png")
        self.geometry(f'200x340')
        self.title('Выбор')
        self.resizable(False, False)

        try:
            with open('../game/balance.txt', 'rb') as file1:
                self.balance = float(pickle.load(file1))
                self.balance = round(self.balance, 2)
        except:
            with open('balance.txt', 'rb') as file1:
                self.balance = float(pickle.load(file1))
                self.balance = round(self.balance, 2)
        self.start()



    def start(self):
        global x1
        x = 50
        y = 95
        x1 = None
        try:
            self.deposit = Button(self, font=('Comic Sans MS', 10, 'bold'), command=deposit.maiin, text='+', width=3,
                              height=1).place(
            x=10, y=10)
        except:
            pass
        self.deposit = Button(
                              # text='+',a
                              # command=deposit.maiin,
                              # relief='flat',
                              # background='#f0f0f0',
                              # # width=26,
                              # # height=26,
                              # # activebackground='#f0f0f0'
                              )
        self.deposit.place(x=17, y=10)
        self.deposit.destroy()
        self.labelBalance = Label(self, font=('Comic Sans MS', 12, 'bold'),fg='green', text='Баланс {}$'.format(self.balance))
        self.labelBalance.place(x=52, y=11)

        self.label1 = Label(self, font=('Comic Sans MS', 15, 'bold'), text='Ячеек:')
        self.label1.place(x=70, y=50)
        self.btnyac1 = Button(self,font=('Comic Sans MS', 9, 'bold'), bg='LightGray', text='9', command=self.ok9)
        self.btnyac1.place(x=x-5,y=y)
        self.btnyac2 = Button(self, font=('Comic Sans MS', 9, 'bold'), bg='LightGray',text='16', command=self.ok16)
        self.btnyac2.place(x=x+20,y=y)
        self.btnyac3 = Button(self, font=('Comic Sans MS', 9, 'bold'), bg='LightGray',text='25', command=self.ok25)
        self.btnyac3.place(x=x+50,y=y)
        self.btnyac4 = Button(self, font=('Comic Sans MS', 9, 'bold'), bg='LightGray',text='36', command=self.ok36)
        self.btnyac4.place(x=x+80,y=y)

        self.label2 = Label(self, font=('Comic Sans MS', 15, 'bold'), text='Мины:').place(x=x+12,y=y+35)
        self.entry2 = Entry(self)
        self.entry2.place(x=x-11,y=y+78)
        self.label3 = Label(self, font=('Comic Sans MS', 15, 'bold'), text='Ставка:').place(x=x+10,y=y+105)
        self.entry3 = Entry(self)
        self.entry3.place(x=x-11,y=y+147)
        self.btnStart = Button(self, font=('Comic Sans MS', 15, 'bold'), command=self.go, text='Старт').place(x=x+60,y=y+180)

        self.BTNNazad = Button(self, font=('Comic Sans MS', 15, 'bold'), command=self.nazad, text='Назад').place(x=x-30,y=y+180)

    def ok9(self):
        global x1
        x1 = 9
        self.btnyac1.configure(bg='gray')
        self.btnyac2.configure(bg='LightGray')
        self.btnyac3.configure(bg='LightGray')
        self.btnyac4.configure(bg='LightGray')


    def ok16(self):
        global x1
        x1 = 16
        self.btnyac2.configure(bg='gray')
        self.btnyac1.configure(bg='LightGray')
        self.btnyac3.configure(bg='LightGray')
        self.btnyac4.configure(bg='LightGray')

    def ok25(self):
        global x1
        x1 = 25
        self.btnyac3.configure(bg='gray')
        self.btnyac2.configure(bg='LightGray')
        self.btnyac1.configure(bg='LightGray')
        self.btnyac4.configure(bg='LightGray')

    def ok36(self):
        global x1
        x1 = 36
        self.btnyac4.configure(bg='gray')
        self.btnyac2.configure(bg='LightGray')
        self.btnyac3.configure(bg='LightGray')
        self.btnyac1.configure(bg='LightGray')

    def go(self):
        global game
        global x1
        global x2
        global x3
        if x1 == 9 or x1 == 16 or x1 == 25 or x1 == 36:
            pass
        else:
            warn(45,'Вы не выбрали количество ячеек')
        try:
            x2 = int(self.entry2.get())
        except:
            warn(104,'Вы не выбрали количество мин')
        try:
            x3 = float(self.entry3.get())
        except:
            warn(103, 'Вы не ввели ставку')

        if x3 < 0.1:
            warn(762, 'Минимальная ставка - 0.1$')

        if x2 < x1 and x2 != 0 and game == False and self.balance-x3 >= 0 and x3 > 0.09:
            try:
                with open('../game/balance.txt', 'rb') as file1:
                    self.balance -= float(self.entry3.get())
                    self.balance = round(self.balance, 2)
                with open('../game/balance.txt', 'wb') as file2:
                    pickle.dump(str(self.balance), file2)
            except:
                with open('balance.txt', 'rb') as file1:
                    self.balance -= float(self.entry3.get())
                    self.balance = round(self.balance, 2)
                with open('balance.txt', 'wb') as file2:
                    pickle.dump(str(self.balance), file2)
            self.labelBalance.configure(text='Баланс {}$'.format(self.balance))
            root = Root()
            root.mainloop()
        else:
            if x2 >= x1:
                warn(93, 'Мин не может быть больше или столько же, сколько и полей.')
            if x2 == 0:
                warn(81, 'На поле должна быть хотябы 1 мина.')
            if game == True:
                warn(34, 'Игра уже запущена.')
            if self.balance - x3 < 0:
                warn(68, 'Не хватает баланса.')







    def nazad(self):
        if game == False:
            self.destroy()
        else:
            warn(48, 'Выполнить действие не возможно: Идет игра')

class Root(Tk):
    def __init__(self):
        global game
        game = True
        super().__init__()
        self.resizable(False, False)
        self.title('Мины')
        self.protocol("WM_DELETE_WINDOW", self.closing)
        self.draw()

    def draw(self):
        global x1
        global x2
        global x3
        self.col_vo = x1
        print(self.col_vo)
        self.count_mines = x2
        self.stavka = x3
        self.schet = self.stavka
        self.mines_here = [i for i in range(1,self.col_vo+1)]
        random.shuffle(self.mines_here)

        self.col_vo = self.col_vo**0.5
        self.root_size = int(self.col_vo*100+190)
        self.geometry(f'{self.root_size}x{self.root_size}')
        num = 0
        x = 100
        y = 150
        self.schetlb = Label(self, font=('Comic Sans MS', 15, 'bold'),text='Ставка:{}$'.format(self.schet))
        self.schetlb.place(x=(self.root_size-150)/2,y=70)
        print(self.mines_here)

        self.colors = ['blue', 'white', 'green', 'yellow','purple','purple','white', 'green', 'yellow','pink']
        self.mines = []
        self.buttons=[]
        self.nor1m = []
        for j in range(int(self.col_vo)):
            for i in range(int(self.col_vo)):
                if self.mines_here[num] <= self.count_mines:
                    self.buttons.append(Button(self, width=11,height=5, bg='gray', command=self.mine))
                    self.mines.append(num)
                else:
                    self.buttons.append(Button(self, width=11,height=5, bg='gray', command=self.norm))
                    self.nor1m.append(num)
                num += 1

        print(self.buttons)


        o = 0
        for j in range(int(self.col_vo)):
            for i in range(int(self.col_vo)):
                self.buttons[o].place(x=x, y=y)
                x += 100
                o += 1
            y += 100
            x = 100


    def closing(self):
        global game
        game = False
        self.destroy()


    def norm(self):
#----------------
        self.schet = (self.stavka/(float((x1-x2)/x1)))
#------------------
        self.schetlb.configure(text='Вы угадали! выйгрыш {}'.format(round(self.schet),3), fg='green')
        try:
            with open('../game/balance.txt', 'rb') as file7:
                balanceq = float(pickle.load(file7))
            self.balance = float(balanceq) + float(self.schet)

            with open('../game/balance.txt', 'wb') as file8:
                pickle.dump(str(self.balance), file8)
        except:
            with open('balance.txt', 'rb') as file7:
                balanceq = float(pickle.load(file7))
            self.balance = float(balanceq) + float(self.schet)

            with open('balance.txt', 'wb') as file8:
                pickle.dump(str(self.balance), file8)

        vibor.labelBalance.configure(text='Баланс {}$'.format(round(self.balance),2))


        self.schetlb.place(x=(self.root_size - 240) / 2, y=70)
        for i in self.nor1m:
            self.buttons[i].configure(bg='green',state='disabled')
            for i in self.mines:
                self.buttons[i].configure(state='disabled')

    def mine(self):
        self.schet = 0
        self.schetlb.configure(text='Вы наткнулись на мину!(',fg='red')
        self.schetlb.place(x=(self.root_size-240)/2,y=70)
        for i in self.mines:
            self.buttons[i].configure(bg='red')




def main2():
    global vibor
    global game
    game = False
    vibor = Vibor()
    vibor.mainloop()


def restart():
    import os
    current_dir = os.getcwd()
    print(current_dir)
    main2()

if __name__ == '__main__':
    main2()
