import flet as ft

class Tela:
    
    def __init__(self, page: ft.Page):
        self.page = page
        modoEscuro = self.page.platform_brightness.value == "dark"
        self.corFundo = ft.colors.WHITE if modoEscuro else ft.colors.BLACK
        self.corTexto = ft.colors.BLACK if modoEscuro else ft.colors.WHITE
        self.objetos()

    def objetos(self):
        
        self.btnCadastroCliente = ft.ElevatedButton(
            text="Cadastrar Cliente",
            on_click =lambda e : self.TelacadastroCliente(), 
            bgcolor = self.corFundo,
            color = self.corTexto,
            icon = ft.Icons.PERSON_ADD_ALT_ROUNDED,
            width = 200)
        
        self.btnCadastroFornecedor = ft.ElevatedButton(
            text="Cadastrar Fornecedor",
            on_click =lambda e : self.TelacadastroFornecedor(), 
            bgcolor = self.corFundo,
            color = self.corTexto,
            icon = ft.Icons.PERSON_ADD_ALT_ROUNDED,
            width = 200)
        
        self.btnCadastroProduto = ft.ElevatedButton(
            text="Cadastrar Produto",
            on_click =lambda e : self.TelacadastroProduto(),
            bgcolor = self.corFundo,
            color = self.corTexto,
            icon = ft.Icons.ADD_SHOPPING_CART,
            width = 200)
        
        self.btnGerarPedido = ft.ElevatedButton(
            text="Pedido",
            on_click =lambda e : self.TelagerarPedido(), 
            bgcolor = self.corFundo,
            color = self.corTexto,
            icon = ft.Icons.ASSIGNMENT_ADD,
            width = 200)
    
        self.btnGerarOrcamento = ft.ElevatedButton(
            text="Orçamento",
            on_click =lambda e : self.TelagerarOrcamento(), 
            bgcolor = self.corFundo,
            color = self.corTexto,
            icon = ft.Icons.ASSIGNMENT_ADD,
            width = 200)
        
        self.btnGerarAmostra = ft.ElevatedButton(
            text="Amostra",
            on_click =lambda e : self.TelagerarAmostra(), 
            bgcolor = self.corFundo,
            color = self.corTexto,
            icon = ft.Icons.ASSIGNMENT_ADD,
            width = 200)
        
        self.colunaEsquerdaTelaPrincipal = ft.Column(
            controls=[self.btnCadastroCliente, self.btnCadastroFornecedor, self.btnCadastroProduto],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20)
        
        self.colunaDireitaTelaPrincipal = ft.Column(
            controls=[self.btnGerarPedido, self.btnGerarOrcamento, self.btnGerarAmostra],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20)

        self.btnTelaInicial = ft.ElevatedButton(
            text="Voltar para tela inicial",
            on_click =lambda e : self.paginaInicial(), 
            bgcolor = self.corFundo,
            color = self.corTexto,
            icon = ft.Icons.HOME,
            width = 200)
        
        
        
    def btn(self, botao=None, local=ft.FloatingActionButtonLocation.START_TOP):
        if botao is None:
            botao = self.btnTelaInicial
        self.page.floating_action_button = botao
        self.page.floating_action_button_location = local
        

    
    def configurarJanela(self, titulo: str, largura: int, altura: int, redimensionavel: bool = False):
        self.page.clean()
        self.page.title = titulo
        self.page.window.width = largura
        self.page.window.height = altura
        self.page.window.center()
        self.page.window.resizable = redimensionavel
        self.page.window.maximizable = False
        self.page.window.minimized = False
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def paginaInicial(self):
        self.configurarJanela("Nome da Empresa", 1000, 600)
        self.page.floating_action_button = None
        
        self.page.add(ft.Row(
                controls=[self.colunaEsquerdaTelaPrincipal ,self.colunaDireitaTelaPrincipal],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20))

    def TelacadastroCliente(self):
        self.configurarJanela("Cadastro de cliente", 1000, 600)
        self.btn()
        self.page.add(ft.Text("Tela de cadastro de cliente",bgcolor=self.corFundo ,color = self.corTexto))
