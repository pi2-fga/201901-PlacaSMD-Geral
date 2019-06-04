from django.db import models

class Fita(models.Model):

    numero_fita = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    posicao_x = models.CharField(max_length=200)
    posicao_y = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.numero_fita)

class FamiliaComponentes(models.Model):        

    fita = models.ForeignKey(Fita, on_delete=models.CASCADE)
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
    