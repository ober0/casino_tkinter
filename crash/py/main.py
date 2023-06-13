import logic
import time
import deposit
import pickle
import sys

from PIL import Image, ImageTk

from tkinter import Tk, Label, Button, mainloop
from tkinter import *
from threading import Thread
import tkinter as tk
import tkinter.messagebox as mb

x = 0
bal = 0
balance = 0

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x430')                                                 #инициализация и параметры окна
        self.resultStavka = 0



        self.resizable(width=True, height=True)
        global balance
        self.last = [0, 0, 0, 0, 0]
        try:
            with open('../txt/historyCrash.txt', 'r') as histor1:
                self.last = (histor1.read().split())
                self.y = 1
        except:
            with open('../crash/txt/historyCrash.txt', 'r') as histor1:
                self.last = (histor1.read().split())
                self.y = 1
        self.auto = 0
        self.autostart = False
        self.q = True


        #------------------------------------------------------------------------------Основные элементы---------------------------------------------------------------------------------------------------

        self.label = Label(self,
                           text="x 1.00",
                           font=('Comic Sans MS', 20, 'bold'),
                           pady=40,
                           padx=100
                           )

        self.label.place(x=180, y=75)

        self.button = Button(self,
                             font=('Comic Sans MS', 15, 'bold'),
                             bg='black',
                             fg='white',
                             text='Забрать!',
                             command=self.stop_game,
                             width=8,
                             height=1,
                             borderwidth=2,
                             relief="groove"
                             )
        self.button.place(x=150,y=200)

        self.button1 = Button(self,
                             font=('Comic Sans MS', 15, 'bold'),
                             bg='black',
                             fg='white',
                             text='Начать',
                             command=self.game_on,
                             borderwidth=2,
                             relief="groove",
                             width=8,
                             height=1
                             )
        self.button1.place(x=280,y=200)

        Label(self,
                text="Введите ставку:",
                font=('Comic Sans MS', 15, 'bold'),
                pady=40,
                padx=100
              ).place(x=50,y=250)

        self.stavka_vvod = Entry(self,
                                 background='white',
                                 justify='center',
                                 width=10,
                                 font=('Comic Sans MS', 13, 'bold')
                                 )
        self.btn_stavka_vvod = Button(self,
                                     font=('Comic Sans MS', 12, 'bold'),
                                     bg='black',
                                     fg='white',
                                     text='Выбрать!',
                                     borderwidth=1,
                                     relief="sunken",
                                     underline=-1,
                                     width=8,
                                     pady=1,
                                     command=self.player_stavka
                                     )
        self.stavka_vvod.place(x=320,y=295)
        self.btn_stavka_vvod.place(x=440,y=290)

        self.btn_skip = Button(self,
                                     font=('Comic Sans MS', 15, 'bold'),
                                     bg='black',
                                     fg='white',
                                     text='Пропустить!',
                                     borderwidth=2,
                                     relief="groove",
                                     underline=-1,
                                     width=10,
                                     height=1,
                                     command=self.skipcrash
                                     )
        self.btn_skip.place(x=410, y=200)

        self.autolabel = Label(self,
                               text="Авто-вывод: {}x".format(self.auto),
                               font=('Comic Sans MS', 15, 'bold')
                               )
        self.autolabel.place(x=10, y=350)

        self.btnAuto1_2x = Button(self,
                                  text='1.2x',
                                  font=('Comic Sans MS', 11, 'bold'),
                                  command=self.auto12x
                                  )
        self.btnAuto1_2x.place(x=210,y=350)

        self.btnAuto1_5x = Button(self,
                                  text='1.5x',
                                  font=('Comic Sans MS', 11, 'bold'),
                                  command=self.auto15x
                                  )
        self.btnAuto1_5x.place(x=270, y=350)

        self.btnAuto2x = Button(self,
                                  text='2x',
                                  font=('Comic Sans MS', 11, 'bold'),
                                  command=self.auto2x
                                  )
        self.btnAuto2x.place(x=330, y=350)

        self.btnAuto5x = Button(self,
                                  text='5x',
                                  font=('Comic Sans MS', 11, 'bold'),
                                  command=self.auto5x
                                  )
        self.btnAuto5x.place(x=370, y=350)

        Label(self,
              text="Или",
              font=('Comic Sans MS', 15, 'bold')
              ).place(x=410, y=350)

        self.svoy_auto = Entry(self,
                                 background='white',
                                 justify='right',
                                 width=5,
                                 font=('Comic Sans MS', 13, 'bold')
                                 )
        self.svoy_auto.place(x=460, y=355)

        Label(self,
              text="x",
              font=('Comic Sans MS', 15, 'bold')
              ).place(x=514, y=350)

        self.btnSvoy_auto = Button(self,
                                text='ОК',
                                font=('Comic Sans MS', 12, 'bold'),
                                command=self.autosvoy,

                                )
        self.btnSvoy_auto.place(x=540, y=350)

        upStr2 = Canvas(self, width=110, height=119, bg='white')
        upStr2.place(x=420,y=75)
        upStr2.create_rectangle(2, 2, 110, 119, fill='#87CEEB')

        self.summaVivod = Label(self,
                                text=f'0$ \n ↓ \n0$',
                                font=('Comic Sans MS', 15, 'bold'),
                                bg='#87CEEB'
                                )
        self.summaVivod.place(x=460, y=90)


        #---------------------------------------------------------Верх страницы--------------------------------------------------------------------------------------

        upStr = Canvas(self, width=600, height=70, bg='white')
        upStr.place(x=0, y=0)
        upStr.create_rectangle(0, 0, 600, 70, fill='yellow')

        self.label_bal = Label(self, text='Ваш баланс {}$'.format(balance),font=('Comic Sans MS', 14, 'normal'), bg='yellow')
        self.label_bal.place(x=390, y=20)

        self.name = Label(self, text='РЕЖИМ CRASH',font=('Comic Sans MS', 20, 'normal'), bg='yellow')
        self.name.place(x=100,y=15)

        self.BTNNazad = Button(self, font=('Comic Sans MS', 15, 'bold'), command=self.nazad, text='Назад').place(
            x=10, y=10)

        self.deposit = Button(self, font=('Comic Sans MS', 14, 'bold'), command=deposit.maiin, text='+', width=3, height=1).place(
            x=340, y=15)
        self.deposit = Button(
            # text='1',
            # command=deposit.maiin,
            # relief='flat',
            # background='yellow',
            # width=30,
            # height=30,
            # activebackground='yellow'
        )

        self.deposit.place(x=320, y=18)
        self.deposit.destroy()
        self.btn_skip.configure(state='disabled')
        self.button.configure(state='disabled')
        # ----------------------------------------------------------История игр-------------------------------------------------------------------------------------------

        upStr1 = Canvas(self, width=80, height=170, bg='white')
        upStr1.place(x=20,y=140)
        upStr1.create_rectangle(2,2, 80,170, fill='#C7FCEC')

        Label(self, text='История игр',font=('Comic Sans MS', 12, 'normal')).place(x=10, y=105)

        self.history1 = Label(self,text='',bg='#C7FCEC',font=('Comic Sans MS', 12, 'bold'))
        self.history1.place(x=40, y=150)
        self.history2 = Label(self,text='',bg='#C7FCEC', font=('Comic Sans MS', 12, 'bold'))
        self.history2.place(x=40, y=180)
        self.history3 = Label(self,text='',bg='#C7FCEC', font=('Comic Sans MS', 12, 'bold'))
        self.history3.place(x=40, y=210)
        self.history4 = Label(self,text='',bg='#C7FCEC', font=('Comic Sans MS', 12, 'bold'))
        self.history4.place(x=40, y=240)
        self.history5 = Label(self,text='',bg='#C7FCEC', font=('Comic Sans MS', 12, 'bold'))
        self.history5.place(x=40, y=270)
        self.nachaloHistory()


    def nachaloHistory(self):
        self.history1.configure(text=self.last[4])
        self.history2.configure(text=self.last[3])
        self.history3.configure(text=self.last[2])
        self.history4.configure(text=self.last[1])
        self.history5.configure(text=self.last[0])


    def restartHistoryCrash(self):

        self.last[0] = self.last[1]
        self.last[1] = self.last[2]
        self.last[2] = self.last[3]
        self.last[3] = self.last[4]
        self.last[4] = self.lastCrash

        self.history1.configure(text=self.last[4])
        self.history2.configure(text=self.last[3])
        self.history3.configure(text=self.last[2])
        self.history4.configure(text=self.last[1])
        self.history5.configure(text=self.last[0])


        try:
            with open('../txt/historyCrash.txt', 'w') as histor:
                for i in self.last:
                    histor.write(f'{str(i)}\n')
        except:
            with open('../crash/txt/historyCrash.txt', 'w') as histor:
                for i in self.last:
                    histor.write(f'{str(i)}\n')


        if self.last[4] <= 1.2:
            self.history1.configure(fg='#E66761')
        elif self.last[4] > 1.2 and self.last[4] <= 2.0:
            self.history1.configure(fg='#4169E1')
        elif self.last[4] > 2 and self.last[4] <= 5:
            self.history1.configure(fg='#59ED54')
        elif self.last[4] > 5 and self.last[4] < 10:
            self.history1.configure(fg='#F754E1')
        else:
            self.history1.configure(fg='#CFB53B')

        if self.last[3] <= 1.2:
            self.history2.configure(fg='#E66761')
        elif self.last[3] > 1.2 and self.last[3] <= 2.0:
            self.history2.configure(fg='#4169E1')
        elif self.last[3] > 2 and self.last[3] <= 5:
            self.history2.configure(fg='#59ED54')
        elif self.last[3] > 5 and self.last[3] < 10:
            self.history2.configure(fg='#F754E1')
        else:
            self.history2.configure(fg='#CFB53B')

        if self.last[2] <= 1.2:
            self.history3.configure(fg='#E66761')
        elif self.last[2] > 1.2 and self.last[2] <= 2.0:
            self.history3.configure(fg='#4169E1')
        elif self.last[2] > 2 and self.last[2] <= 5:
            self.history3.configure(fg='#59ED54')
        elif self.last[2] > 5 and self.last[2] < 10:
            self.history3.configure(fg='#F754E1')
        else:
            self.history3.configure(fg='#CFB53B')

        if self.last[1] <= 1.2:
            self.history4.configure(fg='#E66761')
        elif self.last[1] > 1.2 and self.last[1] <= 2.0:
            self.history4.configure(fg='#4169E1')
        elif self.last[1] > 2 and self.last[1] <= 5:
            self.history4.configure(fg='#59ED54')
        elif self.last[1] > 5 and self.last[1] < 10:
            self.history4.configure(fg='#F754E1')
        else:
            self.history4.configure(fg='#CFB53B')

        if self.last[0] <= 1.2:
            self.history5.configure(fg='#E66761')
        elif self.last[0] > 1.2 and self.last[0] <= 2.0:
            self.history5.configure(fg='#4169E1')
        elif self.last[0] > 2 and self.last[0] <= 5:
            self.history5.configure(fg='#59ED54')
        elif self.last[0] > 5 and self.last[0] < 10:
            self.history5.configure(fg='#F754E1')
        else:
            self.history5.configure(fg='#CFB53B')

    def nazad(self):
        self.destroy()


    def colour(self):

        self.history1.configure(text=self.last[4])
        self.history2.configure(text=self.last[3])
        self.history3.configure(text=self.last[2])
        self.history4.configure(text=self.last[1])
        self.history5.configure(text=self.last[0])

        if self.last[4] <= 1.2:
            self.history1.configure(fg='#E66761')
        elif self.last[4] > 1.2 and self.last[4] <= 2.0:
            self.history1.configure(fg='#4169E1')
        elif self.last[4] > 2 and self.last[4] <= 5:
            self.history1.configure(fg='#59ED54')
        elif self.last[4] > 5 and self.last[4] < 10:
            self.history1.configure(fg='#F754E1')
        else:
            self.history1.configure(fg='#CFB53B')

        if self.last[3] <= 1.2:
            self.history2.configure(fg='#E66761')
        elif self.last[3] > 1.2 and self.last[3] <= 2.0:
            self.history2.configure(fg='#4169E1')
        elif self.last[3] > 2 and self.last[3] <= 5:
            self.history2.configure(fg='#59ED54')
        elif self.last[3] > 5 and self.last[3] < 10:
            self.history2.configure(fg='#F754E1')
        else:
            self.history2.configure(fg='#CFB53B')

        if self.last[2] <= 1.2:
            self.history3.configure(fg='#E66761')
        elif self.last[2] > 1.2 and self.last[2] <= 2.0:
            self.history3.configure(fg='#4169E1')
        elif self.last[2] > 2 and self.last[2] <= 5:
            self.history3.configure(fg='#59ED54')
        elif self.last[2] > 5 and self.last[2] < 10:
            self.history3.configure(fg='#F754E1')
        else:
            self.history3.configure(fg='#CFB53B')

        if self.last[1] <= 1.2:
            self.history4.configure(fg='#E66761')
        elif self.last[1] > 1.2 and self.last[1] <= 2.0:
            self.history4.configure(fg='#4169E1')
        elif self.last[1] > 2 and self.last[1] <= 5:
            self.history4.configure(fg='#59ED54')
        elif self.last[1] > 5 and self.last[1] < 10:
            self.history4.configure(fg='#F754E1')
        else:
            self.history4.configure(fg='#CFB53B')

        if self.last[0] <= 1.2:
            self.history5.configure(fg='#E66761')
        elif self.last[0] > 1.2 and self.last[0] <= 2.0:
            self.history5.configure(fg='#4169E1')
        elif self.last[0] > 2 and self.last[0] <= 5:
            self.history5.configure(fg='#59ED54')
        elif self.last[0] > 5 and self.last[0] < 10:
            self.history5.configure(fg='#F754E1')
        else:
            self.history5.configure(fg='#CFB53B')

    # ----------------------------------------------------------Ход игры в деньгах-------------------------------------------------------------------------------------------

    def pokazstavki(self, x):
        self.summaVivod.configure(text=f'{self.stavka}$ \n ↓ \n{x}$', )
        if self.stavka < 10:
            self.summaVivod.place(x=450, y=90)
        if self.stavka >= 10 and self.stavka < 100:
            self.summaVivod.place(x=435, y=90)
        if self.stavka >= 100:
            self.summaVivod.place(x=428, y=90)


    # ----------------------------------------------------------СОХРАНЕНИЕ СТАВКИ-------------------------------------------------------------------------------------------

    def player_stavka(self):
        self.stavka = float(self.stavka_vvod.get())


    # ----------------------------------------------------------Запуск по кнопке начать-------------------------------------------------------------------------------------------

    def game_on(self):
        global balance

        logic.random_crash()    #запуск скрипта для краша
        self.summaVivod.configure(fg='black')
        self.targ = 0
        self.now = 1.00         #переменные ддля краша
        self.sum_plus = 0.01

        self.q = True
        self.win = False        #При запуске игры нет не победы не поражения
        self.loses = False
        self.skip = False
        self.btn_skip.configure(state='disabled')

        # Обработка ставки
        if self.stavka == '':
            self.warn(76,'Вы не ввели ставку')
        else:
            if balance >= self.stavka:
                self.game = True
                self.button1.configure(state='disabled')
                self.btn_stavka_vvod.configure(state='disabled')
                self.button.configure(state='normal')
                balance -= self.stavka
                self.label_bal['text'] = 'Ваш баланс {}$'.format((round(balance,2)))
                try:
                    with open('../../game/balance.txt', 'wb') as file2:
                        pickle.dump(str(balance), file2)
                except:
                    with open('balance.txt', 'wb') as file2:
                        pickle.dump(str(balance), file2)
                self.game_start()

            elif balance-int(self.stavka) < 0:
                self.label['text'] = 'Нет баланса'
                self.label.place(x=130, y=75)
                self.game = False

    # ----------------------------------------------------------Авто-стоп-------------------------------------------------------------------------------------------

    def auto12x(self):
        self.autostart = True
        self.auto = 1.2
        self.autolabel.configure(text="Авто-вывод: {}x".format(self.auto))
    def auto15x(self):
        self.autostart = True
        self.auto = 1.5
        self.autolabel.configure(text="Авто-вывод: {}x".format(self.auto))
    def auto2x(self):
        self.autostart = True
        self.auto = 2
        self.autolabel.configure(text="Авто-вывод: {}x".format(self.auto))
    def auto5x(self):
        self.autostart = True
        self.auto = 5
        self.autolabel.configure(text="Авто-вывод: {}x".format(self.auto))
    def autosvoy(self):
        self.autostart = True
        self.auto = float(self.svoy_auto.get())
        self.autolabel.configure(text="Авто-вывод: {}x".format(self.auto))
    # --------------------------------------------Запуск игры при условии пройденных проверок и обработки ставки--------------------------------------------------------------------


    def game_start(self):

        try:
            if self.now < logic.num:
                self.now += self.sum_plus
                self.now = round(self.now, 2)
        except:
            pass

        if self.targ == 0:
            self.label.configure(text='x {}'.format(self.now))
        try:
            if self.now <= 2:
                self.after(80, self.game_start)

            elif self.now > 2 and self.now < 5:
                self.after(60, self.game_start)
                self.sum_plus = 0.02
            elif self.now >= 5 and self.now <= 20:
                self.after(40, self.game_start)                          #изменение скорости краша
                self.sum_plus = 0.05
            elif self.now > 20 and self.now <= 100:
                self.after(10, self.game_start)
                self.sum_plus = 0.1
            elif self.now > 100:
                self.after(1, self.game_start)
                self.sum_plus = 0.2
            else:
                pass
        except:
            pass


        try:

            if self.win == False and self.loses == False:
                self.pokazstavki(round(self.now*self.stavka, 2))
            if self.win == True and self.q == True:
                self.pokazstavki(round(self.now*self.stavka ,2))
                self.summaVivod.configure(fg='green')
                self.q = False

        except:
            pass

        try:
            if self.now >= self.auto and self.autostart == True:       #авто вывод
                self.stop_game()
                self.autostart = False
        except:
            pass
        if self.skip == True:
            self.after(self.speedskip, self.game_start)
            self.sum_plus = 0.2
        try:
            if self.now >= logic.num:
                self.now1 = self.now
                self.loses = True
                self.now = 'Crash!'                                   #Обработка краша(конца игры)
                self.label.configure(text='{}'.format(self.now))
                self.targ = 1
                self.loses = True

                if self.loses == True and self.q == True:
                    self.pokazstavki(round(self.now1 * self.stavka, 2))
                    self.summaVivod.configure(fg='red')
                    self.q = False
                self.end()
        except:
            pass

        if self.y == 1:
            self.colour()
            self.y = 0


    # ----------------------------------------------------------Скип прокрут-------------------------------------------------------------------------------------------



    def skipcrash(self):
        self.skip = True

        self.speedskip = 10  #изменить скорость скипа

    # ----------------------------------------------------------Забрать ставку-------------------------------------------------------------------------------------------

    def stop_game(self):
        global balance
        if self.game == True:
            balance += (float(self.stavka)*self.now)
            try:
                with open('../../game/balance.txt', 'wb') as file2:
                    pickle.dump(str(balance), file2)
            except:
                with open('balance.txt', 'wb') as file2:
                    pickle.dump(str(balance), file2)
        self.label_bal['text'] = 'Ваш баланс {}$'.format(round(balance,2))
        if self.now < logic.num:
            self.win = True
            self.button.configure(state='disabled')

            self.btn_skip.configure(state='normal')


    # ----------------------------------------------------------Окончание игры-------------------------------------------------------------------------------------------


    def end(self):
        self.button1.configure(state='normal')
        self.autolabel.configure(text="Авто-вывод: 0x")
        self.btn_skip.configure(state='disabled')
        self.btn_stavka_vvod.configure(state='normal')
        self.lastCrash = logic.num
        self.restartHistoryCrash()
        self.loses = False
        self.skip = False


    def warn(self,num, error):
        msg = f"Произошла ошибка #{num}:\n {error}"
        mb.showwarning("Предупреждение", msg)



    # ----------------------------------------------------------Основная функция(Вывод баланса, создание окна игры)-------------------------------------------------------------------------------------------

def main():
    global balance
    global statelabelInfo
    try:
        with open('../../game/balance.txt', 'rb') as file1:
            balance = float(pickle.load(file1))
            balance = round(balance,2)
    except:
        with open('balance.txt', 'rb') as file1:
            balance = float(pickle.load(file1))
            balance = round(balance,2)
    app = App()
    app.mainloop()

    # ----------------------------------------------------------Для пополнения-------------------------------------------------------------------------------------------

def hi(dep):
    global x
    bal1 = dep
    x += 1
    if x >= 2:
        try:
            with open('../../game/balance.txt', 'rb') as fileq:
                balanceq = float(pickle.load(fileq))
        except:
            with open('balance.txt', 'rb') as fileq:
                balanceq = float(pickle.load(fileq))
        bal = float(bal1) + balanceq

        try:
            with open('../../game/balance.txt', 'wb') as fileqq:
                pickle.dump(str(bal), fileqq)
        except:
            with open('balance.txt', 'wb') as fileqq:
                pickle.dump(str(bal), fileqq)
    # ----------------------------------------------------------Запуск-------------------------------------------------------------------------------------------
def restart():
    import os
    current_dir = os.getcwd()
    main()

if __name__ == '__main__':
    import os
    current_dir = os.getcwd()
    main()


