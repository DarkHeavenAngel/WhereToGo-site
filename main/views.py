from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def place_list(request):
    return render(request, 'main/place_list.html')

def add_place_list(request):
    return render(request, 'main/add_list.html')
