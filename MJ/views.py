from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def feedback(request):
    return render(request, 'feedback.html')

def menu(request):
    return render(request, 'menu.html')