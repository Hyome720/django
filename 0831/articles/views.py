from django.shortcuts import render, redirect
from .models import articleModel

import articles

# Create your views here.

def index(request):
    articles = articleModel.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    
    article = articleModel(name=name, age=age)
    article.save()
    
    return redirect('articles:index')

def new(request):
    return render(request, 'articles/new.html')

def edit(request, pk):
    article = articleModel.objects.get(pk=pk)
    context = {
        'article': article,
    }
    
    return render(request, 'articles/edit.html', context)

def detail(request, pk):
    article = articleModel.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
    
def update(request, pk):
    article = articleModel.objects.get(pk=pk)
    article.name = request.POST.get('name')
    article.age = request.POST.get('age')
    article.save()
    
    return redirect('articles:detail', article.pk)
    
def delete(request, pk):
    article = articleModel.objects.get(pk=pk)
    article.delete()
    
    return redirect('articles:index')
    