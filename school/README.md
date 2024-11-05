# School Management System

Este é um sistema de gerenciamento escolar desenvolvido com Flask e MySQL. O sistema permite gerenciar usuários, turmas e atividades.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

```
school/
│
├── app.py
├── bd.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── ...
├── files/
│   ├── script.sql
│   ├── users.csv
│   └── ...
├── README.md
requirements.txt
```

## Funcionalidades

### Usuários

- **Login**: Os usuários podem fazer login no sistema.
- **Recuperação de Senha**: Os usuários podem recuperar suas senhas.

### Turmas

- **Adicionar Turma**: Os usuários podem adicionar novas turmas.
- **Editar Turma**: Os usuários podem editar turmas existentes.
- **Excluir Turma**: Os usuários podem excluir turmas.
- **Ver Turmas**: Os usuários podem visualizar todas as turmas.

### Atividades

- **Adicionar Atividade**: Os usuários podem adicionar novas atividades a uma turma.
- **Editar Atividade**: Os usuários podem editar atividades existentes.
- **Excluir Atividade**: Os usuários podem excluir atividades.
- **Ver Atividades**: Os usuários podem visualizar todas as atividades de uma turma.

## Configuração do Banco de Dados

O banco de dados é configurado usando o script SQL em [school/files/script.sql](school/files/script.sql). Para configurar o banco de dados, execute o script no seu servidor MySQL.

## Executando o Projeto

1. Clone o repositório.
2. Configure o banco de dados MySQL usando o script SQL fornecido.
3. Instale as dependências necessárias.
4. Execute o aplicativo Flask.

```sh
git clone https://github.com/GetuliovmSantos/flask-simulations
cd school
pip install -r ../requirements.txt
python app.py
```

## Estrutura do Código

- **app.py**: Este arquivo contém as rotas e a lógica principal do aplicativo Flask.
- **bd.py**: Este arquivo contém a classe BD que gerencia a conexão com o banco de dados e as operações CRUD.
- **templates/**: Este diretório contém os arquivos HTML usados para renderizar as páginas do aplicativo.
- **files/**: Este diretório contém arquivos auxiliares, como o script SQL para configurar o banco de dados e um arquivo CSV com dados de usuários.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.