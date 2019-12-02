from django.urls import path
from . import views as url_views


app_name = 'urlshortener'

urlpatterns = [
    path('unknown-url/', url_views.unknown_url, name='unknown_url'),
    path('<url_id>/', url_views.get_url, name='get_url'),
    path('', url_views.index, name='index'),
]
