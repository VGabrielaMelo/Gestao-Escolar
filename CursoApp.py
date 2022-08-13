from tkinter import *
from _Projeto_Cursos import Cursos


class CursoApp:
    titulo = 'Gestão Escolar - Curso'
    font = ('Verdana', 15)

    def __init__(self, master=None):
        self.master = master

        #
        self.master.title(
            CursoApp.titulo
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
            text='Cadastro Cursos',
            font=('Verdana', 25, 'bold')
        )
        self.label_titulo.pack()

        width = 15
        anchor = W

        # Formulario Curso
        self.frame_formulario = Frame(
            self.frame_master
        )

        self.frame_formulario.pack()

        """
        # Código do curso
        self.label_matricula = Label(
            self.frame_formulario,
            text='Código do Curso:',
            font=CursoApp.font,
            width=width,
            anchor=anchor
        )

        self.label_matricula.grid(
            row=0,
            column=0
        )

        self.entry_matricula = Entry(
            self.frame_formulario,
            font=CursoApp.font
        )

        self.entry_matricula.grid(
            row=0,
            column=1
        )

        # Ativo
        self.label_situacao = Label(
            self.frame_formulario,
            text='Situação atual:',
            font=CursoApp.font,
            width=width,
            anchor=anchor
        )

        self.label_situacao.grid(
            row=1,
            column=0
        )

        self.entry_situacao = Entry(
            self.frame_formulario,
            font=CursoApp.font
        )

        self.entry_situacao.grid(
            row=1,
            column=1
        )
        """

        # Nome
        self.label_nome = Label(
            self.frame_formulario,
            text='Nome do Curso:',
            font=CursoApp.font,
            width=width,
            anchor=anchor
        )

        self.label_nome.grid(
            row=2,
            column=0
        )

        self.entry_nome = Entry(
            self.frame_formulario,
            font=CursoApp.font
        )

        self.entry_nome.grid(
            row=2,
            column=1
        )

        # Classificação
        self.label_classificacao = Label(
            self.frame_formulario,
            text='Classificação:',
            font=CursoApp.font,
            width=width,
            anchor=anchor
        )
        self.label_classificacao.grid(
            row=7,
            column=0
        )

        self.entry_classificacao = Entry(
            self.frame_formulario,
            font=CursoApp.font
        )

        self.entry_classificacao.grid(
            row=7,
            column=1
        )

        # Descrição
        self.label_descricao = Label(
            self.frame_formulario,
            text='Descrição:',
            font=CursoApp.font,
            width=width,
            anchor=anchor
        )
        self.label_descricao.grid(
            row=8,
            column=0
        )

        self.entry_descricao = Entry(
            self.frame_formulario,
            font=CursoApp.font
        )

        self.entry_descricao.grid(
            row=8,
            column=1
        )

        # Área de Ferramentas
        self.frame_ferramentas = Frame(
            self.frame_master
        )

        self.frame_ferramentas.pack(
            fill=X
        )

        # Botão Salvar
        self.button_salvar = Button(
            self.frame_ferramentas,
            text='Salvar',
            font=CursoApp.font,
            background='Green',
            foreground='Black',
            command=self.salvar
        )

        self.button_salvar.pack(
            side=RIGHT
        )

        # Botão Fechar
        self.button_fechar = Button(
            self.frame_ferramentas,
            text='Fechar',
            font=CursoApp.font,
            background='Red',
            foreground='Black',
            command=self.master.quit
        )

        self.button_fechar.pack(
            side=LEFT
        )

        # Mensagem
        self.label_mensagem = Label(
            self.frame_ferramentas,
            font=CursoApp.font,
        )
        self.label_mensagem.pack()

    def salvar(self):
        nome = self.entry_nome.get()
        classificacao = self.entry_classificacao.get()
        descricao = self.entry_descricao.get()

        if nome and classificacao != '':
            curso = Cursos(
                nome=nome,
                classificacao=classificacao,
                descricao=descricao
            )

            # self.entry_matricula.insert(0, curso.matricula)

            self.entry_nome.delete(0, END)
            self.entry_nome.focus()

            self.entry_classificacao.delete(0, END)
            self.entry_descricao.delete(0, END)

            self.label_mensagem['foreground'] = 'Green'
            self.label_mensagem['text'] = f'Curso {curso.codigo} - {curso.nome} ' \
                                          f'Cadastrado com sucesso !'

        else:
            self.label_mensagem['foreground'] = 'Black'
            self.label_mensagem['text'] = 'Informe os dados necessarios'


if __name__ == '__main__':
    root = Tk()
    CursoApp(root)
    mainloop()
