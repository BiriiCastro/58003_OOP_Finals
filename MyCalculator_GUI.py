from tkinter import *


class MyCalculator:
    def __init__(self, win):
        # Create display field
        self.entry = Entry(win, width=18, font=("", 20))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        self.btn_7 = Button(win, text="7", width=5, height=2, command=lambda: self.append_to_expression("7"))
        self.btn_7.grid(row=1, column=0, padx=5, pady=5)
        self.btn_8 = Button(win, text="8", width=5, height=2, command=lambda: self.append_to_expression("8"))
        self.btn_8.grid(row=1, column=1, padx=5, pady=5)
        self.btn_9 = Button(win, text="9", width=5, height=2, command=lambda: self.append_to_expression("9"))
        self.btn_9.grid(row=1, column=2, padx=5, pady=5)
        self.btn_div = Button(win, text="/", width=5, height=2, command=lambda: self.append_to_expression("/"))
        self.btn_div.grid(row=1, column=3, padx=5, pady=5)

        self.btn_4 = Button(win, text="4", width=5, height=2, command=lambda: self.append_to_expression("4"))
        self.btn_4.grid(row=2, column=0, padx=5, pady=5)
        self.btn_5 = Button(win, text="5", width=5, height=2, command=lambda: self.append_to_expression("5"))
        self.btn_5.grid(row=2, column=1, padx=5, pady=5)
        self.btn_6 = Button(win, text="6", width=5, height=2, command=lambda: self.append_to_expression("6"))
        self.btn_6.grid(row=2, column=2, padx=5, pady=5)
        self.btn_mul = Button(win, text="*", width=5, height=2, command=lambda: self.append_to_expression("*"))
        self.btn_mul.grid(row=2, column=3, padx=5, pady=5)

        self.btn_1 = Button(win, text="1", width=5, height=2, command=lambda: self.append_to_expression("1"))
        self.btn_1.grid(row=3, column=0, padx=5, pady=5)
        self.btn_2 = Button(win, text="2", width=5, height=2, command=lambda: self.append_to_expression("2"))
        self.btn_2.grid(row=3, column=1, padx=5, pady=5)
        self.btn_3 = Button(win, text="3", width=5, height=2, command=lambda: self.append_to_expression("3"))
        self.btn_3.grid(row=3, column=2, padx=5, pady=5)
        self.btn_sub = Button(win, text="-", width=5, height=2, command=lambda: self.append_to_expression("-"))
        self.btn_sub.grid(row=3, column=3, padx=5, pady=5)

        self.btn_clear = Button(win, text="C", width=5, height=2, command=self.clear_expression)
        self.btn_clear.grid(row=4, column=0, padx=5, pady=5)
        self.btn_0 = Button(win, text="0", width=5, height=2, command=lambda: self.append_to_expression("0"))
        self.btn_0.grid(row=4, column=1, padx=5, pady=5)
        self.btn_dot = Button(win, text=".", width=5, height=2, command=lambda: self.append_to_expression("."))
        self.btn_dot.grid(row=4, column=2, padx=5, pady=5)
        self.btn_add = Button(win, text="+", width=5, height=2, command=lambda: self.append_to_expression("+"))
        self.btn_add.grid(row=4, column=3, padx=5, pady=5)

        self.btn_equals = Button(win, text="=", width=11, height=2, command=self.evaluate_expression)
        self.btn_equals.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.btn_exit = Button(win, text="Exit", width=11, height=2, command=win.quit)
        self.btn_exit.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

    # Value of the buttons
    def append_to_expression(self, char):
        self.entry.insert(END, char)

    # To clear the display
    def clear_expression(self):
        self.entry.delete(0, END)

    # To calculate the expression entered
    def evaluate_expression(self):
        expression = self.entry.get()
        try:
            result = eval(expression)
            self.entry.delete(0, END)
            self.entry.insert(END, str(result))
        except:
            self.entry.delete(0, END)
            self.entry.insert(END, "Error")


windows = Tk()
windows.title("Calculator")
my_calculator = MyCalculator(windows)
windows.mainloop()
