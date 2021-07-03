from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

#:TODO [DEPRECATED]
# def home(request):
#     now=datetime.datetime.now()
#     html = f'<html><body> The time is {now}</body></html>'
#     return HttpResponse(html)


# usando TEMPLATES
def home(request):
    now=datetime.datetime.now()
    
    
    return render(request, 'contas/home.html')