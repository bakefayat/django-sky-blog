from django.shortcuts import render

def handler404(request, exception):
    return render(request, "exception_handling/404.html")

def handler500(request):
    return render(request, "exception_handling/500.html")
