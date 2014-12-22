from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def portfolio(request):
    return render(request, 'blog/portfolio.html')

def contact(request):
    return render(request, 'blog/contact.html')

def blog(request):
    return render(request, 'blog/blog.html')