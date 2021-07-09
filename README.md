# projecto_web_cpds_demo
SIMPLE WEB PROJECT FOR CPDS-CD

>>Simple Django Project for Associacoa Provincial para
Desenvolvimento Sustentavel de Cabo Delegado (CPDS-CD)

[+] como rodar este app
```sh
[ 1 ] CREATE APP
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
    ```
    ```py
    from django.contrib import admin
    from django.urls import path

    urlpatterns = [
        path('admin/', admin.site.urls),
]
#    
    ```
[6] CRIANDO O PRIMEIRO  VIEW:
> na pasta de urls registo os meus views
```py
from projet_name.contas.views import home
# from contas.views import home [onde contas 'e a pasta de app que na qual registei la no inicio]

# no app constas/views.py
def home(request):
    now=datetime.datetime.now()
    html = f'<html><body> The time is {now}</body></html>'
    return HttpResponse(html)
# acessando http://127.0.0.1:8000/home  teras esse template


```

#CRIANDO TEMPLATE
Na mesmo app vou modificar o meu view em vez de retornar um string de html ele vai entao retornar um template de html que estara dentro de uma pasta : ./contas/templates/home.html
```py

# usando TEMPLATES
def home(request):
    now=datetime.datetime.now()
    # poe se dentro de outra pasta caso outro app tenha home nao venha carregar do app contas
    return render(request, 'contas/home.html') 


# CRIANDO O MODELOS

./contas/models.py

from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=180)

    @classmethod
    def create(cls,title):
        book=cls(title=title)
        return book

book=Book.create('Meu livro de django')

pra meu caso criarei o seguinte model o
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_created = models.DateTimeField(auto_now_add=True) #campo de data e auto_now_add=True,
    # ele preeche adata actual de criacoa deste model


```
APos ter criado o model preciso gerar migracoes pra meu banco de dados.

```sh
python manage.py makemigrations
 ```
>After this step the app will lookup on allover my ?installed app in this project in their models
if have any modification found ,then in their migration folder will be generated new version of makemigrations 

>E depois de makemigrations
>precisamos rodar o comando que vai aplicar e criar tais novas tables created

# E aqui temos o arquivo autogerado nas migracoes criando as tabelas e colunas

```py

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
```


# TESTANDO O NOSSO MODELO SEM TER QUE ESCREVER CODIGO DE CRUD (Create Read Update and Delete)
>Basta registar o modelo no admin do seu project
>ex: contas/admin.py
    from .models import Categoria
    admin.site.register(Categoria)


I create another model Transacao
```py

class Transacao(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7,decimal_places=2) #decimal_place=> o nr de digitos que vem depois da virgula
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    observacoes = models.TextField()
```
 Esta classe tem como ForeignKey categoria


 # CRIANDIO FORMULARIOS NO HTML ATRAVES DOS CAMPOS DE MODELOS DE DJANGO
 > para isso no app contas criarei um arquivo form.py 
  > project/contas/form.py

```py 
    # ModelForm
    # para criar django model precisamos importar ModelForm do django para 
    # ele nos der todas as facilidades

    from django.forms import ModelForm,TextInput
    from contas.models import Transacao # Omodel TRansacao 'e o cara k quero fazer crude

    class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data','descricao','valor','categoria','observacoes']

        # atribuido html atributs para ser capturado com css/js
        '''TextInput,Select,Textarea

        '''
        widgets={
            'descricao':TextInput(attrs={'class':'form-control'}),
            'valor':TextInput(attrs={'class':'form-control'}),
            'data':TextInput(attrs={'class':'form-control'}),
            'categoria':TextInput(attrs={'class':'form-control'}),
            'observacoes':TextInput(attrs={'class':'form-control'})
            
            }
 
 
        
"""esse formulario exigira esses atributos obrigatorios o (modelo)

data = models.DateTimeField()
descricao = models.CharField(max_length=200)
valor = models.DecimalField(max_digits=7,decimal_places=2) #decimal_place=> o nr de digitos que vem depois da virgula
categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
observacoes = models.TextField(null=True,blank=True) #campo nao obrigatorio


""" 

    # e Na minha view vou importar este formulario e retornar ele
    # para o um arquivo conatas/templates/contas/form.html
from .forms import TransacaoForm
def nova_transacao(request):
    'se vier com metodo post request.POST sera true ou none e retornara form.htm'
    form =TransacaoForm(request.POST or None) 
    
    if form.is_valid():
        # salvara no db
        form.save()
        # e retornara na listagem
        return redirect('url_trans_list') #trans_list 'e nome que defini para adesignacao
    # da rota transations_list
    
    return render(request, 'contas/form.html',{'form':form})


```
To show draw form in form.html
just add :
```html
    <form method="post" action='#'>
    {% csrf_token %}
    {{form.as_p}} ou[as_table] as=<p> as table=<table>...</table>

    <button class='btn btn-primary' type="submit">Salvar </button>
</form>


a dicionei um js para capturar os campos de formular e atribuir setAttribute('class','form-control')
para assim o bootstrap pegalos


```

#para update do nosso CRUDE criarei um url que recebera um parametro que sera 
id primary key da transacao

```py
mesmo k seu model nao tenhas definido atributo pk o django ja se encarrega de passar esse identificador portanto nao te preocupes se nao o veres pk nu model

#:contas/views.py
def update(request,pk):
    '''
    :params pk= e' id da transacao 
    '''
    # recupero objecto nu banco
    # transation=Transacao.objects.filter(pk=pk) #pega mais k um objecto
    transation=Transacao.objects.get(pk=pk) 
    
    
    # aqui instacio um formulario preechendoos campos do query acima ai transation
    # que pegarei atraveis da filtracao do seu primary_key
    # aqui vou preencher o form os dados que foram retornados
    form =TransacaoForm(request.POST or None, instance=transation)
    
    if form.is_valid():
        form.save()
        return redirect('url_trans_list')
    
    '''
    Aqui retornando o form.html ja preechido com os dados feitos query no database
    '''
    return render(request,'contas/form.html',{'form':form})

#: urls.py
# pk=>primary key
from contas.views import actualizar
urlpatterns =[
    path('update/<int:pk>/',actualizar, name='upadte_trans')
]
"http://192.168.43.66/update/2/"

```
# Fazedo click na transacoa e ele redirecionar para apagina de update
# a transacoa clicada
#NO TEMPLATE DE LIST_TRANSATIONS
>/contas
    /templates
        /contas
            /transations_list.html

```html


<table class="table table-striped">
    <thead>
        <tr>
            <th>Description</th>
            <th>Mount</th>
            <th>Category</th>
            <th>Date</th>
            <th>observacoes</th>
        </tr>
    </thead>

    <tbody>
        
            {% for trans in transations %}
            <tr>
            <td>{{ trans.descricao}}</td>
            <td>{{trans.valor}}</td>
            <td>{{trans.categoria}}</td>
            <td>{{trans.data}}</td>
            <td>
                <p>{{trans.observacoes}}</p>
                <div class='col col-md'>
                    <a class='btn btn-primary' href={% url 'url_update_trans' trans.id %}>Edit</a>
                    <a class='btn btn-danger'>Delete</a>
                </div>
                

            </td>
            </tr>
            {% endfor %}
        
    </tbody>
</table>

<style>
    .col-md{
        /* background:#bfd1e6; */
        display:flex;
        flex-direction:row;
        justify-content: flex-end;/*flex-start|flext-start|center-aroud|space-evenly|space-between;/*/

    }
</style>

```


#APLICANDO BOOTSTRAP CSS NO DJANGO FORM ATRAVES DO JAVASCRIPT
```js
// - Aplicando bootstrap css na django form

    var form =document.getElementById('form')
    for (var e in form.elements){
        // form[e.setAttribute('class','form-control')
        console.log(e)
        var el=document.getElementById(form[e].id)
        console.log(el)
        if(el!=null){
            el.setAttribute('class','form-control')
        }
        var val =document.getElementById('id_valor')
        val.setAttribute('class','form-control col-sm-3')
    }

```


#CRUD PARTE-4   DELETE

```py
contas/views.py

# Para deletar tambem 'e igual ao metodo de update 
# que necessita de um id
def delete(request,pk):
    transation =Transacoa.objects.get(pk=pk)
    transation.delete()
    return redirect('url_trans_list')

#then regist it into your urls

 /controle_gastos/urls.py
 from contas.views import delete
 path('delete_trans/',delete,name='delete_trans')
```

#Informando ao btn de delete no meu Html
```html
{% for trans in transations %}
            <tr>
            <td>{{ trans.descricao}}</td>
            <td>{{trans.valor}}</td>
            <td>{{trans.categoria}}</td>
            <td>{{trans.data}}</td>
            <td>
                <p>{{trans.observacoes}}</p>
                <div class='col col-md'>
                    <a class='btn btn-primary' href={% url 'url_update_trans' trans.id %}>Edit</a>
                    <a class='btn btn-danger' href={% url 'url_delete_trans' trans.id%}>Delete</a>
                </div>
                

            </td>
            </tr>
            {% endfor %}
```
