from django.db import models

# Create your models here.
class Email(models.Model):
    E_identificador = models.IntegerField()
    E_codigo = models.IntegerField()
    E_EMAIL = models.CharField(max_length=100)