from django.contrib import admin
from core.models import Professor, Disciplina

# Register your models here.

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Exeperiencia_profissional', 'Disponibilidade')

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('Nome_Disciplina', 'carga_horaria')
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
