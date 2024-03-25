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
        cidades = Cidade.object.all()
        return render(request, 'cidade.html', {'cidades':cidades})
    def post(self, request):
        pass

# class View(View):
#     def get(self,request,*args,**kwargs):
#         = .object.all()
#         return render(request, '.html', {'':})
#     def post(self, request):
#         pass

# class View(View):
#     def get(self,request,*args,**kwargs):
#         = .object.all()
#         return render(request, '.html', {'':})
#     def post(self, request):
#         pass

# class View(View):
#     def get(self,request,*args,**kwargs):
#         = .object.all()
#         return render(request, '.html', {'':})
#     def post(self, request):
#         pass

# class View(View):
#     def get(self,request,*args,**kwargs):
#         = .object.all()
#         return render(request, '.html', {'':})
#     def post(self, request):
#         pass

# class View(View):
#     def get(self,request,*args,**kwargs):
#         = .object.all()
#         return render(request, '.html', {'':})
#     def post(self, request):
#         pass

# class View(View):
#     def get(self,request,*args,**kwargs):
#         = .object.all()
#         return render(request, '.html', {'':})
#     def post(self, request):
#         pass

# class View(View):
#     def get(self,request,*args,**kwargs):
#         = .object.all()
#         return render(request, '.html', {'':})
#     def post(self, request):
#         pass

# class View(View):
#     def get(self,request,*args,**kwargs):
#         = .object.all()
#         return render(request, '.html', {'':})
#     def post(self, request):
#         pass

# class View(View):
#     def get(self,request,*args,**kwargs):
#         = .object.all()
#         return render(request, '.html', {'':})
#     def post(self, request):
#         pass

# class View(View):
#     def get(self,request,*args,**kwargs):
#         = .object.all()
#         return render(request, '.html', {'':})
#     def post(self, request):
#         pass

# class View(View):
#     def get(self,request,*args,**kwargs):
#         = .object.all()
#         return render(request, '.html', {'':})
#     def post(self, request):
#         pass

# class View(View):
#     def get(self,request,*args,**kwargs):
#         = .object.all()
#         return render(request, '.html', {'':})
#     def post(self, request):
#         pass

# class View(View):
#     def get(self,request,*args,**kwargs):
#         = .object.all()
#         return render(request, '.html', {'':})
#     def post(self, request):
#         pass

# class View(View):
#     def get(self,request,*args,**kwargs):
#         = .object.all()
#         return render(request, '.html', {'':})
#     def post(self, request):
#         pass