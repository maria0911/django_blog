from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'Maria',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '27 December 2020'},
    {
        'author': 'Jane',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '28 December 2020'}
    ]

def home(request):
    context = {
        'posts': posts
        }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

