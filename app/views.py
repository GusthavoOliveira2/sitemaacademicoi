from django.shortcuts import render
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass

class CidadeView(View):
    def get(self,request,*args,**kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'Cidade.html', {'cidades':cidades})
    def post(self, request):
        pass

class AreaSaberView(View):
    def get(self,request,*args,**kwargs):
        areassaberes= AreaSaber.objects.all()
        return render(request, 'AreaSaber.html', {'areassaberes':areassaberes})
    def post(self, request):
        pass

class OcupView(View):
    def get(self,request,*args,**kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'Ocupacao.html', {'ocupacoes':ocupacoes})
    def post(self, request):
        pass

class InstitView(View):
    def get(self,request,*args,**kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, 'Instituicao.html', {'instituicoes':instituicoes})
    def post(self, request):
        pass

class CursoView(View):
    def get(self,request,*args,**kwargs):
        cursos = Curso.objects.all()
        return render(request, 'Curso.html', {'cursos':cursos})
    def post(self, request):
        pass

class PessoaView(View):
    def get(self,request,*args,**kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'Pessoa.html', {'pessoas':pessoas})
    def post(self, request):
        pass

class DiscView(View):
    def get(self,request,*args,**kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'Disciplina.html', {'disciplinas':disciplinas})
    def post(self, request):
        pass

class PeriodoView(View):
    def get(self,request,*args,**kwargs):
        periodos= Periodo.objects.all()
        return render(request, 'Periodo.html', {'periodos':periodos})
    def post(self, request):
        pass

class MatricView(View):
    def get(self,request,*args,**kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'Matricula.html', {'matriculas':matriculas})
    def post(self, request):
        pass

class AvalView(View):
    def get(self,request,*args,**kwargs):
        avaliacoes= Avaliacao.objects.all()
        return render(request, 'Avaliacao.html', {'avaliacoes':avaliacoes})
    def post(self, request):
        pass

class DiscporCursoView(View):
    def get(self,request,*args,**kwargs):
        disccursos= DiscporCurso.objects.all()
        return render(request, 'DiscporCurso.html', {'disccursos':disccursos})
    def post(self, request):
        pass

class FrequenciaView(View):
    def get(self,request,*args,**kwargs):
        frequencias= Frequencia.objects.all()
        return render(request, 'Frequencia.html', {'frequencias':frequencias})
    def post(self, request):
        pass

class TurmaView(View):
    def get(self,request,*args,**kwargs):
        turmas= Turma.objects.all()
        return render(request, 'Turma.html', {'turmas':turmas})
    def post(self, request):
        pass

class OcorrenciaView(View):
    def get(self,request,*args,**kwargs):
        ocorrencias= Ocorrencia.objects.all()
        return render(request, 'Ocorrencia.html', {'ocorrencias':ocorrencias})
    def post(self, request):
        pass

class TipoAvalView(View):
    def get(self,request,*args,**kwargs):
        tipoavals= TipoAvaliacao.objects.all()
        return render(request, 'TipoAval.html', {'tipoavals':tipoavals})
    def post(self, request):
        pass