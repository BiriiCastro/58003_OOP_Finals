from tkinter import *

class MyButton:
    def __init__(self, win):
        self.btn1 = Button(win, text="Color", bg="blue", fg="red", command=self.ChangeColor)
        self.btn1.place(x=100, y=125)
        self.btn2 = Button(win, text="<---Click to change the color of the button")
        self.btn2.place(x=150, y=125)
        self.is_yellow = False

    def ChangeColor(self):
        if self.is_yellow:
            self.btn1.config(bg="blue")
            self.is_yellow = False
        else:
            self.btn1.config(bg="yellow")
            self.is_yellow = True


windows = Tk()
mywin = MyButton(windows)
windows.geometry("480x320+10+10")
windows.title("Button")
windows.mainloop()
