from django.http import HttpResponse


def index(request):
    return HttpResponse("Головна сторінка")


def about(request):
    return HttpResponse("Тут буде інформація про нас")


def contact(request):
    return HttpResponse("Тут будуть наші контакти")


from django.shortcuts import render

# Create your views here.
