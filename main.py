import tkinter as tk
class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="calculator eiei", font=('Arial', 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="AC", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=10, y=40)

        self.button = tk.Button(self.root, text="+/-", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=80, y=40)

        self.button = tk.Button(self.root, text="%", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=150, y=40)

        self.button = tk.Button(self.root, text="/", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=220, y=40)

        self.button = tk.Button(self.root, text="7", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=10, y=95)

        self.button = tk.Button(self.root, text="8", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=80, y=95)

        self.button = tk.Button(self.root, text="9", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=150, y=95)

        self.button = tk.Button(self.root, text="*", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=220, y=95)

        self.button = tk.Button(self.root, text="4", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=10, y=150)

        self.button = tk.Button(self.root, text="5", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=80, y=150)

        self.button = tk.Button(self.root, text="6", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=150, y=150)

        self.button = tk.Button(self.root, text="-", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=220, y=150)

        self.button = tk.Button(self.root, text="1", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=10, y=205)

        self.button = tk.Button(self.root, text="2", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=80, y=205)

        self.button = tk.Button(self.root, text="3", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=150, y=205)

        self.button = tk.Button(self.root, text="+", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=220, y=205)

        self.button = tk.Button(self.root, text="0", height=2, width= 9, font=('Arial', 18))
        self.button.place(x=10, y=260)

        self.button = tk.Button(self.root, text=".", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=150, y=260)

        self.button = tk.Button(self.root, text="=", height=2, width= 3, font=('Arial', 18))
        self.button.place(x=220, y=260)

        self.root.mainloop()

MyCalculator()        
