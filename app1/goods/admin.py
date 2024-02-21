from django.contrib import admin

# здесь регистрируем наши модели - таблицы из models.py
from goods.models import Categories, Products  # импорт моделей

# admin.site.register(Categories) # регистрация модели категорий. Такой метод не позволяет вносить изменения
# admin.site.register(Products) # регистрация модели products. Такой метод не позволяет вносить изменения


# правильная регистрация моделей для большей гибкости
@admin.register(Categories)
class CategoriesAdmin(
    admin.ModelAdmin
):  # позволяет тонко настраивать отображение в админке
    prepopulated_fields = {  # передаём поля, которые будут заполняться автоматом
        "slug": ("name",)  # автоматически будет прописывать поле URL (slug) при заполнении названия
    }


# правильная регистрация моделей для большей гибкости
@admin.register(Products)
class ProductsAdmin(
    admin.ModelAdmin
):  # позволяет тонко настраивать отображение в админке
    prepopulated_fields = {  # передаём поля, которые будут заполняться автоматом
        "slug": ("name",)  # автоматически будет прописывать поле URL (slug) при заполнении названия
    }
