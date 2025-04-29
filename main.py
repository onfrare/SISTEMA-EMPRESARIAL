import flet as ft
from frontend.frontend import Tela

def main(page: ft.Page):
    app = Tela(page)
    app.paginaInicial()
    
ft.app(target=main)