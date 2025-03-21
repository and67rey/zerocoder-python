from .models import Films
from django.forms import ModelForm, TextInput, Textarea

class FilmsForm(ModelForm):
    class Meta:
        model = Films
        fields = ['name', 'description', 'review']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание фильма', 'rows': 8}),
            'review': Textarea(attrs={'class': 'form-control', 'placeholder': 'Обзор фильма', 'rows': 8})
        }