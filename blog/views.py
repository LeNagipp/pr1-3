from django.http import HttpResponse

POSTS = [
    {
        'id': 1,
        'title': 'Вступ до Django',
        'slug': 'vstup-do-django',
        'content': 'Django - це чудовий веб-фреймворк на Python...',
        'category': 'python',
        'author': 'Іван',
        'date': '2025-01-15'
    },
    {
        'id': 2,
        'title': 'Основи Python',
        'slug': 'osnovy-python',
        'content': 'Python - одна з найпопулярніших мов програмування...',
        'category': 'python',
        'author': 'Марія',
        'date': '2025-01-10'
    },
    {
        'id': 3,
        'title': 'HTML та CSS',
        'slug': 'html-ta-css',
        'content': 'HTML використовується для структури, CSS - для стилів...',
        'category': 'web',
        'author': 'Петро',
        'date': '2025-01-20'
    },
    {
        'id': 4,
        'title': 'JavaScript для початківців',
        'slug': 'javascript-dlya-pochatkivtsiv',
        'content': 'JavaScript робить веб-сторінки інтерактивними...',
        'category': 'web',
        'author': 'Олена',
        'date': '2024-12-25'
    },
    {
        'id': 5,
        'title': 'Робота з базами даних',
        'slug': 'robota-z-bazamy-danyh',
        'content': 'Бази даних зберігають інформацію...',
        'category': 'database',
        'author': 'Іван',
        'date': '2024-11-30'
    },
]


def index(request):
    query_author = request.GET.get('q')

    if query_author:
        results = [p for p in POSTS if p['author'].lower() == query_author.lower()]
    else:
        results = POSTS

    output = "<h1>Всі статті блогу</h1>"
    if query_author:
        output = f"<h1>Статті автора: {query_author}</h1>"

    for post in results:
        output += f"""
            <div>
                <h3><a href="/blog/{post['id']}/">{post['title']}</a></h3>
                <p>Категорія: {post['category']} | Дата: {post['date']}</p>
                <hr>
            </div>
        """
    return HttpResponse(output)


def post_detail(request, post_id):
    post = next((p for p in POSTS if p['id'] == post_id), None)

    if post:
        return HttpResponse(f"""
            <h1>{post['title']}</h1>
            <p><b>Автор:</b> {post['author']} | <b>Дата:</b> {post['date']}</p>
            <p><b>Категорія:</b> {post['category']}</p>
            <div>{post['content']}</div>
            <br>
            <a href="/blog/">Повернутися до списку</a>
        """)
    else:
        return HttpResponse("<h2>Статтю не знайдено</h2>", status=404)


from django.shortcuts import render

# Create your views here.
