from django.db import models
from django.contrib.auth.models import User


class Residencia(models.Model):
    numero = models.IntegerField(unique=True, primary_key=True)
    dueño = models.CharField(max_length=50)
    telefono = models.IntegerField()
    mail = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Residencia {self.numero}"


class Correspondecia(models.Model):
    fechaRecepcion = models.DateField()
    conserje = models.ForeignKey(User, limit_choices_to={'groups__name': "Conserjes"}, on_delete=models.SET_NULL,
                                 null=True, blank=True)
    remitente = models.CharField(max_length=50)
    destinatario = models.CharField(max_length=50)
    estados = [('R', 'Recibido'),
               ('N', 'No Recibido'), ]
    estado = models.CharField(max_length=1, choices=estados)
    residencia = models.ForeignKey(Residencia, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"Correspondencia de {self.residencia} para {self.destinatario}"
