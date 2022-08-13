from tkinter import *
from _Projeto_Professor import Professor


class ProfessorApp:
    titulo = 'Gestão Escola - Professor'
    font = ('Verdana', 15)

    def __init__(self, master=None):
        self.master = master

        #
        self.master.title(
            ProfessorApp.titulo
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
            text='Cadastro Professores',
            font=('Verdana', 25, 'bold')
        )
        self.label_titulo.pack()

        width = 15
        anchor = W

        # Formulario Professor
        self.frame_formulario = Frame(
            self.frame_master
        )

        self.frame_formulario.pack()

        """
        # Matricula
        self.label_matricula = Label(
            self.frame_formulario,
            text='Matricula:',
            font=ProfessorApp.font,
            width=width,
            anchor=anchor
        )

        self.label_matricula.grid(
            row=0,
            column=0
        )

        self.entry_matricula = Entry(
            self.frame_formulario,
            font=ProfessorApp.font
        )

        self.entry_matricula.grid(
            row=0,
            column=1
        )

        # Ativo
        self.label_situacao = Label(
            self.frame_formulario,
            text='Situação atual:',
            font=ProfessorApp.font,
            width=width,
            anchor=anchor
        )

        self.label_situacao.grid(
            row=1,
            column=0
        )

        self.entry_situacao = Entry(
            self.frame_formulario,
            font=ProfessorApp.font
        )

        self.entry_situacao.grid(
            row=1,
            column=1
        )
        """

        # Nome
        self.label_nome = Label(
            self.frame_formulario,
            text='Nome Completo:',
            font=ProfessorApp.font,
            width=width,
            anchor=anchor
        )

        self.label_nome.grid(
            row=2,
            column=0
        )

        self.entry_nome = Entry(
            self.frame_formulario,
            font=ProfessorApp.font
        )

        self.entry_nome.grid(
            row=2,
            column=1
        )

        # CPF
        self.label_cfp = Label(
            self.frame_formulario,
            text='CPF:',
            font=ProfessorApp.font,
            width=width,
            anchor=anchor
        )

        self.label_cfp.grid(
            row=3,
            column=0
        )

        self.entry_cpf = Entry(
            self.frame_formulario,
            font=ProfessorApp.font
        )

        self.entry_cpf.grid(
            row=3,
            column=1
        )

        # E-mail
        self.label_email = Label(
            self.frame_formulario,
            text='E-mail:',
            font=ProfessorApp.font,
            width=width,
            anchor=anchor
        )

        self.label_email.grid(
            row=4,
            column=0)

        self.entry_email = Entry(
            self.frame_formulario,
            font=ProfessorApp.font
        )

        self.entry_email.grid(
            row=4,
            column=1
        )

        # Telefone
        self.label_telefone = Label(
            self.frame_formulario,
            text='Telefone:',
            font=ProfessorApp.font,
            width=width,
            anchor=anchor
        )
        self.label_telefone.grid(
            row=5,
            column=0
        )

        self.entry_telefone = Entry(
            self.frame_formulario,
            font=ProfessorApp.font
        )

        self.entry_telefone.grid(
            row=5,
            column=1
        )

        # Sub titulo
        self.frame_subtitulo = Frame(
            self.frame_master
        )

        self.frame_subtitulo.pack()

        self.label_subtitulo = Label(
            self.frame_subtitulo,
            text='Formação Academica',
            font=('Verdana', 18, 'bold')
        )
        self.label_subtitulo.pack()

        # SubFormalario
        self.frame_subformulario = Frame(
            self.frame_master
        )

        self.frame_subformulario.pack()

        # Formação
        self.label_formacao = Label(
            self.frame_subformulario,
            text='Formação:',
            font=ProfessorApp.font,
            width=width,
            anchor=anchor
        )
        self.label_formacao.grid(
            row=0,
            column=0
        )

        self.entry_formacao = Entry(
            self.frame_subformulario,
            font=ProfessorApp.font
        )

        self.entry_formacao.grid(
            row=0,
            column=1
        )

        # Especialidade
        self.label_especialidade = Label(
            self.frame_subformulario,
            text='Especialidade:',
            font=ProfessorApp.font,
            width=width,
            anchor=anchor
        )
        self.label_especialidade.grid(
            row=1,
            column=0
        )

        self.entry_especialidade = Entry(
            self.frame_subformulario,
            font=ProfessorApp.font
        )

        self.entry_especialidade.grid(
            row=1,
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
            font=ProfessorApp.font,
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
            font=ProfessorApp.font,
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
            font=ProfessorApp.font,
        )
        self.label_mensagem.pack()

    def salvar(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        email = self.entry_email.get()
        telefone = self.entry_telefone.get()
        formacao = self.entry_formacao.get()
        especialidade = self.entry_especialidade.get()

        if nome and cpf != "":
            try:
                professor = Professor(
                    nome=nome,
                    cpf=cpf,
                    email=email,
                    telefone=telefone,
                    formacao=formacao,
                    especialidade=especialidade
                )

                # self.entry_matricula.insert(0, professor.matricula)

                self.entry_nome.delete(0, END)
                self.entry_nome.focus()

                self.entry_cpf.delete(0, END)
                self.entry_email.delete(0, END)
                self.entry_telefone.delete(0, END)
                self.entry_formacao.delete(0, END)
                self.entry_especialidade.delete(0, END)

                self.label_mensagem['foreground'] = 'Green'
                self.label_mensagem['text'] = f'Professor {professor.matricula} - {professor.nome} ' \
                                              f'Cadastrado com sucesso !'

            except ValueError as err:
                self.label_mensagem['text'] = err
                self.label_mensagem.pack()
        else:
            self.label_mensagem['text'] = 'Informe os dados necessarios'


if __name__ == '__main__':
    root = Tk()
    ProfessorApp(root)
    mainloop()
