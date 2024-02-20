from django.http import HttpResponse
from django.shortcuts import render  # render - для отрисовки html страницы

# Здесь записываются функции или классы, которые обрабатывают запросы от пользователей

# представление(контроллер)
def index(request):  # вся информация о запросе хранится в запросе 
  # (в него попадает экз класса httpRequest, который содержит в себе все данные о запросе: какой пользователь - 
  # аноним/зарегистрированный, файлы куки, метод запроса (get/post))
  # return HttpResponse('Home page') будет просто страница с указанным в аргументе текстом
  context = {
		'title': 'Home - Главная',
		'content': 'Магазин мебели HOME'

	} # имитация подгрузки контента вместо бд
  return render(request, 'main/index.html', context)  # request- для информации, адрес шаблона страницы, context - наш словарь



def about(request):
		context = {
			'title': 'Home - О нас',
			'content': 'О нас',
			'text_on_page': 'Пространный текст о том, почему этот магазин такой классный и о том какой хороший товар'
		}
		return render(request, 'main/about.html', context)