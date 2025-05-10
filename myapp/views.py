from django.shortcuts import render, HttpResponse






def index(request):
    return HttpResponse("Welcome to the index page!")

def page2(request):
    return HttpResponse("This is page 2.")

def page3(request):
    return HttpResponse("This is page 3.")



def index(request):
    return render(request, 'index.html')  # or another template name if different
