from ast import mod
from email.mime import image
from email.policy import default
from enum import unique
from pyexpat import model
from unicodedata import category
from django.db import models


# Создаём таблицы здесь!
# Таблица категорий товаров
# API для взаимодействия с таблицей Categories
class Categories(models.Model):  # наследование при создании таблиц от класса Model
    name = models.CharField(
        "Название категории",  # verbose_name для отображения поля при добавлении в админке
        max_length=150,  # Максимальная длина
        unique=True,  # уникальность поля
    )
    slug = models.SlugField(
        "URL",  # verbose_name для отображения поля при добавлении в админке
        max_length=200,
        unique=True,
        blank=True,  # поле может быть пустым
        null=True,
    )

    class Meta:  # для правильного именования
        db_table = "category"  # именование таблицы в бд (в единственном числе)
        verbose_name = (
            "Категорию"  # для отображения в админ панели при добавлении (род. падеж)
        )
        verbose_name_plural = "Категории"  # для отображения в админ панели

    def __str__(self):  # для правильного отображения имен в админке при входе (вместо object)
        return self.name


# API для взаимодействия с таблицей Products
class Products(models.Model):
    name = models.CharField(
        "Название",  # verbose_name для отображения поля при добавлении в админке
        max_length=150,  # Максимальная длина
        unique=True,  # уникальность поля
    )
    slug = models.SlugField(
        "URL",  # verbose_name для отображения поля при добавлении в админке
        max_length=200,
        unique=True,
        blank=True,  # поле может быть пустым
        null=True,
    )
    description = models.TextField("Описание", blank=True, null=True)
    image = models.ImageField(
        "Изображение",
        upload_to="goods_images",  # ссылка на изображение
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        "Цена",
        default=0.00,  # значение по умолчанию
        max_digits=4,  # количество знаков до запятой
        decimal_places=2,  # количество знаков после запятой
    )
    discount = models.DecimalField(
        "Скидка в %",
        default=0.00,  # значение по умолчанию
        max_digits=7,  # количество знаков до запятой
        decimal_places=2,  # количество знаков после запятой
    )
    quantity = models.PositiveBigIntegerField("Количество", default=0)
    category = models.ForeignKey(  # связка с таблицей
        to=Categories,  # с какой таблицей связываем
        on_delete=models.CASCADE,  # PROTECT - категория не будет удалена, если есть товары ссылающиеся на эту категорию,
        # CASCADE - при удалении категории будут удалены и все закреплённые за данной категорией товары (будет предупреждение)
        # SET_DEFAULT - при удалении категории все закреплённые за данной категорией товары будут принимать значение по умолчанию - default = ''
        verbose_name="Категория",
    )

    class Meta:  # для правильного именования
        db_table = "product"  # именование таблицы в бд (в единственном числе)
        verbose_name = (
            "Продукт"  # для отображения в админ панели при добавлении (род. падеж)
        )
        verbose_name_plural = "Продукты"  # для отображения в админ панели

    def __str__(self):  # для правильного отображения имен в админке при входе (вместо object)
        return f'{self.name} Количество - {self.quantity}'