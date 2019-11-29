from django.urls import path
from . import views as url_views


app_name = 'urlshortener'

urlpatterns = [
    path('', url_views.index, name='index'),
]
