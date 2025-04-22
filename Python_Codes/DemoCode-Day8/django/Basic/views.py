# myapp/views.py
from django.shortcuts import render
def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

# from django.http import HttpResponse
#
# def home(request):
#     return HttpResponse("Hello, Django!")  # This is the first screen
# def about(request):
#     return HttpResponse("This is the About page!")  # New screen

