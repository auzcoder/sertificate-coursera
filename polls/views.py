from django.shortcuts import render

from django.http import HttpResponse

# 1-labaratoriya
# def index(request):
#     return HttpResponse("Hello, world. 3dacafbf is the polls index.")

def index(request):
    return render(request, 'index.html')
