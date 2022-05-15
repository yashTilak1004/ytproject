from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'My first blog',
        'title': 'blog',
        'content': 'This is a blog on django',
        'date_posted': '10th April 2022'
    }
]


def home(request):
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
    # return render(request, 'home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
