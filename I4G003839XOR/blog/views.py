from django.shortcuts import render
from .models import Post

# Create your views here.

posts = [
    {
    'author': 'Gbengarock',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'created_date': 'June 18, 2022',
    'published_date': 'June 19, 2022'
    },
    {
    'author': 'Zuri',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'created_date': 'June 19, 2022',
    'published_date': 'June 20, 2022'
    },
    
]



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
