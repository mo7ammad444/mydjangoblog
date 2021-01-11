from django.shortcuts import render
from django.shortcuts import HttpResponse


def about(request):
    # return HttpResponse('we will succeed')
    return render(request,'about.html')

def home(request):
    return render(request,'home.html')