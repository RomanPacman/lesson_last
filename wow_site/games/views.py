from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def main_page_1(request):
    return HttpResponse('Главная страница')
