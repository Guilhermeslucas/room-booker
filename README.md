# roomsBooker

Esse é um projeto bem simples para que empresas possam agendar suas reuniões via chamadas REST.
Foi todo escrito em Python e conta com a ajuda de algumas bibliotecas de Python, como:

- Django
- django-rest-framework
- coverage

Além disso, ainda explorei algumas vantagens que o Docker pode nos dar para reprodução de aplicações
de maneira simples e rápida.

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

docker run -t booker-api -p 5000:5000 django-room-booker

```

Vale ressaltar nessa parte que estamos mapeando a porta 5000 do container (que é onde o django esta rodando) na porta 5000 do host, para que possamos acessar externamente
nossa API.

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