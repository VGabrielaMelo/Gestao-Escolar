from tkinter import *
from tkinter.ttk import Treeview
# TKCALENDAR = AONDE TEM OS ENTRY COM OS CALENDÁRIOS
from tkcalendar import DateEntry
# AINDA VOU DESCOBRIR COMO USAR ESSE MODULO DATETIME KKK
import datetime
from _Projeto_Cursos import Cursos
from _Projeto_Professor import Professor
from _Projeto_Turma import Turma


class TurmaApp:

    width = 10

    anchor = W

    # titulo padrão da minha interface
    titulo = 'Formulário de Turma'

    # fonte padrão dos elementos da interface
    font = ('Verdana', 14)

    # LISTA FIXA DOS PERIODOS
    lista_periodo = ['Manhã', 'Tarde', 'Noite']

    def __init__(self, master=None):

        self.master = master

        self.master.title(TurmaApp.titulo)

        self.frame_master = Frame(self.master)

        self.frame_master.pack()

        self.frame_ferramentas = Frame(self.frame_master)

        self.frame_ferramentas.pack()

        self.button = Button(
            self.frame_ferramentas, text='Salvar Turma', command=self.salvar)

        self.button.pack()

        # Mensagem
        self.label_mensagem = Label(
            self.frame_ferramentas,
            font=TurmaApp.font
        )

        self.label_mensagem.pack()

        self.frame_titulo = Frame(self.frame_master)

        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text=TurmaApp.titulo,
            font=(
                'Verdana',
                30,
                'bold'
            )
        )

        self.label_titulo.pack()

        self.frame_datas = Frame(self.frame_master)

        self.frame_datas.pack()

        # data de
        self.label_data_de = Label(
            self.frame_datas,
            text='Data Inicio:',
            font=TurmaApp.font,
            width=TurmaApp.width,
            anchor=TurmaApp.anchor
        )

        self.label_data_de.grid(
            row=0,
            column=0
        )

        self.entry_data_de = DateEntry(
            self.frame_datas,
            font=TurmaApp.font
        )

        self.entry_data_de.grid(
            row=0,
            column=1
        )

        # Data ate
        self.label_data_ate = Label(
            self.frame_datas,
            text='Data até:',
            font=TurmaApp.font,
            width=TurmaApp.width,
            anchor=TurmaApp.anchor
        )

        self.label_data_ate.grid(
            row=1,
            column=0
        )

        self.entry_data_ate = DateEntry(
            self.frame_datas,
            font=TurmaApp.font,
        )

        self.entry_data_ate.grid(
            row=1,
            column=1
        )

        # PERIODO - LISTA DOS PERIODOS
        self.frame_periodo = Frame(self.frame_master)

        self.frame_periodo.pack()

        self.label_data_de = Label(
            self.frame_periodo,
            text='Perido:',
            font=TurmaApp.font,
            width=TurmaApp.width,
            anchor=TurmaApp.anchor
        )

        self.label_data_de.grid(
            row=0,
            column=0
        )

        self.lista_periodo = Listbox(self.frame_periodo)

        for item in TurmaApp.lista_periodo:
            self.lista_periodo.insert(END, item)

        self.lista_periodo.grid(
            row=0,
            column=1
        )

        # CURSO LISTA DOS CURSOS PARA SELECIONAR

        self.frame_curso = Frame(self.frame_master)

        self.frame_curso.pack()

        self.label_curso = Label(
            self.frame_curso,
            text='Curso:',
            font=TurmaApp.font,
            width=TurmaApp.width,
            anchor=TurmaApp.anchor
        )

        self.label_curso.grid(
            row=0,
            column=0
        )

        self.lista_curso = Treeview(
            self.frame_curso,
            selectmode="browse",
            columns=("codigo", "nome"),
            show="headings"
        )

        self.lista_curso.column(
            "codigo",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista_curso.heading(
            "#1",
            text="Código"
        )

        self.lista_curso.column(
            "nome",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista_curso.heading(
            "#2",
            text="Nome"
        )
        self.listar_curso()

        self.lista_curso.grid(
            row=0,
            column=1
        )

        # Professor - LISTA PARA SELECIONAR O PROFESSOR
        self.frame_professor = Frame(self.frame_master)

        self.frame_professor.pack()

        self.label_professor = Label(
            self.frame_professor,
            text='professor:',
            font=TurmaApp.font,
            width=TurmaApp.width,
            anchor=TurmaApp.anchor
        )

        self.label_professor.grid(
            row=0,
            column=0
        )

        self.lista_professor = Treeview(
            self.frame_professor,
            selectmode="browse",
            columns=("matricula", "nome"),
            show="headings",
        )

        self.lista_professor.column(
            "matricula",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista_professor.heading(
            "#1",
            text="Código"
        )

        self.lista_professor.column(
            "nome",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista_professor.heading(
            "#2",
            text="Nome"
        )

        self.listar_professor()

        self.lista_professor.grid(
            row=0,
            column=1
        )

    def listar_curso(self):
        # PEGANDO A LISTA DOS CURSOS LA NA CLASSA CURSO, USANDO O METODO LISTAR
        lista_cursos = Cursos.listar()

        for curso in lista_cursos:
            # PERCORRENDO A LISTA E COLANDO CADA 'LINHA', NA TABELA DOS CURSOS
            self.lista_curso.insert(
                "",
                END,
                values=(
                    curso[0],
                    curso[1]
                )
            )

    def listar_professor(self):
        # MESMA LOGICA DO CURSO, PEGANDO A LISTA DOS PROFESSORES
        lista_professores = Professor.listar()

        for professor in lista_professores:
            self.lista_professor.insert(
                "",
                END,
                values=(
                    professor[0],
                    professor[1]
                )
            )

    def salvar(self):

        # pegando a data "convertando a data para data de banco de dados"
        data_de = self.entry_data_de.get()

        data_de_format = datetime.datetime.strptime(data_de, "%d/%m/%Y").date()

        print(data_de_format)

        data_ate = self.entry_data_ate.get()

        data_ate_format = datetime.datetime.strptime(data_ate, "%d/%m/%Y").date()

        print(data_ate_format)

        # VERIFICANDO SE TUDO FOI SELECIONADO
        try:
            # PEGANDO O PERIODO LA NA TABELA PERIODO
            periodo = self.lista_periodo.get(
                self.lista_periodo.curselection())
            print(periodo)

            # Pegando o Curso
            curItem = self.lista_curso.focus()

            curso = self.lista_curso.item(curItem)
            # PEGANDO O CÓDIGO DO CURSO, E SETANDO EM UMA VARIAVEL
            codigo_curso = curso['values'][0]

            print(codigo_curso)

            # Pegando o Professor
            curItem = self.lista_professor.focus()

            professor = self.lista_professor.item(curItem)
            # MESMA COISA AQUI
            matricula_professor = professor['values'][0]

            print(matricula_professor)
            # TENTAR FAZER O CADASTRO DA TURMA, SE DER ERRO, É PQ NÃO TEM PERIODO E DATA PARA ADICIONAR A TURMA
            try:
                turma = Turma(
                    periodo=periodo,
                    inicio=data_de_format,
                    fim=data_ate_format,
                    codigo_curso=codigo_curso,
                    matricula_professor=matricula_professor,
                )

                # self.entry_matricula.insert(0, aluno.matricula)

                # self.entry_matricula.grid(
                #     row=0,
                #     column=1
                # )

                self.label_mensagem['foreground'] = 'Green'
                self.label_mensagem['text'] = f"Turma {turma.codigo} cadastrado !"

            except ValueError as err:
                self.label_mensagem['foreground'] = 'Red'
                self.label_mensagem['text'] = err
        except:
            self.label_mensagem['foreground'] = 'Red'
            self.label_mensagem['text'] = 'Preencher todos os campos !'


if __name__ == '__main__':
    root = Tk()

    TurmaApp(root)

    root.mainloop()
