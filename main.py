import flet as ft
from frontend.frontend import Tela
import backend.backend as be


def main(page: ft.Page):
    app = Tela(page)
    app.paginaInicial()
    
ft.app(target=main, port=4040, host=be.obterIP(), view=ft.WEB_BROWSER)