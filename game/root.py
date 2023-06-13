import sys
from tkinter import *
from PIL import ImageTk, Image
import pickle
from deposit import deposit
from conclusion import conclusson
from warn import soon

def GoCrash():
    sys.path.insert(0, '../crash/py')
    import main
    main.restart()

def GoMines():
    sys.path.insert(0, '../mine')
    import main2
    main2.restart()

def GoDouble():
    sys.path.insert(0, '../double')
    import main3
    main3.restart()

def ubn():
    global label_bal
    with open('balance.txt', 'rb') as file:
        balance = float(pickle.load(file))
    label_bal.configure(text='Ваш баланс {}$'.format((round(balance,2))))
    root.protocol("WM_DELETE_WINDOW", lambda: quit())
    root.after(1000,ubn)


root = Tk()
root.geometry('510x475')
root.resizable(False, False)

imageCrash = ImageTk.PhotoImage(file="img\crash.png")
Button(root, image=imageCrash, relief = 'flat', command=GoCrash).place(x=20, y=250)



imageMines = ImageTk.PhotoImage(file="img\mines.png")
Button(root, image=imageMines, relief = 'flat',pady=10, padx=10, command=GoMines).place(x=180, y=250)

with open('balance.txt', 'rb') as file:
    balance = float(pickle.load(file))



depositImage = ImageTk.PhotoImage(file="img\deposit.png")
button_dep = Button(image=depositImage, relief='flat',  background='#f0f0f0', activebackground='#f0f0f0', height=40, width=190, command=deposit).place(x=283,y=121)

label_bal = Label(text='Ваш баланс {}$'.format((round(balance,2))), font=('Comic Sans MS', 12, 'bold'))
label_bal.place(x=300,y=30)
ubn()

conclusionImage = ImageTk.PhotoImage(file="img\conclusion.png")
button_conclusion = Button(image=conclusionImage, relief='flat',  background='#f0f0f0', activebackground='#f0f0f0', height=45, width=190, command=conclusson).place(x=280,y=65)

logoimage = ImageTk.PhotoImage(file="img\logo.png")
nameLabee = Label(image=logoimage, height=140, width=210,background='#f0f0f0').place(x=30, y=30)

deathwing=Image.open('img\double.png')
image2=deathwing.resize((150,185),Image.ANTIALIAS)
doubleimage=ImageTk.PhotoImage(image2)

doubleLabee = Button(image=doubleimage, relief = 'flat',pady=10, padx=10,background='#f0f0f0', command=GoDouble).place(x=340, y=248)


labelchange = Label(text='Выберите режим:', font=('Comic Sans MS', 15, 'bold')).place(x=155, y=190)


root.mainloop()