from django.db import models

# Create your models here.

class car(models.Model):
    placa = models.CharField(max_length=7)
    modelo = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    diaria = models.IntegerField()

    class Meta:
        db_table = 'car'

class rentacar(models.Model):
    data_criacao = models.DateTimeField(auto_now=True)
    data_agendamento = models.DateTimeField()
    dias_agendados = models.IntegerField()
    car = models.ForeignKey(car, on_delete=models.CASCADE)

    class Meta:
        db_table = 'rentacar'
