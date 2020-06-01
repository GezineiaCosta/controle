from django.db import models

# Create your models here.

class Professor(models.Model):
    Nome = models.CharField(max_length=100)
    codigo_prof = models.CharField(max_length=10)
    Exeperiencia_profissional = models.CharField('experiencia', max_length=200)
    Hora_aula = models.TimeField('Tempo', auto_now=True)
    Disponibilidade = models.TextField(max_length=150)

class Disciplina(models.Model):
    Nome_Disciplina = models.TextField(max_length=50)
    codigo_disciplina = models.CharField(max_length=10)
    carga_horaria = models.TimeField()



