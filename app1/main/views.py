from django.http import HttpResponse
from django.shortcuts import render

# Здесь записываются функции или классы, которые обрабатывают запросы от пользователей

# представление(контроллер)
def index(request):  # вся информация о запросе хранится в запросе 
  # (в него попадает экз класса httpRequest, который содержит в себе все данные о запросе: какой пользователь - 
  # аноним/зарегистрированный, файлы куки, метод запроса (get/post))
  return HttpResponse('Home page')


def about(request):
    return HttpResponse('About page')