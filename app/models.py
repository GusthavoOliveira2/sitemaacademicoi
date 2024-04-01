from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100,verbose_name= "Nome da Cidade")
    uf = models.CharField(max_length=100, verbose_name= "UF")
    def __str__(self):
        return self.nome
    class Meta: 
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100,verbose_name= "Nome da Area")
    def __str__(self):
        return self.nome
    class Meta: 
        verbose_name = "AreaSaber"
        verbose_name_plural = "AreasSaberes"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100,verbose_name= "Nome da Ocupacao")
    def __str__(self):
        return self.nome
    class Meta: 
        verbose_name = "Ocupacao"
        verbose_name_plural = "Ocupacoes"

class Instituicao(models.Model):
    nome = models.CharField(max_length=100,verbose_name= "Nome da Instituicao")
    site = models.CharField(max_length=100,verbose_name= "Nome do Site")
    telefone = models.CharField(max_length=100,verbose_name= "Numero de Telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name= "Nome da Cidade")
    def __str__(self):
        return self.nome
    class Meta: 
        verbose_name = "Instituicao"
        verbose_name_plural = "Instituicoes"

class Curso(models.Model):
    nome = models.CharField(max_length=100,verbose_name= "Nome do Curso")
    carga_horaria_total = models.CharField(max_length=100,verbose_name= "Carga Horaria Total")
    duracao_meses = models.CharField(max_length=100,verbose_name= "Duracao em Meses")
    area = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name= "Nome da Area")
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name= "Nome da Instituicao")
    def __str__(self):
        return self.nome
    class Meta: 
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100,verbose_name="Nome da Pessoa")
    pai = models.CharField(max_length=100,verbose_name="Nome do Pai")
    mae = models.CharField(max_length=100,verbose_name="Nome da AMe")
    cpf = models.CharField(max_length=100,verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    email = models.CharField(max_length=100,verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name= "Nome da Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name= "Nome da Ocupacao")
    def __str__(self):
        return self.nome
    class Meta: 
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100,verbose_name= "Nome da Disciplina")
    area = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name= "Nome da Area")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name= "Nome do Curso")
    def __str__(self):
        return self.nome
    class Meta: 
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Periodo(models.Model):
    periodo = models.CharField(max_length=100,verbose_name= "Periodo")
    def __str__(self):
        return self.periodo
    class Meta: 
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"

class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name= "Nome da Instituicao")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name = "Nome do Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name = "Nome da Pessoa ")
    data_inicio = models.DateField(verbose_name= "Data de Inicio")
    data_termino = models.DateField(verbose_name= "Data de Termino")
    matricula = models.CharField(max_length=100,verbose_name= "Matricula")

    def __str__(self):
        return self.matricula
    class Meta: 
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100,verbose_name= "Descricao")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name= "Nome do Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name= "Nome da Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name= "Nome da Pessoa ")
    def __str__(self):
        return self.descricao
    class Meta: 
        verbose_name = "Avaliacao"
        verbose_name_plural = "Avaliacoes"

class DiscporCurso(models.Model):
    disc = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name= "Nome da Disciplina")
    carga_horaria = models.CharField(max_length=100,verbose_name= "Carga Horaria")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name= "Nome do Curso")
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name= "Periodo")

    def __str__(self):
        return self.carga_horaria
    
    class Meta: 
        verbose_name = "DiscporCurso"
        verbose_name_plural = "DiscsporCursos"

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name= "Nome da Curso")
    numero_de_faltas = models.CharField(max_length=100,verbose_name= "Numero de faltas")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name= "Nome da Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name= "Nome da Pessoa ")
    def __str__(self):
        return self.numero_de_faltas
    class Meta: 
        verbose_name = "Frequencia"
        verbose_name_plural = "Frequencias"

class Turma(models.Model):
    nome = models.CharField(max_length=100,verbose_name= "Nome da Turma")
    periodo = models.CharField(max_length=100,verbose_name= "Periodo")
    def __str__(self):
        return self.nome
    class Meta: 
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=100,verbose_name= "Descricao da Ocorrencia")
    data_ocorrencia = models.DateField(verbose_name= "Data da Ocorrencia")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name= "Nome da Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name= "Nome da Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name= "Nome da Pessoa ")

    def __str__(self):
        return self.descricao
    class Meta: 
        verbose_name = "Ocorrencia"
        verbose_name_plural = "Ocorrencias"

class TipoAvaliacao(models.Model):
    tipoavaliacao = models.CharField(max_length=100,verbose_name= "Tipo de Avaliacao")
    def __str__(self):
        return self.tipoavaliacao
    class Meta: 
        verbose_name = "TipoAvaliacao"
        verbose_name_plural = "TiposAvaliacoes"