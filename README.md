# roomsBooker

Esse é um projeto bem simples para que empresas possam agendar suas reuniões via chamadas REST.
Foi todo escrito em Python e conta com a ajuda de algumas bibliotecas de Python, como:

- Django
- django-rest-framework
- coverage

Além disso, ainda explorei algumas vantagens que o Docker pode nos dar para reprodução de aplicações
de maneira simples e rápida.

Vale ressaltar que utilizei o log padrão do django, que está logando no arquivo ```all_logs.log```.

Abaixo, vou mostrar duas maneiras de rodar a aplicação, uma via Docker e outra nativamente:

## 1. Rodando a aplicação

### 1.1 Rodando via Docker

Para rodar via docker, basta ter o docker instalado na sua máquina. Caso não tenha, basta seguir este [link](https://docs.docker.com/install/#supported-platforms) para
instalá-lo. Após isso, na raiz do projeto, onde está localizado o Dockerfile, basta executar:

``` shell

docker build -t django-room-booker .

```

Esse comando vai criar uma imagem Docker, que nesse caso é baseada na imagem do Python, na sua máquina, para que você possa rodar um container.

Após esse comando, vamos realmente iniciar o container que vai servir a nossa API. Para isso, rode:

``` shell

docker run -p 5000:5000 -d -v <LOCAL_QUE_VOCE_DESEJA_MONTAR>/:/app/ django-room-booker

```

Vale ressaltar nessa parte que estamos mapeando a porta 5000 do container (que é onde o django esta rodando) na porta 5000 do host, para que possamos acessar externamente
nossa API. Também é importante ressaltar que devemos montar volumes para não perdermos as informações caso algo aconteça com os containers.

### 1.2 Rodando nativamente

Para rodar a aplicaçao nativamente, também precisamos de poucos passos até tê-la de pé. Para isso, dentro da pasta do projeto, rode os seguintes comandos:

``` shell

pip3 install -r requirements.txt

```

Esse comando é usado para instalar todas as depências necessárias para o projeto. Cabe lembrar que é necessário ter isntalado o ```pip```. Caso você não tenha essa ferramenta
instalada, esse [link](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3) tem instruções muito bem detalhadas de como fazer esse processo.

Após isso, vamos realizar as migrações para o banco. Basta rodar (ainda na raiz do projeto):

``` shell

python3 manage.py migrate

```

Feitas as migrações, é hora de rodar o projeto. Você pode fazer isso da seguinte maneira:

``` shell

python3 manage.py runserver

```

Para rodar os testes, e também ter acesso as informações de coverage, basta rodar:

``` shell

coverage run manage.py test

```

E para obter as informações de cobertura, basta rodar:

``` shell

coverage report

```

## 2. Documentação da API

### 2.1 Documentação das salas

Para interagir com as salas, foram criados os endpoints abaixo. Também estão mostrados como estes devem ser consumidos.

#### 2.1.1 Criar uma sala

- **Endpoint:** /booker/rooms/

- **Method:** POST

- **Body:**

``` json

{
    "name": "Quaresma",
    "level": "2",
    "description": "sala grande"
}

```

- **Response Codes:**

**201**: A sala foi criada. Também será retornado o json com a estrutura da sala, junto com a chave primaria que foi criada.

**409**: O Body não está correto

#### 2.1.2 Editar uma sala

- **Endpoint:** /booker/rooms/<pk:int>/

- **Method:** PATCH

- **Body:** Aqui no body, você deve colocar todos os campos que deseja alterar do objeto que já existe no banco, com o valor que deseja que ele obtenha.

``` json

{
    "name": "Quaresma",
    "level": "3",
    "description": "sala media"
}

```

- **Response Codes:**

**200**: A sala foi alterada com sucesso.

**404**: A sala que você está tentando alterar não existe.

#### 2.1.1 Deletar uma sala

- **Endpoint:** /booker/rooms/<pk:int>/

- **Method:** DELETE

- **Response Codes:**

**200**: A sala foi removida com sucesso.

**404**: A sala que você está tentando deletar não existe

#### 2.1.1 Listar salas

- **Endpoint:** /booker/rooms/

- **Method:** GET

- **Response Codes:**

**200**: O processo de listagem das salas ocorreu com sucesso. Também será retornado uma lista das salas da seguinte forma:

``` json

[
    {
        "name": "Quaresma",
        "level": 2,
        "description": "sala grande",
        "pk": 1
    },
    {
        "name": "Brasil",
        "level": 3,
        "description": "sala pequena",
        "pk": 2
    }
]

```

### 2.2 Documentação das reservas

#### 2.2.1 Criar uma reserva
#### 2.2.2 Editar uma reserva
#### 2.2.1 Deletar uma reserva
#### 2.2.1 Listar reserva