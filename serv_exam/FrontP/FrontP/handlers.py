# handlers.py

from django.shortcuts import render

def custom_handler404(request, exception):
    return render(request, '404.html', status=404)
