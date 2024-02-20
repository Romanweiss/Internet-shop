from django.urls import path

from main import views

app_name = 'main'  # прописывается для того чтобы работало namespace

urlpatterns = [
    path('', views.index, name='index'),  # name - для обращения в html на языке шаблонов
    path('about/', views.about, name='about'),
]
