from tkinter import *
from tkinter.ttk import Treeview

from _Projeto_Professor import Professor


class ProfessorAppLista:
    # titulo padrão da minha interface
    titulo = 'Lista de Professores'

    # fonte padrão dos elementos da interface
    font = ('Verdana', 14)

    width = 10

    anchor = W

    def __init__(self, master=None):
        self.master = master

        self.master.title(
            ProfessorAppLista.titulo
        )

        self.frame_master = Frame(
            self.master
        )
        self.frame_master.pack(
        )

        self.frame_titulo = Frame(
            self.frame_master
        )

        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text=ProfessorAppLista.titulo,
            font=('Verdana', 30, 'bold')
        )

        self.label_titulo.pack()

        self.frame_lista = Frame(
            self.frame_master
        )

        self.frame_lista.pack()

        self.lista = Treeview(
            self.frame_lista,
            selectmode="browse",
            columns=("Matricula", "Nome", "CPF", "Ativo", "Telefone", "E-mail", "Formação", "Especialidade"),
            show="headings"
        )

        # Declarando as colunas
        # Criando o cabeçalho da lista
        # Stretch = é o arrasta do cabeçalho da tabela
        self.lista.column(
            "Matricula",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#1",
            text="Matricula"
        )

        self.lista.column(
            "Nome",
            anchor=CENTER,
            width=150,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#2",
            text="Nome"
        )

        self.lista.column(
            "CPF",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#3",
            text="CPF"
        )

        self.lista.column(
            "Ativo",
            anchor=CENTER,
            width=50,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#4",
            text="Ativo"
        )

        self.lista.column(
            "Telefone",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#5",
            text="Telefone"
        )

        self.lista.column(
            "E-mail",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#6",
            text="E-mail"
        )

        self.lista.column(
            "Formação",
            anchor=CENTER,
            width=150,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#7",
            text="Formação"
        )

        self.lista.column(
            "Especialidade",
            anchor=CENTER,
            width=150,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#8",
            text="Especialidade"
        )

        self.lista.pack()

        self.listar()

    def listar(self):
        lista_professor = Professor.listar()

        for professor in lista_professor:
            professor_status = "Ativo" if professor[3] == 1 else "Inativo"
            self.lista.insert(
                "",
                END,
                values=(professor[0],
                        professor[1],
                        professor[2],
                        professor_status,
                        professor[4],
                        professor[5],
                        professor[6],
                        professor[7]))


if __name__ == '__main__':
    root = Tk()

    ProfessorAppLista(root)

    root.mainloop()
