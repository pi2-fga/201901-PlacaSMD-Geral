from django.db import models

class FamiliaComponentes(models.Model):        

    nome_componente = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50)
    distancia_componentes = models.CharField(max_length=200)
    angulo = models.CharField(max_length=200)
    posicao_x_inicial = models.CharField(max_length=200)
    posicao_y_inicial = models.CharField(max_length=200)
    quantidade_componentes = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    
    def __str__(self):
        return str(self.nome_componente)
    
class Fita(models.Model):

    familia_componentes = models.ForeignKey(FamiliaComponentes, on_delete=models.CASCADE)
    numero_fita = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    posicao_x = models.CharField(max_length=200)
    posicao_y = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.numero_fita)    

class Placa(models.Model):

    nome = models.CharField(max_length=200)
    fitas = models.ManyToManyField(Fita)

    def __str__(self):
        return str(self.nome) 