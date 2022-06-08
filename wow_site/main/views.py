from django.http import HttpResponse, HttpResponseNotFound


def main_page(request):
    return HttpResponse('Главная страница')


def pages_site(request, page_id):
    print(request.GET)
    #http://127.0.0.1:8000/1/?name=roman&stepname=novash&music=rock
    return HttpResponse(f'Разные страницы <p>{page_id}</p>')

def archive(request, year):
    return HttpResponse(f'Архив по годам <p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')