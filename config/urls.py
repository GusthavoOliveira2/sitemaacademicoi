"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('cidades/', CidadeView.as_view(), name='cidades'),
    path('areassaber/', AreaSaberView.as_view(), name='areassaber'),
    path('ocupacoes/', OcupView.as_view(), name='ocupacoes'),
    path('instituicoes/', InstitView.as_view(), name='instituicoes'),
    path('cursos/', CursoView.as_view(), name='cursos'),
    path('pessoas/', PessoaView.as_view(), name='pessoas'),
    path('disciplinas/', DiscView.as_view(), name='disciplinas'),
    path('periodos/', PeriodoView.as_view(), name='periodos'),
    path('matriculas/', MatricView.as_view(), name='matriculas'),
    path('avaliacoes/', AvalView.as_view(), name='avaliacoes'),
    path('disciplinasporcurso/', DiscporCursoView.as_view(), name='disciplinascurso'),
    path('frequencias/', FrequenciaView.as_view(), name='frequencias'),
    path('turmas/', TurmaView.as_view(), name='turmas'),
    path('ocorrencias/', OcorrenciaView.as_view(), name='ocorrencias'),
    path('tipoavals/', TipoAvalView.as_view(), name='tipoavals'),
   
    
]
