from django.shortcuts import redirect, render
from .form import TransacaoForm

# Create your views here.
from django.http import HttpResponse
import datetime
from .models import Transacao
#:TODO [DEPRECATED]
# def home(request):
#     now=datetime.datetime.now()
#     html = f'<html><body> The time is {now}</body></html>'
#     return HttpResponse(html)
# usando TEMPLATES
def home(request):
    data={}
    data['now']=datetime.datetime.now()
    print(data['now'])
    data['transactions']=[
        {'date':'12/04/2020-23:12:08','mount':1200,'name':'saidino','category':'admin'},
        {'date':'10/07/2021-13:52:08','mount':100,'name':'hacker','category':'user'},
        {'date':'22/01/2021-11:15:08','mount':1700,'name':'benny','category':'admin'},
        {'date':'2/04/2020-21:32:08','mount':890,'name':'benildo','category':'hacker'},
        {'date':'12/04/2021-3:12:08','mount':120,'name':'joaquim','category':'admin'}
        ,{'date':'12/04/2021-3:12:8','mount':1120,'name':'Claudia','category':'root'}
        ]
    # posso passar esses dados como parametro e serem recebidos la no meu template Html
    
    return render(request, 'contas/home.html',data)

def transations_list(request):
    data={}
    data['transations']=Transacao.objects.all()
    #objects.filter/objects...
    print(data['transations'])   
    return render(request, 'contas/transations_list.html',data)



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


def update(request,pk):
    # transation=Transacao.objects.filter(pk=pk) #pega mais k um objecto
    transation=Transacao.objects.get(pk=pk) 
    
    
    # aqui instacio um formulario preechendoos campos do query acima ai transation
    # que pegarei atraveis da filtracao do seu primary_key
    # aqui vou preencher o form os dados que foram retornados
    form =TransacaoForm(request.POST or None, instance=transation)
    
    if form.is_valid():
        form.save()
        return redirect('url_trans_list')
    
    return render(request,'contas/form.html',{'form':form})


def delete(request,pk):
    transation=Transacao.objects.get(pk=pk)
    
    transation.delete()
    return redirect('url_trans_list')