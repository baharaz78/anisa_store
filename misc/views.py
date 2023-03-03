from django.shortcuts import render
from django.http import HttpResponse

def aboutus(request):
    if request.method == 'GET':
        ...
    elif request.method == 'POST':
        ...
    return render(request, 'misc/aboutus.html')