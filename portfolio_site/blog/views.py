from django.shortcuts import render

from blog.models import Entry

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def portfolio(request):
    return render(request, 'blog/portfolio.html')

def contact(request):
    return render(request, 'blog/contact.html')

def blog(request):
    posts = Entry.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts,})