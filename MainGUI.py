import tkinter
from tkinter import *
from tkinter import ttk
import http.client
import urllib.request
import xml.etree.ElementTree as ET
from PIL import Image, ImageTk
from io import BytesIO


# API 연결
server = "openapi.naver.com"
client_id = "7uMx_PsjI4ue2YoFX8j8"
client_secret = "kTKdhnM99E"


class MainGUI:
    def search_books(self):
        # 버튼 초기화
        for button in self.book_listbox.winfo_children():
            button.destroy()

        search_query = self.query_entry.get()
        conn = http.client.HTTPSConnection(server)
        encText = urllib.parse.quote(search_query)
        conn.request("GET", "/v1/search/book.xml?display=10&start=1&query="+encText, None,
                     {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
        req = conn.getresponse()
        print(req.status)
        if int(req.status) == 200:
            response_body = req.read()
            xml_root = ET.fromstring(response_body.decode('utf-8'))
            for item in xml_root.findall('.//item'):
                title = item.findtext('title')
                author = item.findtext('author')
                image = item.findtext('image')
                button = Button(self.book_listbox, text=title,
                                command=lambda t=title, a=author, i=image: self.display_book_info(t, a, i))
                button.pack(anchor='w')
            else:
                print("OpenAPI request has failed! Please retry")


    def display_book_info(self, title, author, image_url):
        # 버튼 초기화
        for button in self.book_listbox.winfo_children():
            button.destroy()

        try:
            # 책 이미지 다운로드
            image_data = urllib.request.urlopen(image_url).read()

            # 다운받은 이미지 TKinter에 맞게 변환
            image = ImageTk.PhotoImage(Image.open(BytesIO(image_data)))

            # 책 이미지 라벨 생성
            image_label = Label(self.book_listbox, image=image)
            image_label.image = image  # Store a reference to the image
            image_label.pack(side=LEFT)
        except Exception as e:
            print(f"Error loading image: {e}")

        info_label = Label(self.book_listbox, text=f"Title: {title}\nAuthor: {author}")
        info_label.pack(side=LEFT)

    def __init__(self):
        # API 연결
        server = "openapi.naver.com"
        client_id = "7uMx_PsjI4ue2YoFX8j8"
        client_secret = "kTKdhnM99E"

        # 윈도우 생성
        self.window = Tk()
        self.window.title('도서 탐색기')
        icon = tkinter.PhotoImage(file='Image/TUK.png')
        self.window.iconphoto(False, icon)

        # 탭 메뉴
        tab_menu = ttk.Notebook(self.window, width=800, height=600, style='TNotebook.Tab')
        tab_menu.pack()

        # 검색 탭
        search_tab = Frame(self.window)
        tab_menu.add(search_tab)

        search_img = tkinter.PhotoImage(file="Image/Search.png")
        tab_menu.tab(0, image=search_img, text=" Search ", compound=tkinter.LEFT)

        # 검색 입력 필드
        query_label = Label(search_tab, text="검색어 : ")
        query_label.pack(side=LEFT)

        self.query_entry = Entry(search_tab)
        self.query_entry.pack(side=LEFT)

        search_button = Button(search_tab, text="검색", command=self.search_books)
        search_button.pack(side=LEFT)

        # 책 목록 표시를 위한 Listbox
        self.book_listbox = Listbox(search_tab)
        self.book_listbox.pack(fill=BOTH, expand=True)

        # 즐겨찾기 탭
        favorite_tab = Frame(self.window)
        tab_menu.add(favorite_tab)

        favorite_img = tkinter.PhotoImage(file="Image/Favorite.png")
        tab_menu.tab(1, image=favorite_img, text=" Favorite ", compound=tkinter.LEFT)

        # 지도 탭
        map_tab = Frame(self.window)
        tab_menu.add(map_tab)

        map_img = tkinter.PhotoImage(file="Image/Map.png")
        tab_menu.tab(2, image=map_img, text=" Map ", compound=tkinter.LEFT)

        self.window.mainloop()


MainGUI()
