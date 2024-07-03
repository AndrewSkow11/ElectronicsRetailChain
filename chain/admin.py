from django.contrib import admin
from .models import LinkOfChain, Contact, Product


def clear_debt(modeladmin, request, queryset):
    """Функция для очистки задолженности """
    queryset.update(debt=0)


clear_debt.short_description = ("Очистить задолженность перед поставщиком"
                                " у выбранных объектов")


class AdminLinkOfChain(admin.ModelAdmin):
    list_display = ('name', 'get_supplier', 'debt')
    list_filter = ('contact__city',)
    search_fields = ('name', 'contact__city')

    actions = [clear_debt]

    def get_supplier(self, obj):
        return obj.supplier.name if obj.supplier else ('Нет поставщика '
                                                       'более низкой иерархии')

    get_supplier.short_description = 'Поставщик'
    get_supplier.admin_order_field = 'supplier__name'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model',)
    search_fields = ('name', 'model',)


admin.site.register(LinkOfChain, AdminLinkOfChain)
admin.site.register(Contact)
admin.site.register(Product, ProductAdmin)
