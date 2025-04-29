import flet as ft
from frontend.frontend import Tela

def main(page: ft.Page):
    app = Tela(page)
    app.paginaInicial()
    
#ft.app(target=main)
ft.app(target=main, port=4040, host="192.168.0.33", view=ft.WEB_BROWSER)