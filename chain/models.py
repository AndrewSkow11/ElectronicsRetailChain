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


# иерархия завода - 0
# розничная сеть - 1 или 2
# ИП - 1 или 2


# - Продукты:
#   - название,
#   - модель,
#   - дата выхода продукта на рынок.


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


class LinkOfChain(models.Model):
    """Модель звена сети"""
    name = models.CharField(max_length=255, verbose_name='название звена')
    contact = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE,
        related_name='contact',
        verbose_name='контакты звена'
    )
    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='поставщик'
    )
    debt = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        verbose_name='задолженность'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания'
    )

    # - Поставщик (предыдущий по иерархии объект сети).
    def get_hierracly_level(self):
        """Метод определяет уровень иерархии текущего звена,
         рекурсивно поднимаясь по цепочке поставщиков"""

        def get_level(link, level=0):
            if link.supplier:
                return get_level(link.supplier, level + 1)
            return level

        return get_level(self)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "звено сети"
        verbose_name_plural = "звенья сети"

class Product(models.Model):
    # - Продукты:
    #   - название,
    #   - модель,
    #   - дата выхода продукта на рынок.


    name = models.CharField(
        max_length=256,
        verbose_name='название продукта'
    )
    model = models.CharField(
        max_length=256,
        verbose_name='модель продукта'
    )
    market_date = models.DateField(
        verbose_name='дата выхода на рынок'
    )
    link_of_chain = models.ForeignKey(
        LinkOfChain,
        on_delete=models.CASCADE,
        related_name='product',
        verbose_name='звено сети'
    )

    def __str__(self):
        return f'{self.name} - {self.model} - {self.market_date}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
