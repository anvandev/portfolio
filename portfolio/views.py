from django.shortcuts import render, get_object_or_404
from . models import Info


def home(request):
    about_me = get_object_or_404(Info, id=1)
    return render(request, 'portfolio/home.html', {'about_me': about_me})


def portfolio(request):
    return render(request, 'portfolio/portfolio.html')


def resume(request):
    return render(request, 'portfolio/resume.html')
