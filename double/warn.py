import tkinter.messagebox as mb

def warn(num, text):
    msg = f"Произошла ошибка #{num}:\n {text}"
    mb.showwarning("Предупреждение", msg)

def warn1(num, text):
    msg = f"Уведомление #{num}:\n {text}"
    mb.showwarning("Поздравляем!", msg)

def soon():
    mb.showwarning("Приносим извинение", "Данный режим еще в разработке.")