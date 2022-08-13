import sqlite3


class Cursos:
    def __init__(self, nome, classificacao, descricao=None):
        self.nome = nome
        self.__codigo = 0
        self.classificacao = classificacao
        self.descricao = descricao

        self.banco_dados()

    @property
    def codigo(self):
        return self.__codigo

    def banco_dados(self):
        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = f"""
            INSERT INTO Cursos (
                Nome,
                Classificacao,
                Descricao
            )
            VALUES (
                '{self.nome}',
                '{self.classificacao}',
                '{self.descricao}'
            )
        """

        cursor.execute(sql)

        self.__codigo = cursor.lastrowid

        conexao.commit()

        conexao.close()

    @classmethod
    def listar(cls):
        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = f"""
            SELECT * FROM Cursos
                """

        cursor.execute(sql)

        # Lista de alunos recuperada do banco
        lista_cursos = cursor.fetchall()

        conexao.close()

        return lista_cursos

    def __repr__(self):
        impressao = f'''
        --- Cadastro Cursos ---
Código Curso: {self.__codigo}
Nome: {self.nome}
Classificação: {self.classificacao}
Descrição: {self.descricao}
        '''
        return impressao


if __name__ == '__main__':
    # Python = Cursos(nome='Python', classificacao='Programação')
    print(Cursos.listar())
