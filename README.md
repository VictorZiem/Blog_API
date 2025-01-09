Blog API com Flask
Este repositório apresenta uma API de Blog desenvolvida em Python utilizando Flask e SQLite. O projeto demonstra um CRUD (Create, Read, Update, Delete) completo para posts e comentários, ilustrando boas práticas de organização de código, interação com banco de dados e retorno de dados em formato JSON.

Índice
Tecnologias Utilizadas
Como Executar
Clonando o Repositório
Instalando Dependências
Executando o Projeto
EndPoints Disponíveis
Posts
Comentários
Estrutura de Pastas
Possíveis Melhorias
Contribuindo
Licença
Tecnologias Utilizadas
Python 3.x
Flask para criação de rotas e gestão de requisições HTTP
Flask-SQLAlchemy para integração com o banco de dados SQLite
SQLite como banco de dados local e leve
Como Executar
1. Clonando o Repositório
Abra o terminal (ou Git Bash) e digite:

git clone https://github.com/SEU_USUARIO/Blog_API.git
cd Blog_API
2. Instalando Dependências
É recomendado criar um ambiente virtual antes:

python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no Linux/Mac
source venv/bin/activate
Depois, instale as dependências:

pip install -r requirements.txt
Se não houver um requirements.txt, instale manualmente:

pip install flask flask_sqlalchemy
3. Executando o Projeto
Verifique que você está na pasta raiz do projeto (Blog_API).
Inicie a aplicação:
python blog_API.py
O Flask rodará por padrão em http://127.0.0.1:5000.
Para finalizar, pressione CTRL + C no terminal.
Endpoints Disponíveis
1. Posts
GET /posts
Retorna todos os posts em formato JSON.

POST /posts
Cria um novo post.
Corpo (JSON):

json
{
  "title": "Título do Post",
  "content": "Conteúdo do Post"
}
Retorna o post criado.

GET /posts/<post_id>
Retorna um post específico pelo seu ID.

PUT /posts/<post_id>
Atualiza um post existente.
Corpo (JSON) – campos opcionais:

json
{
  "title": "Novo Título",
  "content": "Novo Conteúdo"
}
DELETE /posts/<post_id>
Exclui um post específico.

2. Comentários
GET /posts/<post_id>/comments
Retorna todos os comentários associados a um post.

POST /posts/<post_id>/comments
Cria um comentário para um post.
Corpo (JSON):

json
{
  "text": "Comentário..."
}
GET /posts/<post_id>/comments/<comment_id>
Retorna um comentário específico de um post.

PUT /posts/<post_id>/comments/<comment_id>
Atualiza o conteúdo de um comentário.
Corpo (JSON):

json
{
  "text": "Novo texto do comentário"
}
DELETE /posts/<post_id>/comments/<comment_id>
Exclui um comentário específico de um post.

Estrutura de Pastas
Blog_API/
├── blog_API.py          # Arquivo principal Flask
├── blog.db              # Banco de dados SQLite (gerado após rodar a aplicação)
├── my_models.py         # (ou models.py) Classes e tabelas (Post, Comment)
├── requirements.txt     # Dependências do projeto
├── venv/                # Ambiente virtual (opcional)
└── README.md            # Documentação do projeto
Possíveis Melhorias
Autenticação: Adicionar sistema de login (JWT ou sessão) para restringir criação/edição de posts.
Paginação: Em /posts e /comments, implementar paginação para lidar com grandes volumes de dados.
Validação de Dados: Usar bibliotecas como Flask-Marshmallow para validar campos.
Testes Automatizados: Integrar pytest ou unittest para garantir a qualidade do código.
Deploy: Hospedar em serviços como Heroku, Render, AWS, etc., usando um servidor WSGI (Gunicorn, uWSGI, etc.).
Contribuindo
Contribuições são bem-vindas! Você pode abrir Issues para sugerir melhorias ou relatar bugs, bem como criar Pull Requests. O processo padrão:

Fork este repositório
Crie uma branch (git checkout -b minha-feature)
Faça suas alterações e commit (git commit -m "Descrição da feature")
Push para a branch criada (git push origin minha-feature)
Abra um Pull Request descrevendo o que foi feito
