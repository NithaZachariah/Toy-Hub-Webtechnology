from django.shortcuts import render
from django.http import HttpResponse
from .models import Toy

def home(request):
    toy = Toy.objects.all()
    return render(request, 'Home.html',{'toy':toy})

from django.shortcuts import render
from .models import Toy  # or Product

def home(request):
    toy = Toy.objects.all()
    return render(request, 'Home.html', {'toy': toy})

def search_view(request):
    query = request.GET.get('query', '')
    results = Toy.objects.filter(name__icontains=query) if query else Toy.objects.none()
    return render(request, 'search_results.html', {'results': results, 'query': query})
