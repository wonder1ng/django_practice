from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def hello_world(request):
#     return HttpResponse('Hello world!')

# def hello_world(request):
#     return render(request, 'base.html')

def hello_world(request):
    return render(request, 'accountapp/hello_world.html')