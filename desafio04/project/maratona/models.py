from django.db import models
import json

# Create your models here.
class Aulas(models.Model):
    aula_nome = models.CharField(max_length=255)
    aula_url = models.CharField(max_length=255)
    pub_dia = models.DateField('date published')

    def __str__(self):
        return self.aula_nome##json.dumps(self, default=lambda o: o.__dict__)