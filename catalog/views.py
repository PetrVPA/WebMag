from django.shortcuts import render


def home(request):
    return render(request, 'home.html')#папка template для файлов страниц программы по умолчанию и не указ

def contacts(request):
    return render(request, 'contacts.html')

