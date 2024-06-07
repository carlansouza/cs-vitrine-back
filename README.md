# CS VITRINE - Backend


```markdown
# FastAPI Project
Desenvolvido para teste de seleção, com o objetivo de criar uma vitrine de venda de carros.

Este é um projeto básico de uma aplicação FastAPI com autenticação usando JWT, configurada para ser executada em um contêiner Docker.

## Configuração e Execução

### Pré-requisitos

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
```	
### Passos para executar o projeto

1. **Clone o repositório:**

   ```sh
   git clone https://github.com/carlansouza/cs-vitrine-back
   cd seu-repositorio
   ```

2. **Configure as variáveis de ambiente:**

   ```sh
   cp .env_example .env
   ```
    - Crie um arquivo `.env` e configure as variáveis de ambiente conforme necessário.

3. **Construir a imagem Docker:**

   ```sh
   docker-compose build
   ```

4. **Iniciar o contêiner Docker:**

   ```sh
   docker-compose up
   ```

5. **A aplicação estará disponível em:**

   ```
   http://localhost:8000/docs
   ```

##
- ## Seed
o seed.py é responsável por popular o banco de dados com os dados iniciais.

| User: admin@admin.com | Password: admin | Tipo: Admin |
|-----------------------|------------------| ------------|
| User: user@example.com | Password: password1| Tipo: User |



##
# Uso da API

## Swagger
 - Para acessar a documentação da API, acesse o link: http://localhost:8000/docs
##

### Dinâmica
```markdown
- Cada carro deve tem as informações: 
    name, brand, model, price, image_url.

- Cada user tem as informações: 
    name, email, password.

- No login se deve passar apenas: 
    email e password

- Só é possivel cadastrar um carro com a autenticação de administrador, assim como atualizar e deletar.

- A rota GET /car é aberta, logo, pode ser acessada independente de autenticação.
```

### Criação de um novo usuário

- **Endpoint:** `POST /users/`
- **Corpo da requisição:**

  ```json
  {
    "name": "seu-username",
    "email": "seu-email@example.com",
    "hasehd_password": "sua-senha"
  }
  ```

- **Exemplo de comando curl:**

  ```sh
  curl -X POST "http://localhost:8000/users/" -H "Content-Type: application/json" -d '{
    "username": "seu-username",
    "email": "seu-email@example.com",
    "hasehd_password": "sua-senha"
  }'
  ```

### Autenticação e obtenção do token JWT

- **Endpoint:** `POST /auth`
- **Corpo da requisição (form-data):**

  ```json
  {
    "email": "seu-email",
    "password": "sua-senha"
  }
  ```

##
## Erro de CORS
- Caso ocorra erro de CORS, necessario verificar a porta que o frontend está rodando e adicionar no arquivo main.py

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`:

### Instruções de Uso do README.md

1. **Clone o repositório**: Baixe o projeto do repositório GitHub.
2. **Construa a imagem Docker**: Use `docker-compose build` para construir a imagem Docker.
3. **Inicie o contêiner Docker**: Use `docker-compose up` para iniciar o contêiner.
4. **Acesse a aplicação**: A aplicação estará disponível em `http://localhost:8000/docs`.

