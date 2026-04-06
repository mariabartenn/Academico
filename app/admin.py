from django.contrib import admin
from .models import Aluno, Professor, Pessoa, Cidade, Curso, Disciplina, Matricula, Frequencia, Ocorrencia, InstituicaoEnsino, CursoDisciplina, Avaliacao, AvaliacaoTipo, AreaSaber, Ocupacao, Turma

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(AreaSaber)

admin.site.register(Pessoa)
admin.site.register(Aluno)
admin.site.register(Professor)

admin.site.register(InstituicaoEnsino, InstituicaoAdmin)

admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Disciplina)
admin.site.register(CursoDisciplina)

admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(AvaliacaoTipo)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)