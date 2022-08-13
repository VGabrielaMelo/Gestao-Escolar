from tkinter import *
from _Projeto_Alunos import Aluno


class AlunoApp:
    """
    Classe empacotadora (wapper) para armazenar todos os componentes da interface de Alunos.
    """
    # Titulo Padrão da minha interface
    titulo = 'Gestão Escolar - Aluno'
    # Fonte padrão
    font = ('Verdana', 15)

    def __init__(self, master=None):
        """
        Contrutor do Wapper
        Local para declararmos os componentes da interface.
        """

        # Armazenei em um atributo o container principal.
        self.master = master
        self.master.title(
            AlunoApp.titulo
        )

        # Criação do Framer central para apresentar em tela os componentes.
        self.frame_master = Frame(
            self.master
        )

        self.frame_master.pack()

        # Apresentar o titulo da interface
        # Segmentar as áreas da interface utilizando o container Frame
        self.frame_titulo = Frame(
            self.frame_master
        )
        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text='Cadastro Alunos',
            font=('Verdana', 25, 'bold')
        )
        self.label_titulo.pack()

        width = 15
        anchor = W

        # Formulario do aluno
        # Segmentou a área do formulario
        self.frame_formulario = Frame(
            self.frame_master
        )
        self.frame_formulario.pack()

        """
        # Matricula
        self.label_matricula = Label(
            self.frame_formulario,
            text='Matricula:',
            font=AlunoApp.font,
            width=width,
            anchor=anchor
        )

        self.label_matricula.grid(
            row=0,
            column=0
        )

        self.entry_matricula = Entry(
            self.frame_formulario,
            font=AlunoApp.font
        )

        self.entry_matricula.grid(
            row=0,
            column=1
        )
        """

        # Nome Completo
        self.label_nome = Label(
            self.frame_formulario,
            text='Nome Completo:',
            font=AlunoApp.font,
            width=width,
            anchor=anchor
        )

        self.label_nome.grid(
            row=1,
            column=0
        )
        
        self.entry_nome = Entry(
            self.frame_formulario, 
            font=AlunoApp.font
        )

        self.entry_nome.grid(
            row=1,
            column=1
        )

        # CPF
        self.label_cfp = Label(
            self.frame_formulario,
            text='CPF:',
            font=AlunoApp.font,
            width=width,
            anchor=anchor
        )

        self.label_cfp.grid(
            row=2,
            column=0
        )

        self.entry_cpf = Entry(
            self.frame_formulario,
            font=AlunoApp.font
        )

        self.entry_cpf.grid(
            row=2,
            column=1
        )

        # E-mail
        self.label_email = Label(
            self.frame_formulario,
            text='E-mail:',
            font=AlunoApp.font,
            width=width,
            anchor=anchor
        )

        self.label_email.grid(
            row=3,
            column=0)

        self.entry_email = Entry(
            self.frame_formulario,
            font=AlunoApp.font
        )

        self.entry_email.grid(
            row=3,
            column=1
        )

        # Telefone
        self.label_telefone = Label(
            self.frame_formulario,
            text='Telefone:',
            font=AlunoApp.font,
            width=width,
            anchor=anchor
        )
        self.label_telefone.grid(
            row=4,
            column=0
        )

        self.entry_telefone = Entry(
            self.frame_formulario,
            font=AlunoApp.font
        )

        self.entry_telefone.grid(
            row=4,
            column=1
        )

        # Área de ferramentas
        self.frame_ferramentas = Frame(
            self.frame_master
        )

        self.frame_ferramentas.pack(
            fill=X
        )

        # Botão SALVAR
        self.button_salvar = Button(
            self.frame_ferramentas,
            text='Salvar',
            font=AlunoApp.font,
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
            font=AlunoApp.font,
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
            font=AlunoApp.font
        )
        self.label_mensagem.pack()

    def salvar(self):
        # remove o valor Entry
        # self.entry_matricula.delete(0, END)

        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        email = self.entry_email.get()
        telefone = self.entry_telefone.get()

        if nome and cpf and email != '':

            try:
                aluno = Aluno(
                    nome=nome,
                    cpf=cpf,
                    email=email,
                    telefone=telefone
                )

                # self.entry_matricula.insert(0, aluno.matricula)

                self.entry_nome.delete(0, END)
                self.entry_nome.focus()

                self.entry_cpf.delete(0, END)
                self.entry_email.delete(0, END)
                self.entry_telefone.delete(0, END)

                self.label_mensagem['foreground'] = 'Green'
                self.label_mensagem['text'] = f'Aluno {aluno.matricula} - {aluno.nome} Cadastrado com sucesso !'

            except ValueError as err:
                self.label_mensagem['foreground'] = 'Red'
                self.label_mensagem['text'] = err
        else:
            self.label_mensagem['text'] = 'Informe os dados necessarios'


if __name__ == '__main__':
    root = Tk()
    AlunoApp(root)
    root.mainloop()
