# Gestão Escolar
Projeto desenvolvido para o curso de desenvolvimento Python.
OBS.: O projeto não está completo, o mesmo, foi criado com base nos meus conhecimentos atuais.

US001 - Gerenciador de alunos
Como usuário do administrativo.
Quero cadastrar, listar e editar todos os alunos matriculados.
Para que se possa ter a gestão dos alunos.

Requisitos
É necessário que as seguintes informações sejam armazenadas:
•	Nome completo;
•	CPF;
•	Matrícula;
•	Telefone;
•	E-mail.
A matrícula deve ser um código único que represente o aluno;
Todos os campos são obrigatórios exceto o telefone.
Para o atributo e-mail é necessário que se verifique se existe o símbolo ‘@’.

US002 - Gerenciador de Professores
Como usuário do administrativo.
Quero gerenciar todos os docentes da instituição.
Para que possa ter a gestão dos professores.

Requisitos
É necessário que as seguintes informações sejam armazenadas:
•	Nome completo;
•	CPF;
•	Matrícula;
•	Telefone;
•	E-mail;
•	Ativo;
•	Formação;
•	Especialidade.
A matrícula deve ser um código único que represente o professor;
Para o atributo e-mail é necessário que se verifique se existe o símbolo ‘@’.
Os campos Nome, CPF, Matrícula e Ativo são obrigatórios.

US003 - Gerenciador de Cursos
Como gestor de uma instituição de ensino.
Quero cadastrar, listar e editar os cursos.
Para que possa controlar e ofertar os cursos.

Requisitos
O sistema deve conter os atributos:
•	Nome do curso;
•	Código do curso;
•	Classificação;
•	Ativo;
•	Descrição.
Todos os atributos exceto a descrição serão obrigatórios;
O código do curso deve ser um valor único que identifique o curso.

US004 - Gerenciador de Turmas
Como usuário do administrativo.
Quero relacionar os alunos à um curso e professor para criar uma turma.
Para que possa gerir as turmas.

Requisitos
Será possível registrar as seguintes informações:
•	Código da turma;
•	Período;
•	Data de início;
•	Data de fim.
Todos os atributos são obrigatórios;
Será possível vincular vários alunos à uma turma, sendo que mínimo de alunos para abertura da turma é 3 (três);
É obrigatório o vínculo de somente um professor;
É obrigatório o vínculo de somente um curso.

