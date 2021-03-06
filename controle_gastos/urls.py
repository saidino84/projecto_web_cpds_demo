"""controle_gastos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


# importando o meu view home 
from contas.views import home,transations_list, nova_transacao,update,delete

admin.site.site_header='Administração - Associação Provincial para Desenvolvimento Sustentável  de Cabo Delgado'
admin.site.site_title='Administração Da Associação Provincial para Desenvolvimento Sustentável  de Cabo Delgado'
admin.site.index_title='Seja Bem-Vindo Da Associação Provincial para Desenvolvimento Sustentável  de Cabo Delgado'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home,name='url_home'),
    path('',transations_list,name='url_trans_list'),
    path('add_trans/',nova_transacao,name='url_add_new_trans'),
    # recebera um id de transacao
    path('update_trans/<int:pk>/', update, name='url_update_trans'),
    path('delete_trans/<int:pk>/',delete,name='url_delete_trans')
    
]

# EStrutura do projecto