from tkinter import *
from tkinter import messagebox

timer = None


def delete_text():
    messagebox.showerror(title="Oops", message="Say bye-bye to your text :(")
    text.delete(1.0, END)


def writing(key):
    global timer
    try:
        window.after_cancel(timer)
    except ValueError:
        pass
    timer = window.after(300000, delete_text)


window = Tk()
window.title('Disappearing text app')

start_label = Label(text="Type here: ")
start_label.pack()

text = Text(width=80, height=40)
text.focus()
text.pack()

window.bind_all('<Key>', writing)

window.mainloop()
