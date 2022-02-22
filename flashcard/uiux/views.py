from django.http import HttpResponse
from django.shortcuts import render

# data.html uses ajax to send a RESTFUL API request.
def data(request):
    return render(request , 'frontend/data.html')