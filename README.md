# Projeto Django com Tdd

- Author: Kaio Cesar

O intuito deste projeto é mostrar a criação de um projeto real da CRIAÇÃO DA BASE DE DADOS, TESTE UNITÁRIO até o DEPLOY.

## I. Base de dados
###### 0. Entra no shell do MySQL como root
`$ mysql -u root -p`

###### 1. Cria um usuário para teste
`mysql> CREATE USER 'tester'@'localhost' IDENTIFIED BY '123321';`

###### 2. Garante todos os privilegios para este usuário
`mysql> GRANT ALL PRIVILEGES ON * . * TO 'tester'@'localhost';`

###### 3. Desloga do shell e loga com o novo usuário
`mysql> quit;`

`$ mysql -u tester -p`

###### 4. Cria uma base de dados
`mysql> CREATE DATABASE django_test_db;`

###### 5. Acessa a base de dados
`mysql> USE django_test_db;`

###### 6. Cria uma table 
`mysql> CREATE TABLE accounts (id int(11) primary key not null auto_increment, agencia int(10), num_conta int(15), tipo_conta char(3), status char(1) default 0, created_at datetime);`

###### 7. Alguns inserts para agregar o teste
`mysql> INSERT INTO accounts (agencia, num_conta, tipo_conta, status, created_at) VALUES(0004,101001,'1','1','2015-02-16 02:50:00');`

`mysql> INSERT INTO accounts (agencia, num_conta, tipo_conta, status, created_at) VALUES(0004,101002,'1','1','2015-02-16 02:51:00');`

`mysql> INSERT INTO accounts (agencia, num_conta, tipo_conta, status, created_at) VALUES(0004,101003,'1','1','2015-02-16 02:53:00');`

`mysql> INSERT INTO accounts (agencia, num_conta, tipo_conta, status, created_at) VALUES(0004,0123,'2','1','2015-02-16 03:00:00');`



## II. Criação da estrutura do projeto
###### 1. Através do shell, criamos um diretório e entramos nele
`$ mkdir tdd-django && cd tdd-django`

###### 2. Criamos um Virtual Env
`$ virtualenv -p /usr/bin/python3 env`

###### 3. Ativamos o Virtual Env
`$ source env/bin/activate`

###### 4. Instalamos o django (versão 1.7.2)
`$ pip install django==1.7.2`

###### 5. Instalamos também a lib MySQL-python (Atenção que para Python 3 a mysql-python ainda não é suportada)
`$ pip install MySQL-python`

###### 6. Criamos um projeto django com a manage.py na raiz
`$ django-admin.py startproject sistema .`

###### 7. Criamos um app dentro do nosso projeto
`$ python manage.py startapp accounts`


## III. Configurações do projeto
###### 1. vamos adicionar as configurações de banco de dados, no arquivo `/sistema/settings.py`

`
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'NAME': 'django_test_db',

        'HOST': '127.0.0.1',

        'USER': 'tester',

        'PASSWORD': '123321',

    }

}
`

###### 2. Agora adicionamos a app 'accounts' ao nosso 'INSTALLED_APPS'
<code>
	INSTALLED_APPS = (
		........
	    'accounts'
	)
</code>

###### 3. Agora executamos o syncdb para criar um usuário para o painel adm e realizar tarefas de base

(Atenção que neste passo você cadastrará usuário e senha para o painel administrativo)

`$ python manage.py syncdb`

###### 4. Por ultimo executamos as migrates
` python manage.py migrate`

Tudo certo, agora podemos então executamos a aplicação com o seguinte comando:
`python manage.py runserver 127.0.0.1:8001`

Através do navegador acessamos `http://127.0.0.1:8001/` e obtemos um "It worked!".
também podemos acessar o painel administrativo `http://127.0.0.1:8001/admin` (utilize os dados que você cadastrou quando lançou o comando syncdb)








