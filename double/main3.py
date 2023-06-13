import time
import pickle
from tkinter import *
import random
import deposit
from PIL import ImageTk, Image
import pyautogui
from warn import warn
import os


class Main(Tk):
    def __init__(self):
        global canvas
        global pra
        global x
        super().__init__()
        self.geometry('600x450')
        self.const()
        self.overrideredirect(True)
        self.colour = {
            'red': 0,
            'black': 0,
            'lime': 0
        }
        x = 600
        y = 300
        canvas_verh = Canvas(self, bg='yellow', width=606,height=100)
        canvas_verh.place(x=0,y=0)
        self.knowBalance()
        self.wm_geometry("+%d+%d" % (x, y))
        canvas = Canvas(self, bg='#FFEBCD', width=605,height=700)
        canvas.place(x=-5,y=-100)
        canvas.create_polygon(285, 255+pra, 300, 290+pra, 315, 255+pra, fill='gray')
        canvas.create_polygon(285, 355+pra, 300, 320+pra, 315, 355+pra, fill='gray')
        canvas_verh = Canvas(self, bg='white', width=606, height=79)
        canvas_verh.create_rectangle(0,0,606,80, fill='yellow')
        canvas_verh.place(x=-5, y=-5)

        self.BTNNazad = Button(self, font=('Comic Sans MS', 15, 'bold'), command=self.nazad, text='Назад')
        self.BTNNazad.place(x=10, y=10)
        self.titlegame = Label(self, text='Режим Double', font=('Comic Sans MS', 19, 'bold'), bg='yellow')
        canvas_verh.create_line(100, 66, 285, 66)
        self.BTNNazad.configure(state='normal')

        self.btn_stavka_allIn = Button(self, text='Max', font=('Comic Sans MS', 11, 'normal'), bg='white', command=self.allIn)
        self.btn_stavka_allIn.place(x=215,y=278)
        self.latscolor()
        self.titlegame.place(x=100,y=18)
        self.quardsCoordinate()
        self.timeOnStart = 10
        try:
            self.stavkibtn()
        except:
            pass
        self.timer = Label(self, text='До прокрута: {}'.format(self.timeOnStart), font=('Comic Sans MS', 14, 'bold'), bg='#FFEBCD')
        self.timer.place(x=220, y=110+pra)
        self.timerFun()


    def allIn(self):
        self.allIn1 = True


    def latscolor(self):
        text1 = 0
        text2 = 0
        text3 = 0
        text4 = 0
        text5 = 0
        text6 = 0
        text7 = 0
        text8 = 0
        text9 = 0
        text10 = 0

        with open('../double/txt/history.txt', 'r') as file:
            canvas.create_rectangle(280,350,590,420, fill='#AFEEEE')
            Label(self, text='Last colors:',font=('Comic Sans MS', 14, 'bold'),bg='#AFEEEE').place(x=360,y=252)
            text = file.read()
            text = text.split()
            for i in range(1,11):
                text10 = text9
                text9 = text8
                text8 = text7
                text7 = text6
                text6 = text5
                text5 = text4
                text4 = text3
                text3 = text2
                text2 = text1
                text1 = text[-i]
        last10 = canvas.create_rectangle(290,390,310,410,fill=text10)
        last9 = canvas.create_rectangle(320,390,340,410, fill=text9)
        last8 = canvas.create_rectangle(350, 390, 370, 410, fill=text8)
        last7 = canvas.create_rectangle(380, 390, 400, 410, fill=text7)
        last6 = canvas.create_rectangle(410, 390, 430, 410, fill=text6)
        last5 = canvas.create_rectangle(440, 390, 460, 410, fill=text5)
        last4 = canvas.create_rectangle(470, 390, 490, 410, fill=text4)
        last3 = canvas.create_rectangle(500, 390, 520, 410, fill=text3)
        last2 = canvas.create_rectangle(530, 390, 550, 410, fill=text2)
        last1 = canvas.create_rectangle(560, 390, 580, 410, fill=text1)



    def stavkibtn(self):
        global pra
        self.labelblack = Label(self, text='{}$'.format(self.colour['black']), font=('Comic Sans MS', 14, 'bold'),
                                bg='#FFEBCD')
        self.labelblack.place(x=430, y=410 + pra)
        self.labelred = Label(self, text='{}$'.format(self.colour['red']), font=('Comic Sans MS', 14, 'bold'),
                              bg='#FFEBCD')
        self.labelred.place(x=50, y=410 + pra)
        self.labellime = Label(self, text='{}$'.format(self.colour['lime']), font=('Comic Sans MS', 14, 'bold'),
                                bg='#FFEBCD')
        self.labellime.place(x=240, y=410 + pra)
        self.stavkaobn()
        self.vvod = Label(self, text='Ставка              $', font=('Comic Sans MS', 14, 'bold'), bg='#FFEBCD')
        self.vvod.place(x=15,y=280)
        self.entryStavka = Entry(self, font=('Comic Sans MS', 14, 'bold'), width=7)
        self.entryStavka.place(x=90,y=280)
        self.btnStavkaRed = Button(self,text='Red 2x', font=('Comic Sans MS', 14, 'bold'),bg='red', fg='white', width=10, command=self.stavkared)
        self.btnStavkaRed.place(x=50,y=360+pra)
        self.btnStavkaBlack = Button(self, text='Black 2x', font=('Comic Sans MS', 14, 'bold'),bg='black', fg='white', width=10, command=self.stavkablack)
        self.btnStavkaBlack.place(x=420, y=360+pra)
        self.btnStavkalime = Button(self, text='lime 14x', font=('Comic Sans MS', 14, 'bold'),bg='#00FF00', fg='white', width=10, command=self.stavkalime)
        self.btnStavkalime.place(x=235, y=360+pra)


    def stavkaobn(self):
        self.labelblack.configure(text='{}$'.format(self.colour['black']))
        self.labelred.configure(text='{}$'.format(self.colour['red']))
        self.labellime.configure(text='{}$'.format(self.colour['lime']))
        self.after(100,self.stavkaobn)


    def stavkared(self):
        self.stavka = self.entryStavka.get()
        if self.allIn1 == True:
            self.stavka = self.balance
        try:
            self.stavka = float(self.stavka)
        except:
            warn(54, 'Ставка должна быть числом.')
        self.allIn1 = False
        if float(self.stavka) > 0 and float(self.stavka) <= self.balance:
            self.BTNNazad.configure(state='disabled')
        if (self.balance - float(self.stavka)) >= 0:
            if float(self.stavka) >= 0.1:
                with open('../game/balance.txt', 'rb') as file5:
                    self.balance = float(pickle.load(file5))
                    self.balance = round(self.balance, 2)
                self.balance -= float(self.stavka)
                with open('../game/balance.txt', 'wb') as file1:
                    pickle.dump(str(self.balance), file1)
                self.colour['red'] += float(self.stavka)
            else:
                warn(91, 'Минимальная ставка - 0.1$')
        else:
            warn(92, 'Недостаточно баланса')

    def stavkablack(self):
        self.stavka = self.entryStavka.get()
        try:
            self.stavka = float(self.stavka)
        except:
            warn(54, 'Ставка должна быть числом.')
        if float(self.stavka) > 0 and float(self.stavka) <= self.balance:
            self.BTNNazad.configure(state='disabled')
        if (self.balance - float(self.stavka)) >= 0:
            if float(self.stavka) >= 0.1:
                with open('../game/balance.txt', 'rb') as file:
                    self.balance = float(pickle.load(file))
                    self.balance = round(self.balance, 2)
                self.balance -= float(self.stavka)
                with open('../game/balance.txt', 'wb') as file2:
                    pickle.dump(str(self.balance), file2)
                self.colour['black'] += float(self.stavka)
            else:
                warn(91, 'Минимальная ставка - 0.1$')
        else:
            warn(92, 'Недостаточно баланса')


    def stavkalime(self):
        self.stavka = self.entryStavka.get()
        try:
            self.stavka = float(self.stavka)
        except:
            warn(54, 'Ставка должна быть числом.')
        if float(self.stavka) > 0 and float(self.stavka) <= self.balance:
            self.BTNNazad.configure(state='disabled')
        if (self.balance - float(self.stavka)) >= 0:
            if float(self.stavka) >= 0.1:
                with open('../game/balance.txt', 'rb') as file3:
                    self.balance = float(pickle.load(file3))
                    self.balance = round(self.balance, 2)
                self.balance -= float(self.stavka)
                with open('../game/balance.txt', 'wb') as file4:
                    pickle.dump(str(self.balance), file4)
                self.colour['lime'] += float(self.stavka)
            else:
                warn(91, 'Минимальная ставка - 0.1$')
        else:
            warn(92, 'Недостаточно баланса')



    def nazad(self):
        self.destroy()


    def timerFun(self):
        self.depositbtn = Button(self, font=('Comic Sans MS', 12, 'bold'), command=deposit.maiin, text='+', width=3,height=1)
        self.depositbtn.place(x=350, y=20)
        if self.timeOnStart >-1:
            self.timer.configure(text='До прокрута: {}'.format(self.timeOnStart))
        self.timeOnStart -=1
        if self.timeOnStart == -1 :
            self.startgame()
        self.after(1000, self.timerFun)


    def knowBalance(self):
            with open('../game/balance.txt', 'rb') as file6:
                self.balance = float(pickle.load(file6))
                self.balance = round(self.balance, 2)
            self.labnelBal = Label(self, font=('Comic Sans MS', 13, 'bold'), text='Ваш баланс: {}$'.format(self.balance), bg='yellow')
            self.labnelBal.place(x=400, y=27)
            self.after(100,self.knowBalance)

    def const(self):
        global pra
        pra = -20
        global j
        self.l = 0
        self.kk = 100
        j = 0


    def quardsCoordinate(self):
        global pra

        self.random = random.randint(200,20000)
        self.x = -79977 - self.random
        self.y = 280+pra
        self.r = 50
        self.create()


    def create(self):
        global pra
        for i in range(400):
            for i in range(1,15):
                if i%2 == 0:
                    canvas.create_rectangle(self.x, self.y,self.x+self.r,self.y+self.r, fill='black')
                else:
                    canvas.create_rectangle(self.x, self.y, self.x + self.r, self.y + self.r, fill='red')
                self.x+=50
            canvas.create_rectangle(self.x, self.y, self.x + self.r, self.y + self.r, fill='#00FF00')
            self.x += 50
            canvas.create_polygon(285, 255+pra, 300, 290+pra, 315, 255+pra, fill='gray')
            canvas.create_polygon(285, 355+pra, 300, 320+pra, 315, 355+pra, fill='gray')

    def startgame(self):
        global canvas
        global pra
        global j
        self.btnStavkaRed.configure(state='disabled')
        self.btnStavkaBlack.configure(state='disabled')
        self.btnStavkalime.configure(state='disabled')

        canvas.delete(ALL)
        if self.kk <= 25:
            self.kk -= random.choice([i / 10 for i in range(1, 3)])
        else:
            self.kk-=random.choice([i/10 for i in range(3,6)])
        self.l+=self.kk
        self.x = -79977-self.random+self.l
        self.create()
        self.latscolor()
        if self.kk >= 0:
            self.after(5, self.startgame)
        else:

            self.latscolor()
            x = str((pyautogui.pixel(895, 488)))

            if x == '(0, 0, 0)':
                self.result = 'black'
                self.colour['black'] *= 2
                self.okras()

            elif x == '(255, 0, 0)':
                self.result = 'red'
                self.colour['red'] *= 2
                self.okras()
            else:
                self.result = 'lime'
                self.colour['lime'] *= 14
                self.okras()
            print(self.result)
            self.procEnd()
            self.end1 = 0
            self.end()

    def okras(self):
        if self.result == 'black':
            self.labelblack.configure(fg='lime')
            self.labelred.configure(fg='red')
            self.labellime.configure(fg='red')
        if self.result == 'red':
            self.labelred.configure(fg='lime')
            self.labelblack.configure(fg='red')
            self.labellime.configure(fg='red')
        if self.result == 'lime':
            self.labellime.configure(fg='lime')
            self.labelred.configure(fg='red')
            self.labelblack.configure(fg='red')
        self.after(1,self.okras)
    def end(self):
        if self.end1 == 1:
            with open('../double/txt/history.txt', 'a')as fileHistory:
                fileHistory.write('{}\n'.format(self.result))
            self.destroy()
            main()
            return
        self.end1+=1
        self.after(3000,self.end)

    def procEnd(self):
        for i in self.colour:
            if i == self.result:
                if self.result == 'lime':
                    self.balance += float(self.colour[i] * 14)
                else:
                    self.balance += float(self.colour[i])
        with open('../game/balance.txt', 'wb') as file7:
            pickle.dump(str(self.balance), file7)

def main():
    root = Main()
    root.mainloop()

def restart():
    main()

if __name__ == '__main__':
    main()
