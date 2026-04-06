from django.db import models


# RF12 - Cidade
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} - {self.uf}"


# RF02 - Ocupação
class Ocupacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# RF01 - Pessoa
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField()
    email = models.EmailField()

    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# RF03 - Instituição
class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# RF04 - Área do Saber
class AreaSaber(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# RF05 - Curso
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()

    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# RF06 - Turma
class Turma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# RF07 - Disciplina
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# RF15 - Tipo de Avaliação
class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# RF08 - Matrícula
class Matricula(models.Model):
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

    def __str__(self):
        return f"{self.pessoa} - {self.curso}"


# RF09 - Avaliação
class Avaliacao(models.Model):
    descricao = models.CharField(max_length=200)

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao


# RF10 - Frequência
class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    numero_faltas = models.IntegerField()

    def __str__(self):
        return f"{self.pessoa} - {self.disciplina}"


# RF11 - Turno
class Turno(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


# RF13 - Ocorrência
class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=200)
    data = models.DateField()

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao


# RF14 - CursoDisciplina
class CursoDisciplina(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    carga_horaria = models.IntegerField()
    periodo = models.IntegerField()

    def __str__(self):
        return f"{self.curso} - {self.disciplina}"