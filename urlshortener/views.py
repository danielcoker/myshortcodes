from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UrlForm
from django.contrib import messages
from .models import Url


def index(request):
    if request.method == 'POST':
        url_form = UrlForm(data=request.POST)

        if url_form.is_valid():
            url_object = url_form.save()
            messages.info(request, url_object.short())

            return redirect(request.path_info)
    else:
        url_form = UrlForm()
        
    return render(request, 'urlshortener/home.html', {'url_form':url_form})


def get_url(request, url_id):
    try:
        url_object = Url.objects.get(url_id=url_id)
        return redirect(url_object.long())
    except Url.DoesNotExist:
        return redirect('urlshortener:unknown_url')


def unknown_url(request):
    return render(request, 'urlshortener/unknown_url.html')
