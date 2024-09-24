import flet as ft


def main (page: ft.Page):
    page.Title = 'Cadastro Rellatório'
    
    def cadastrar(e):
        print(produto.value)
        print(preco.value)
    txt_titulo = ft.Text('titulo do produto:')
    produto = ft.TextField(label="Digite o titulo do produto...", text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text('preço do produto')
    preco = ft.TextField(value="0", label="Digite o preço do produto", text_align=ft.TextAlign.LEFT)
    btn_produtos = ft.ElevatedButton('Cadastrar', on_click=cadastrar)
    
    page.add(
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_produtos
    )

ft.app(target=main)