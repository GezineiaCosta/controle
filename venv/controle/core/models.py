from django.db import models

# Create your models here.

class Professor(models.Model):
    Nome = models.CharField(max_length=100)
    codigo_prof = models.DecimalField(max_digits=4, decimal_places=0)
    Exeperiencia_profissional = models.CharField('experiencia', max_length=200)
    Hora_aula = models.TimeField('Tempo', auto_now=True)
    Disponibilidade = models.TextField(max_length=100)

class Disciplina(models.Model):
    Nome_Disciplina = models.TextField(max_length=25)
    codigo_disciplina = models.DecimalField(max_digits=4, decimal_places=0)
    carga_horaria = models.TimeField()

class Professor_Disciplina(models.Model):
    codigo_prof = models.DecimalField(max_digits=4, decimal_places=0)
    codigo_disciplina = models.DecimalField(max_digits=4, decimal_places=0)
    nome_curso = models.CharField(max_length=20)
    semestre = models.DecimalField(max_digits=4, decimal_places=0)

