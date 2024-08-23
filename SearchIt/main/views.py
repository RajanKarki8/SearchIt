from django.shortcuts import render, redirect
from .models import Item
from django.db.models import Q
from django.http import HttpResponse

def home(request):
    items = Item.objects.all()
    context = {
        'items':items
    }
    return render(request, 'main/home.html', context)


def SearchItem(request):
    
    query = request.GET['query'] if 'query' in request.GET else '' 
    items = Item.objects.filter(
        Q(name__icontains = query)|
        Q(about__icontains = query)|
        Q(image__icontains = query))
    context = {'query':query , 'items':items}
    return render(request, 'main/search.html', context)