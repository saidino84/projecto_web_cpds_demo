from django.shortcuts import render
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
    form =TransacaoForm()
    
    return render(request, 'contas/form.html',{'form':form})