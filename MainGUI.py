from tkinter import *


class MainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('도서 탐색기')
        self.window.geometry('800x600')
        self.window.configure(bg='white')

        self.window.mainloop()


MainGUI()
