# projecto_web_cpds_demo
SIMPLE WEB PROJECT FOR CPDS-CD

>> Simple Django Project for Associacoa Provincial para
Desenvolvimento Sustentavel de Cabo Delegado (CPDS-CD)


<!-- como rodar este app
[1] CREATE APP
    python3 manager.py startapp contas
    [com esse comando sera criado uma pasta com nome contas
    e la tera seu app com todas as configuracoes feitas
    ]
    pra este app ser recohecido com systema precisamos registar nas settings na seccao 
    INSTALLED_APPS=[contas]

[2] CREATE DATABASE MIGRATIONS
    criar o banco de dados que ja vem embutido no frammworker
    logo ao iniciar o projecto (razao pela qual o[django eh considerado como frammworker com baterias inclusas a])

    >> python manager.py migrate

    [hence this command will create a database configurations of db.sqlite] and tables,

[3] RUN FIRST TIME YOUR APP
    >>python manager.py runserver
    your app is in http://127.0.0.1:8000/

[4] CREATE SUPERUSER
    atraves do app [django.contrib.admin]
    que vem com opadrao do se projecto 
    e possivel agora criares seus clientes 
     ocomando abaixo cria um superuser no banco de dados de app

     >> python manager.py createsuperuser
        username: xxxxx
        password:xxxxx
        este user
 [5] TESTANDO OS USUARIOS CRIADOS
    >python manage.py runserver
    >>http://127.0.0.1:8000/admin

    este url /admin
    esta registada na pasta urls 
     -->
    ```py
    from django.contrib import admin
    from django.urls import path

    urlpatterns = [
        path('admin/', admin.site.urls),
]

    ```