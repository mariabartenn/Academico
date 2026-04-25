from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome} ({self.uf})"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Ocupação")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class Pessoa(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome")
    pai = models.CharField(max_length=150, verbose_name="Nome do Pai", blank=True, null=True)
    mae = models.CharField(max_length=150, verbose_name="Nome da Mãe")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    email = models.EmailField(verbose_name="E-mail")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Instituição")
    site = models.URLField(verbose_name="Site")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Área do Saber")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"

class Curso(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Curso")
    carga_horaria_total = models.IntegerField(verbose_name="Carga Horária Total")
    duracao_meses = models.IntegerField(verbose_name="Duração (Meses)")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área")
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class Turno(models.Model): # RF11 
    nome = models.CharField(max_length=50, verbose_name="Turno")

    def __str__(self):
        return self.nome

class Turma(models.Model): # RF06 
    nome = models.CharField(max_length=100, verbose_name="Nome da Turma")
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name="Turno", null=True)

    def __str__(self):
        return self.nome

class Disciplina(models.Model): # RF07 
    nome = models.CharField(max_length=100, verbose_name="Disciplina")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área")

    def __str__(self):
        return self.nome

class CursoDisciplina(models.Model): # RF14 
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    carga_horaria = models.IntegerField(verbose_name="Carga Horária")
    periodo = models.CharField(max_length=50, verbose_name="Período")

class Matricula(models.Model): # RF08 
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_previsao_termino = models.DateField(verbose_name="Previsão de Término")

class AvaliacaoTipo(models.Model): # RF15 
    nome = models.CharField(max_length=100, verbose_name="Tipo de Avaliação")

    def __str__(self):
        return self.nome

class Avaliacao(models.Model): # RF09 
    descricao = models.TextField(verbose_name="Descrição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE, verbose_name="Tipo")

class Frequencia(models.Model): # RF10 
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    numero_faltas = models.IntegerField(verbose_name="Número de Faltas")

class Ocorrencia(models.Model): # RF13 
    descricao = models.TextField(verbose_name="Descrição")
    data = models.DateField(verbose_name="Data")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")