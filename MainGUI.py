import tkinter
from tkinter import *
from tkinter import ttk


class MainGUI:
    def __init__(self):
        # 윈도우 생성
        self.window = Tk()
        self.window.title('도서 탐색기')

        # 탭 메뉴
        tab_menu = ttk.Notebook(self.window, width=800, height=600)
        tab_menu.pack()

        # 검색 탭
        search_tab = Frame(self.window)
        tab_menu.add(search_tab)

        search_img = tkinter.PhotoImage(file="Image/Search.png")
        tab_menu.tab(0, image=search_img, text="Search", compound=tkinter.LEFT)

        # 즐겨찾기 탭
        favorite_tab = Frame(self.window)
        tab_menu.add(favorite_tab, text="Favorite")

        favorite_img = tkinter.PhotoImage(file="Image/Favorite.png")
        tab_menu.tab(1, image=favorite_img, text="Favorite", compound=tkinter.LEFT)

        # 지도 탭
        map_tab = Frame(self.window)
        tab_menu.add(map_tab, text="Map")

        map_img = tkinter.PhotoImage(file="Image/Map.png")
        tab_menu.tab(2, image=map_img, text="Search", compound=tkinter.LEFT)

        self.window.mainloop()


MainGUI()
