from django.db import models


# Create your models here.
# 1. Необходимо реализовать модель сети по продаже электроники.
#
# Сеть должна представлять собой иерархическую структуру из трех уровней:
# - завод;
# - розничная сеть;
# - индивидуальный предприниматель.
#
# Каждое звено сети ссылается только на одного поставщика
# оборудования (не обязательно предыдущего по иерархии).
# Важно отметить, что уровень иерархии определяется
# не названием звена, а отношением к остальным элементам сети,
# т. е. завод всегда находится на уровне 0,
# а если розничная сеть относится напрямую к заводу,
# минуя остальные звенья, ее уровень — 1.
#
# 2. Каждое звено сети должно обладать следующими элементами:
# - Название.

# - Продукты:
#   - название,
#   - модель,
#   - дата выхода продукта на рынок.
# - Поставщик (предыдущий по иерархии объект сети).
# - Задолженность перед поставщиком в денежном выражении с точностью до копеек.
# - Время создания (заполняется автоматически при создании).

class Contact(models.Model):
    """Вспомогательный элемент модели звена сети"""
    #  - email,
    email = models.EmailField(
        verbose_name='email',
    )
    #   - страна,
    country = models.CharField(
        max_length=64,
        verbose_name='страна'
    )
    #   - город,
    city = models.CharField(
        max_length=64,
        verbose_name='город',
    )
    #   - улица,
    street = models.CharField(
        max_length=64,
        verbose_name='улица'
    )
    #   - номер дома.
    building_number = models.CharField(
        max_length=32,
        verbose_name='номер дома'
    )

    def __str__(self):
        return (f'{self.email} - {self.country} - {self.city} - {self.street}'
                f' - {self.building_number}')

    class Meta:
        verbose_name = "контакт"
        verbose_name_plural = "контакты"


class Link(models.Model):
    """Модель звена сети"""
    name = models.CharField(max_length=255, verbose_name='название звена')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "звено сети"
        verbose_name_plural = "звенья сети"
