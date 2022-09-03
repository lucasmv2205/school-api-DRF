from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
  list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
  list_display_link = ('id', 'nome')
  search_fields = ('nome',)
  list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
  list_display = ('id', 'codigo', 'descricao')
  list_display_link = ('id', 'codigo')
  search_fields = ('codigo',)

admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):
  list_display = ('id', 'aluno', 'curso', 'periodo')
  list_display_link = ('id')

admin.site.register(Matricula, Matriculas)