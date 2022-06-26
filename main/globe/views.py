from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import anime
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "home.html")


def anime_search(request):
    query = request.GET.get('q')
    
    objlist = anime.objects.filter(Q(Anime__icontains = query) | Q(Animejap__icontains = query))
    return render(request, "anime_search.html", {'objlist':objlist})
    



def display(request):
    gla = anime.objects.all()
    paginator = Paginator(gla, 5) 

    page_number = request.GET.get('page')
    gl = paginator.get_page(page_number)
    return render(request, "result.html", {'gl': gl})

