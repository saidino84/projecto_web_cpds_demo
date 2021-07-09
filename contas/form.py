from django.forms import ModelForm,TextInput,DateInput
from .models import Transacao
llkk
class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data','descricao','valor','categoria','observacoes']
 
    widgets={
        'valor':TextInput(attrs={'class':'form-control'}),
        'data':DateInput(attrs={'class':'form-control'}),
        'categoria':TextInput(attrs={'class':'form-control'}),
        'observacoes':TextInput(attrs={'class':'form-control'})
             }
        
"""esse formulario exigira esses atributos obrigatorios

data = models.DateTimeField()
descricao = models.CharField(max_length=200)
valor = models.DecimalField(max_digits=7,decimal_places=2) #decimal_place=> o nr de digitos que vem depois da virgula
categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
observacoes = models.TextField(null=True,blank=True) #campo nao obrigatorio


"""   
    