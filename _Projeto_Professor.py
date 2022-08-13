import sqlite3


class Professor:
    """
    Classe que cria o objeto professor.
    """

    def __init__(self, nome, cpf, telefone=None,
                 email=None, formacao=None, especialidade=None):
        self.nome = nome
        self.cpf = cpf
        self.__matricula = 0
        self.tefefone = telefone
        self.email = None
        self.verifica_email(email)
        self.formacao = formacao
        self.especialidade = especialidade

        self.bando_dados()

    @property
    def matricula(self):
        return self.__matricula

    def verifica_email(self, email):
        if email != '':
            if '@' in email:
                self.email = email
            else:
                raise ValueError('E-mail incorreto.')
        else:
            self.email = email

    def bando_dados(self):
        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = f"""
            INSERT INTO Professores(
                Nome,
                CPF,
                Telefone,
                Email,
                Formacao,
                Especialidade
            )
            
            VALUES(
                '{self.nome}',
                '{self.cpf}',
                '{self.tefefone}',
                '{self.email}',
                '{self.formacao}',
                '{self.especialidade}'
            )
        """

        cursor.execute(sql)

        self.__matricula = cursor.lastrowid

        conexao.commit()

        conexao.close()

    @classmethod
    def listar(cls):
        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = """
            SELECT * FROM Professores
                """

        cursor.execute(sql)

        # Lista de alunos recuperada do banco
        lista_professores = cursor.fetchall()

        conexao.close()

        return lista_professores

    def __repr__(self):
        impressao = f'''
        ---- CADASTRO PROFESSORES ----
Matricula: {self.__matricula}
Nome Completo: {self.nome}
CPF: {self.cpf}
Telefone: {self.tefefone}
Formação: {self.formacao}
Especialidade: {self.especialidade}
        '''
        return impressao


if __name__ == '__main__':
    # professor_01 = Professor(nome='Ricardo', cpf=7, email='ricardo@')
    print(Professor.listar())
