from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
    
class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7,decimal_places=2) #decimal_place=> o nr de digitos que vem depois da virgula
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    observacoes = models.TextField(null=True,blank=True) #campo nao obrigatorio
    
    def __str__(self):
        return self.descricao
    # pra definir a designacoa em plural do meu model 
    # preciso definir uma classe MetaData dentro da minha class model
    # e nela passar atributo verbose_name_plural='transacoes'
    class Meta:
        verbose_name_plural='Transacoes'
    
    