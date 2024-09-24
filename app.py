import flet as ft


def main (page: ft.Page):
    page.Title = 'Cadastro Rellatório'
    
    txt_titulo = ft.Text('titulo do produto:')
    produto = ft.TextField(label="Digite o titulo do produto...", text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text('preço do produto')
    preco = ft.TextField(value="0", label="Digite o preço do produto", text_)
    
    page.add(
        txt_titulo
    )

ft.app(target=main)