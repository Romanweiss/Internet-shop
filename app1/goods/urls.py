from django.urls import path

from goods import views

app_name = 'goods' # прописывается для того чтобы работало namespace


urlpatterns = [
    path('', views.catalog, name='index'),  # name - для обращения в html на языке шаблонов
    path('product/', views.product, name='product'),
]
