from app.settings import DEBUG
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),  # подключаем url адреса приложения в главный url файл с помощью функции include
    path('catalog/', include('goods.urls', namespace='catalog'))  # подключаем url адреса приложения в главный url файл с помощью функции include
    # namespace - для обозначения приложения к которому относятся данные url адреса, 
    # когда мы обращаемся к ним в шаблонах (создание пространства имен), нужно указать app_name в url файле приложения

]

if DEBUG:  # импорт выше, работать будет только в дебаг режиме
	urlpatterns += [
   path("__debug__/", include("debug_toolbar.urls")),
   ]  # добавляем пути приложения дебагер