from django.http import HttpResponse

from django.shortcuts import render, redirect

POSTS = [
    {'id': 1, 'title': 'Вступ до Django', 'content': '...', 'category': 'python', 'author': 'іван',
     'date': '2025-01-15'},
    {'id': 2, 'title': 'Основи Python', 'content': '...', 'category': 'python', 'author': 'марія',
     'date': '2025-01-10'},
    {'id': 3, 'title': 'HTML та CSS', 'content': '...', 'category': 'web', 'author': 'петро', 'date': '2025-01-20'},
]


COMMENTS = [
    {'post_id': 1, 'author': 'Олексій', 'text': 'Дуже корисно!'},
]


def index(request):
    return render(request, 'blog/index.html', {'posts': POSTS})


def post_detail(request, post_id):
    post = next(filter(lambda p: p['id'] == post_id, POSTS), None)

    if post is None:
        return render(request, 'blog/404.html', status=404)

    post_comments = list(filter(lambda c: c['post_id'] == post_id, COMMENTS))

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': post_comments,
    })


def category_posts(request, category_name):
    posts = list(filter(lambda p: p['category'] == category_name, POSTS))
    return render(request, 'blog/category.html', {
        'category_name': category_name,
        'posts': posts,
    })

from django.shortcuts import render

# Create your views here.
