from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def blog(request):
    return render(request, 'main/blog.html')

def team(request):
    return render(request, 'main/team.html')

def contacts(request):
    return render(request, 'main/contacts.html')
