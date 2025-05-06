import flet as ft
import backend.backend as be

class Tela:
    
    def __init__(self, page: ft.Page):
        self.page = page
        modoEscuro = self.page.platform_brightness.value == "dark"
        self.corFundo = ft.colors.WHITE if modoEscuro else ft.colors.BLACK
        self.corTexto = ft.colors.BLACK if modoEscuro else ft.colors.WHITE
        self.objetos()

    def objetos(self):
        self.btnCadastroCliente = self.criarBotao("Cadastrar Cliente", ft.Icons.PERSON_ADD_ALT_ROUNDED, self.TelacadastroCliente)
        self.btnCadastroFornecedor = self.criarBotao("Cadastrar Fornecedor", ft.Icons.PERSON_ADD_ALT_ROUNDED, self.TelacadastroFornecedor)
        self.btnCadastroProduto = self.criarBotao("Cadastrar Produto", ft.Icons.ADD_SHOPPING_CART, self.TelacadastroProduto)
        self.btnGerarPedido = self.criarBotao("Pedido", ft.Icons.ASSIGNMENT_ADD, self.TelagerarPedido)
        self.btnGerarOrcamento = self.criarBotao("Orçamento", ft.Icons.ASSIGNMENT_ADD, self.TelagerarOrcamento)
        self.btnGerarAmostra = self.criarBotao("Amostra", ft.Icons.ASSIGNMENT_ADD, self.TelagerarAmostra)
        self.btnTelaInicial = self.criarBotao("Voltar para tela inicial", ft.Icons.HOME, self.paginaInicial)

        self.ctxCadastroNome = ft.TextField(label="Nome", width=650,capitalization=ft.TextCapitalization.CHARACTERS)
        self.ctxCadastroFantasia = ft.TextField(label="Nome Fantasia", width=300,capitalization=ft.TextCapitalization.CHARACTERS)
        self.ctxCadastroCnpj = ft.TextField(label="CNPJ", width=300, keyboard_type=ft.KeyboardType.NUMBER, on_change=lambda e: be.validarCnpj(e, self.ctxCadastroNome, self.ctxCadastroFantasia, self.ctxCadastroCep, self.ctxCadastroRua, self.ctxCadastroNumero, self.ctxCadastroBairro, self.ctxCadastroCidade, self.ctxCadastroUf))
        self.ctxCadastroIe = ft.TextField(label="IE", width=300,capitalization=ft.TextCapitalization.CHARACTERS)
        
        self.ctxCadastroCep= ft.TextField(label="CEP", width=300,capitalization=ft.TextCapitalization.CHARACTERS)
        self.ctxCadastroRua= ft.TextField(label="Rua", width=300,capitalization=ft.TextCapitalization.CHARACTERS)
        self.ctxCadastroNumero= ft.TextField(label="Número", width=300,on_change=be.somenteNumero)
        self.ctxCadastroBairro= ft.TextField(label="Bairro", width=300,capitalization=ft.TextCapitalization.CHARACTERS)
        self.ctxCadastroCidade= ft.TextField(label="Cidade", width=300,capitalization=ft.TextCapitalization.CHARACTERS)
        self.ctxCadastroUf= ft.TextField(label="UF", width=300,capitalization=ft.TextCapitalization.CHARACTERS)
    
        self.ctxCadastroTelefone= ft.TextField(label="Telefone", width=300,on_change=be.formatarTelefone)
        self.ctxCadastroEmail = ft.TextField(label="Email", width=300,on_change=be.validarEmail,capitalization=ft.TextCapitalization.CHARACTERS)
        self.ctxCadastroContato = ft.TextField(label="Contato", width=300, capitalization=ft.TextCapitalization.CHARACTERS)
        
        self.bntConfirmarCadastroCliente = ft.ElevatedButton(text="Cadastrar", width=650)

        self.colunaEsquerdaTelaPrincipal = ft.Column(controls=
            [self.btnCadastroCliente, self.btnCadastroFornecedor, self.btnCadastroProduto],
                alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=20)

        self.colunaDireitaTelaPrincipal = ft.Column(controls=
            [self.btnGerarPedido, self.btnGerarOrcamento, self.btnGerarAmostra],
                alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=20)

        self.colunaEsquerdaCadastroCliente = ft.Column(controls=[
            self.ctxCadastroCnpj,self.ctxCadastroCep,self.ctxCadastroNumero,
            self.ctxCadastroBairro,self.ctxCadastroUf,self.ctxCadastroTelefone],
            alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=20)
        
        self.colunaDireitaCadastroCliente = ft.Column(controls=[
            self.ctxCadastroFantasia,self.ctxCadastroIe,self.ctxCadastroRua,self.ctxCadastroCidade,
            self.ctxCadastroEmail,self.ctxCadastroContato],
            alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=20)
            
        self.containerCadastroCliente = ft.Container(content=
        ft.Column(controls=[ft.Row(controls=[self.ctxCadastroNome], 
        alignment=ft.MainAxisAlignment.CENTER), ft.Column(controls=
        [ft.Row(controls=[self.colunaEsquerdaCadastroCliente, self.colunaDireitaCadastroCliente], 
        alignment=ft.MainAxisAlignment.CENTER, spacing=50)]),ft.Row(controls=[self.bntConfirmarCadastroCliente], 
        alignment=ft.MainAxisAlignment.CENTER)]), padding=20)

   
    def criarBotao(self, texto, icone=None, acao=None):
        return ft.ElevatedButton(
            text=texto,
            on_click=lambda e: acao(),
            bgcolor=self.corFundo,
            color=self.corTexto,
            icon=icone,
            icon_color=self.corTexto,
            style=ft.ButtonStyle(text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            width=200
        )

    def configurarPosiçãoBtn(self, botao=None, local=ft.FloatingActionButtonLocation.START_TOP):
        if botao is None:
            botao = self.btnTelaInicial

        self.page.floating_action_button_location = local
        
        if str(local).endswith("TOP"): 
            self.page.floating_action_button = ft.Container(content=botao,margin=ft.margin.only(top=20))
        else:
            self.page.floating_action_button = ft.Container(content=botao,margin=ft.margin.only(bottom =20))
        
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
        self.configurarPosiçãoBtn()
        self.page.add(self.containerCadastroCliente)
        

    def TelacadastroFornecedor(self):
        self.configurarJanela("Cadastro de fornecedor", 1000, 600)
        self.configurarPosiçãoBtn()
        self.page.add(ft.Text("Tela de cadastro de fornecedor",color=self.corFundo))

    def TelacadastroProduto(self):
        self.configurarJanela("Cadastro de produto", 1000, 600)
        self.configurarPosiçãoBtn()
        self.page.add(ft.Text("Tela de cadastro de produto",color=self.corFundo))

    def TelagerarPedido(self):
        self.configurarJanela("Gerar pedido", 1000, 600)
        self.configurarPosiçãoBtn()
        self.page.add(ft.Text("Tela de gerar pedido",color=self.corFundo))

    def TelagerarOrcamento(self):
        self.configurarJanela("Gerar orçamento", 1000, 600)
        self.configurarPosiçãoBtn()
        self.page.add(ft.Text("Tela de gerar orçamento",color=self.corFundo))

    def TelagerarAmostra(self):
        self.configurarJanela("Gerar amostra", 1000, 600)
        self.configurarPosiçãoBtn()
        self.page.add(ft.Text("Tela de gerar amostra",color=self.corFundo))
