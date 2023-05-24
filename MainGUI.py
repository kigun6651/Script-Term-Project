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
        tab_menu.add(search_tab, text="Search")

        # 즐겨찾기 탭
        favorite_tab = Frame(self.window)
        tab_menu.add(favorite_tab, text="Favorite")

        # 지도 탭
        map_tab = Frame(self.window)
        tab_menu.add(map_tab, text="Map")

        self.window.mainloop()


MainGUI()
