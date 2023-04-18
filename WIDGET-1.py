from tkinter import *

windows = Tk()

frame = Frame()

Label(frame,text="Laboratory Activity 5").grid(row=1, column=0)
Label(frame,text="Submitted to: Mam Sayo").grid(row=2, column=0)

frame.pack(expand=True)

windows.geometry("480x320+20+20")
windows.title("Text Field")
windows.mainloop()