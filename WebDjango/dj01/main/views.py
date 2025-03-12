from django.http import HttpResponse

def index(request):
    content = """
    <h1>Это мой первый проект на Django</h1>
    <p>По адресу /data можно перейти на страницу с данными</p>
    <p>По адресу /text можно перейти на страницу с текстом</p>
    """
    return HttpResponse(content)

def data(request):
    return HttpResponse("<h2>Это страница с данными</h1>")

def text(request):
    return HttpResponse("<h2>Это страница с текстом</h1>")