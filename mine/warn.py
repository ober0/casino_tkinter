import tkinter.messagebox as mb

def warn(num, warmmsg):
    msg = f"Произошла ошибка #{num}:\n {warmmsg}"
    mb.showwarning("Предупреждение", msg)