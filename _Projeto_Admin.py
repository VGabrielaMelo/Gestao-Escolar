import sqlite3


class Admin:
    def __init__(self, nome, email, usuario, senha):
        self.nome = nome
        self.email = email
        self.__usuario = usuario
        self.__senha = senha

        self.banco_dados()

    @property
    def email(self):
        return self.__email

    @property
    def usuario(self):
        return self.__usuario

    @property
    def senha(self):
        return self.__senha

    @email.setter
    def email(self, email):
        if '@' in email:
            self.__email = email
        else:
            raise ValueError('E-mail inválido')

    def banco_dados(self):
        conexao = sqlite3.connect('Gestão_Escolar.db')

        cursor = conexao.cursor()

        sql = f"""
            INSERT INTO Administradores (
                nome,
                email,
                usuario,
                senha
            )
            VALUES (
                '{self.nome}',
                '{self.email}',
                '{self.usuario}',
                '{self.senha}'
            )
        """
        cursor.execute(sql)

        conexao.commit()

        conexao.close()

    def __repr__(self):
        return f'{self.nome}: {self.email} - {self.__usuario} - {self.__senha}'


if __name__ == '__main__':
    Gabi = Admin(nome='Gabi', email='vgm@vgm', usuario='vgm', senha='girl')
    print(Gabi)
