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

<pre>
	DATABASES = {

	    'default': {

	        'ENGINE': 'django.db.backends.mysql',

	        'NAME': 'django_test_db',

	        'HOST': '127.0.0.1',

	        'USER': 'tester',

	        'PASSWORD': '123321',

	    }

	}
</pre>


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


## IV. Criação do modelo de dados
Sem pressa, vamos ao nosso arquivo `accounts/models.py` e iremos criar seu conteúdo da seguinte maneira:
<pre>
	from __future__ import absolute_import
	from django.db import models


	class Accounts(models.Model):
		id = models.IntegerField(primary_key=True)
		agencia = models.IntegerField()
		num_conta = models.IntegerField()
		tipo_conta = models.CharField(max_length=3)
		status = models.CharField(max_length=1)
		created_at = models.DateTimeField()

		class Meta:
			managed = False
			db_table = 'accounts'
			verbose_name = 'Account'
			verbose_name_plural = 'Accounts'

		"""
			Função ilustrativa para ajudar a explicar o test unitário
		"""	
		def CheckAccount(self, number=None):
			if (not number):
				return False

			if (numer == '123'):
				return True

			return False
</pre>



## V. Implementar testes de funcionalidade com a lib TestCase
Para realizar um teste, o django disponibiliza no seu comando de geração de aplicações, um arquivo tests.py,
e dentro de cada arquivo deste está o conteúdo abaixo:

<pre>
	from django.test import TestCase

	# Create your tests here.
</pre>

Agora iremos acessar o arquivo  tests.py que está dentro de `accounts/`

e iremos iniciar nossos testes básicos, veja abaixo como ficara o nosso teste:

<pre>
	from django.test import TestCase

	from accounts.models import Accounts

	class AccountsTestCase (TestCase):

		def test_check_account(self):
			Act = Accounts()
			self.assertEqual(Act.CheckAccount(), True)

</pre>

E para visualizarmos esse teste unitário, vá até o terminal e digite o sequinte comando:
`$ python manage.py test`

Esse comando irá primeiro criar uma base de dados de teste, em seguida irá executar todos os testes do projeto, e ao final ela irá excluir a base de dados de testes.




