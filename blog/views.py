from django.shortcuts import render


posts = [
    {
        'author': 'AndreiGNT',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '24/07/2023'
    },
    {
        'author': 'Elena',
        'title': 'Second Post',
        'content': 'Second Post content',
        'date_posted': '24/07/2023'
    }
]

def home(request):
    template_name = 'blog/home.html'
    context = {
        'posts': posts
    }
    return render(request, template_name, context)


def about(request):
    template_name = 'blog/about.html'
    return render(request, template_name)