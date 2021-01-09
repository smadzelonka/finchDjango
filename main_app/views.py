from django.shortcuts import render
from .models import Finch

# Create your views here.


def home(req):
    return render(req, 'home.html')


def about(req):
    return render(req, 'about.html')


def finches_index(req):
    finches = Finch.objects.all()
    context = {'finches': finches}
    return render(req, 'finches/index.html', context)
