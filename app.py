import flet as ft
from models import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///projeto1.db"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def main(page: ft.Page):
    page.Title = 'Cadastro Relatório'
    lista_produtos = ft.ListView()

    # Função para cadastrar novo produto
    def cadastrar(e):
        novo_produto = Produto(titulo=produto.value, preco=preco.value)
        session.add(novo_produto)
        session.commit()

        # Adicionar na lista da interface
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(produto.value),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
            )
        )
        page.update()
        print("Produto salvo com sucesso")

    # Função para deletar produto
    def deletar(e):
        produto_existente = session.query(Produto).filter_by(titulo=produto.value).first()

        if produto_existente:
            session.delete(produto_existente)
            session.commit()
            print("Produto removido do banco de dados")

            # Remover da interface
            for i, control in enumerate(lista_produtos.controls):
                if isinstance(control.content, ft.Text) and control.content.value == produto.value:
                    lista_produtos.controls.pop(i)
                    break

            page.update()
        else:
            print("Produto não encontrado")

    # Elementos da interface
    txt_titulo = ft.Text('Título do produto:')
    produto = ft.TextField(label="Digite o título do produto...", text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text('Preço do produto:')
    preco = ft.TextField(value="0", label="Digite o preço do produto", text_align=ft.TextAlign.LEFT)
    btn_produtos = ft.ElevatedButton('Cadastrar', on_click=cadastrar)
    btn_deletar = ft.ElevatedButton('Deletar', on_click=deletar)

    # Adicionando elementos à página
    page.add(
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_produtos,
        btn_deletar,
    )

    # Carregar produtos já cadastrados
    for p in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(p.titulo),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
            )
        )

    page.add(lista_produtos)

ft.app(target=main)
