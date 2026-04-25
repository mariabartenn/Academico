from django.contrib import admin
from .models import *

# --- DEFINIÇÃO DOS INLINES (Requisitos de i a ix do arquivo) ---

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class OcorrenciaInline(admin.TabularInline):
    model = Ocorrencia
    extra = 1

# --- CONFIGURAÇÃO DAS CLASSES ADMIN COM OS INLINES ---

@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline] # i. Gerenciar Pessoas por Ocupação

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    inlines = [PessoaInline] # ii. Gerenciar Pessoas por Cidade

@admin.register(InstituicaoEnsino)
class InstituicaoAdmin(admin.ModelAdmin):
    inlines = [CursoInline, MatriculaInline] # iii. Gerenciar Cursos por Instituição

@admin.register(AreaSaber)
class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoInline] # iv. Gerenciar Cursos por Área do Saber

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline, MatriculaInline, AvaliacaoInline, OcorrenciaInline] 
    # v. Disciplinas por Curso | vi. Matrículas por Curso | viii. Avaliações por Curso

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline, AvaliacaoInline, FrequenciaInline, OcorrenciaInline]
    # vii. Avaliações por Disciplina | ix. Frequência por Disciplina

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline, FrequenciaInline, OcorrenciaInline]
    # Gerencia tudo que está ligado à pessoa diretamente

# --- REGISTROS SIMPLES (Para o que não precisa de Inline customizado) ---

admin.site.register(Turno)
admin.site.register(Turma)
admin.site.register(AvaliacaoTipo)
admin.site.register(CursoDisciplina)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)