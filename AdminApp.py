from tkinter import *
from _Projeto_Admin import Admin


class AdminApp:
    titulo = 'Gestão Escolar - Login'
    font = ('Verdana', 15)

    def __init__(self, master=None):
        self.master = master
        self.master.title(
            AdminApp.titulo
        )

        #
        self.frame_master = Frame(
            self.master
        )

        self.frame_master.pack()

        #
        self.frame_titulo = Frame(
            self.frame_master
        )
        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text='ÁREA RESTRITA',
            font=('Verdana', 25, 'bold')
        )
        self.label_titulo.pack()

        width = 10
        anchor = W

        # Formulario do aluno
        # Segmentou a área do formulario
        self.frame_formulario = Frame(
            self.frame_master
        )
        self.frame_formulario.pack()

        # LOGIN
        self.label_login = Label(
            self.frame_formulario,
            text='Usuário:',
            font=AdminApp.font,
            width=width,
            anchor=anchor
        )

        self.label_login.grid(
            row=0,
            column=0
        )

        self.entry_login = Entry(
            self.frame_formulario,
            font=AdminApp.font
        )

        self.entry_login.grid(
            row=0,
            column=1
        )

        # SENHA
        self.label_senha = Label(
            self.frame_formulario,
            text='Senha:',
            font=AdminApp.font,
            width=width,
            anchor=anchor
        )

        self.label_senha.grid(
            row=1,
            column=0
        )

        self.entry_nome = Entry(
            self.frame_formulario,
            font=AdminApp.font
        )

        self.entry_nome.grid(
            row=1,
            column=1
        )

        # Área de ferramentas
        self.frame_ferramentas = Frame(
            self.frame_master
        )

        self.frame_ferramentas.pack(
            fill=X
        )

        # Botão ENTRAR
        self.button_entrar = Button(
            self.frame_ferramentas,
            text='Entrar',
            font=AdminApp.font,
            background='Blue',
            foreground='White',
        )

        self.button_entrar.pack()


if __name__ == '__main__':
    root = Tk()
    AdminApp(root)
    mainloop()
