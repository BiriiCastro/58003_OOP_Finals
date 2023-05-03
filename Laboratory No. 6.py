from tkinter import *


class Table:
    def __init__(self):
        self.frame = Frame(windows, bg="cyan")
        self.frame.grid(row=0, column=0, pady=100, padx=120)

        self.header1 = Label(self.frame, text="a", bg="cyan")
        self.header1.grid(row=0, column=0, padx=30)
        self.header2 = Label(self.frame, text="a^2", bg="cyan")
        self.header2.grid(row=0, column=1, padx=30)
        self.header3 = Label(self.frame, text="a^3", bg="cyan")
        self.header3.grid(row=0, column=2, padx=30)

    def table_body(self):
        for i in range(1, 5):
            body1 = Label(self.frame, text=str(i), bg="cyan")
            body1.grid(row=i, column=0)
            body2 = Label(self.frame, text=str(i ** 2), bg="cyan")
            body2.grid(row=i, column=1)
            body3 = Label(self.frame, text=str(i ** 3), bg="cyan")
            body3.grid(row=i, column=2)


windows = Tk()
mywin = Table()
mywin.table_body()
windows.geometry("480x360+50+50")
windows.title("Rock Paper Scissor Game")
windows.configure(background="cyan")
windows.mainloop()
