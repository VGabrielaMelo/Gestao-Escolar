from tkinter import *
from tkinter.ttk import Treeview

from _Projeto_Alunos import Aluno


class AlunoAppLista:
    # titulo padrão da minha interface
    titulo = 'Lista de Alunos'

    # fonte padrão dos elementos da interface
    font = ('Verdana', 14)

    width = 10

    anchor = W

    def __init__(self, master=None):
        # armazenei em um atributo o container principal
        self.master = master

        self.master.title(AlunoAppLista.titulo)

        # criação do frame central para apresentar em tela os componentes, dentro do container principal
        # frame_master espaço vazio
        self.frame_master = Frame(self.master)
        self.frame_master.pack()

        # apresentar o titulo da interface
        # Segmentando as areas da interfca utiziando o container frame
        # frame do titulo
        self.frame_titulo = Frame(
            self.frame_master
        )

        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text=AlunoAppLista.titulo,
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
            columns=("Matricula", "Nome", "CPF", "Telefone", "E-mail"),
            show="headings"
        )

        # Declarando as colunas
        # Criando o cabeçalho da lista
        # Stretch = é o arrasta do cabeçalho da tabela
        self.lista.column(
            "Matricula",
            anchor=CENTER,
            width=200,
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
            width=200,
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
            width=200,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#3",
            text="CPF"
        )

        self.lista.column(
            "Telefone",
            anchor=CENTER,
            width=200,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#4",
            text="Telefone"
        )

        self.lista.column(
            "E-mail",
            anchor=CENTER,
            width=200,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#5",
            text="E-mail"
        )

        self.lista.pack()

        self.listar()

    def listar(self):
        lista_alunos = Aluno.listar()

        for aluno in lista_alunos:
            self.lista.insert(
                "",
                END,
                values=(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4]))


if __name__ == '__main__':
    root = Tk()

    AlunoAppLista(root)

    root.mainloop()

    # print(Aluno.listar())
