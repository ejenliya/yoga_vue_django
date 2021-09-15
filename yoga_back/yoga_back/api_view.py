from django.shortcuts import render

def apidoc(request):
    return render(request, 'doc/index.html')