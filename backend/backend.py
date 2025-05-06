import flet as ft
import requests
import socket
import re

def obterIP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80)) 
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return None

def somenteNumero(evento: ft.ControlEvent):
    evento.control.value = ''.join(filter(str.isdigit, evento.control.value))
    evento.control.update()


def formatarTelefone(evento: ft.ControlEvent):
    valorNumerico = ''.join(filter(str.isdigit, evento.control.value))[:11]
    telefoneFormatado = valorNumerico
    if len(valorNumerico) == 11:
        telefoneFormatado = f"({valorNumerico[:2]}) {valorNumerico[2:7]}-{valorNumerico[7:]}"
    elif len(valorNumerico) >= 7:
        telefoneFormatado = f"({valorNumerico[:2]}) {valorNumerico[2:6]}-{valorNumerico[6:]}"
    elif len(valorNumerico) >= 3:
        telefoneFormatado = f"({valorNumerico[:2]}) {valorNumerico[2:]}"
    
    if len(valorNumerico) >= 10 or len(valorNumerico) == 0:
        evento.control.error_text = None
    else:
        evento.control.error_text = "Número de telefone inválido"
    evento.control.value = telefoneFormatado
    evento.page.update()


def validarCnpj(evento, campoNome, campoFantasia, campoCep, campoRua, campoNumero, campoBairro, campoCidade, campoUf):
    cnpj = ''.join(filter(str.isdigit, evento.control.value))[:14]
    evento.control.value = cnpj

    if len(cnpj) != 14:
        evento.control.error_text = "CNPJ incompleto"
        evento.page.update()
        return

    try:
        resposta = requests.get(
            f"https://www.receitaws.com.br/v1/cnpj/{cnpj}",
            headers={"Accept": "application/json"}
        )
        dados = resposta.json()

        if "erro" in dados or dados.get("status") == "ERROR":
            evento.control.error_text = "CNPJ inválido ou não encontrado"
        else:
            evento.control.error_text = ""
            campoNome.value = dados.get("nome", "").upper()
            campoFantasia.value = dados.get("fantasia", "").upper()
            campoCep.value = dados.get("cep", "").replace(".", "").replace("-", "")
            campoRua.value = dados.get("logradouro", "").upper()
            campoNumero.value = dados.get("numero", "")
            campoBairro.value = dados.get("bairro", "").upper()
            campoCidade.value = dados.get("municipio", "").upper()
            campoUf.value = dados.get("uf", "").upper()

            # CNPJ formatado
            evento.control.value = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
    except:
        evento.control.error_text = "Erro ao consultar o CNPJ"

    evento.page.update()

def validarEmail(evento: ft.ControlEvent):
    email = evento.control.value
    if email == "":
        evento.control.error_text = None
        evento.page.update()
        return
    padraoEmail = r'^[^@]+@[^@]+\.[^@]+$'
    if re.match(padraoEmail, email):
        evento.control.error_text = None
    else:
        evento.control.error_text = "E-mail inválido"
    evento.page.update()

