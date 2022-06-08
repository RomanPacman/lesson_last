from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', main_page, name='home'),
    path('<int:page_id>/', pages_site),
    re_path(r'archive/(?P<year>[0-9]{4}/', archive),

]
