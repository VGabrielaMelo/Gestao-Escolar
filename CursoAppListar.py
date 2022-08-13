from tkinter import *
from tkinter.ttk import Treeview

from _Projeto_Cursos import Cursos


class CursoAppListar:
    titulo = "Lista dos Cursos"
    font = ('Verdana', 14)

    width = 10

    anchor = W

    def __init__(self, master=None):
        self.master = master

        self.master.title(
            CursoAppListar.titulo
        )

        self.frame_master = Frame(
            self.master
        )
        self.frame_master.pack()

        self.frame_titulo = Frame(
            self.frame_master
        )

        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text=CursoAppListar.titulo,
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
            columns=("Código", "Nome", "Ativo", "Classificação", "Descrição"),
            show="headings"
        )

        self.lista.column(
            "Código",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#1",
            text="Código"
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
            "Ativo",
            anchor=CENTER,
            width=200,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#3",
            text="Ativo"
        )

        self.lista.column(
            "Classificação",
            anchor=CENTER,
            width=200,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#4",
            text="Classificação"
        )

        self.lista.column(
            "Descrição",
            anchor=CENTER,
            width=200,
            minwidth=50,
            stretch=NO
        )

        self.lista.heading(
            "#5",
            text="Descrição"
        )

        self.lista.pack()

        self.listar()

    def listar(self):
        lista_curso = Cursos.listar()

        for curso in lista_curso:
            cursos_status = "Ativo" if curso[3] == 1 else "Inativo"
            self.lista.insert(
                "",
                END,
                values=(curso[0],
                        curso[1],
                        curso[2],
                        cursos_status,
                        curso[4]))


if __name__ == '__main__':
    root = Tk()

    CursoAppListar(root)

    root.mainloop()
