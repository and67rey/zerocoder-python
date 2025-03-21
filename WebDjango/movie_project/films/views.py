from django.shortcuts import render
from .models import Films
from .forms import FilmsForm

def index(request):
    films = Films.objects.all()
    return render(request, 'films/index.html', {'films': films})

def create_form(request):
    error = ""
    if request.method == 'POST':
        form = FilmsForm(request.POST)  # Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()
        else:
            error = "Данные были заполнены некорректно"
    form = FilmsForm()
    return render(request, 'films/create_form.html', {'form': form, 'error': error})