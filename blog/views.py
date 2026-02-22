from django.http import HttpResponse

POSTS = [
    {'id': 1, 'title': 'Вступ до Django', 'author': 'Іван'},
    {'id': 2, 'title': 'Робота з Views', 'author': 'Марія'},
    {'id': 3, 'title': 'Маршрутизація в Django', 'author': 'Іван'},
]


def index(request):
    query_author = request.GET.get('q')
    results = POSTS

    if query_author:
        results = [post for post in POSTS if post['author'].lower() == query_author.lower()]

    output_text = "<h1>Список статей:</h1>"
    if not results:
        output_text += "<p>Статей цього автора не знайдено.</p>"

    for post in results:
        output_text += f"<p>ID: {post['id']} | <b>{post['title']}</b> | Автор: {post['author']}</p>"

    return HttpResponse(output_text)


def post_detail(request, post_id):
    current_post = None
    for post in POSTS:
        if post['id'] == post_id:
            current_post = post
            break

    if current_post:
        return HttpResponse(f"<h1>{current_post['title']}</h1><p>Автор: {current_post['author']}</p>")
    else:
        return HttpResponse("Статтю не знайдено", status=404)


from django.shortcuts import render

# Create your views here.
