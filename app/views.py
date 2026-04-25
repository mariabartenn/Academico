from django.shortcuts import render
from django.views import View
from .models import *

# View Principal (Dashboard) [cite: 443, 622]
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

# RF01 - Gerenciar Pessoas [cite: 6, 653]
class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoas.html', {'pessoas': pessoas})

# RF05 - Gerenciar Cursos [cite: 7, 624]
class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'cursos.html', {'cursos': cursos})

# RF03 - Gerenciar Instituições de Ensino [cite: 6]
class InstituicoesView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = InstituicaoEnsino.objects.all()
        return render(request, 'instituicoes.html', {'instituicoes': instituicoes})

# RF07/RF14 - Gerenciar Disciplinas e sua relação com Cursos 
class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        # Para o RF14, podemos passar também a relação CursoDisciplina
        relacoes = CursoDisciplina.objects.all()
        return render(request, 'disciplinas.html', {
            'disciplinas': disciplinas,
            'relacoes': relacoes
        })

# RF08 - Gerenciar Matrículas [cite: 7]
class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matriculas.html', {'matriculas': matriculas})

# RF09 - Gerenciar Avaliações [cite: 7]
class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})

# RF13 - Gerenciar Ocorrências [cite: 8]
class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias})