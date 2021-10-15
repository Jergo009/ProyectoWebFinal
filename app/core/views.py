from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from core.models import Category, Product


def myfirstview(request):
    data = {
        'name': 'William',
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', data)

def mysecondview(request):
    data = {
        'name': 'William',
        'categories': Category.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'second.html', data)