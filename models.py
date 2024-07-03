from django.db import models

class Factory(models.Model):
    name = models.CharField(max_length=255, verbose_name='название завода')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "завод"
        verbose_name_plural = "заводы"


class RetailNetwork(models.Model):
    name = models.CharField(max_length=255, verbose_name='название розничной сети')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "розничная сеть"
        verbose_name_plural = "розничные сети"


class Entrepreneur(models.Model):
    name = models.CharField(max_length=255, verbose_name='имя предпринимателя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "предприниматель"
        verbose_name_plural = "предприниматели"


class LinkOfChain(models.Model):
    name = models.CharField(max_length=255, verbose_name='название звена цепочки')
    parent_link = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children', verbose_name='родительское звено')
    factory = models.OneToOneField(Factory, on_delete=models.CASCADE, null=True, blank=True, related_name='завод', verbose_name='завод')
    retail_network = models.OneToOneField(RetailNetwork, on_delete=models.CASCADE, null=True, blank=True, related_name='розничная_сеть', verbose_name='розничная сеть')
    entrepreneur = models.OneToOneField(Entrepreneur, on_delete=models.CASCADE, null=True, blank=True, related_name='предприниматель', verbose_name='предприниматель')

    def get_hierarchy_level(self):
        if self.factory:
            return 1
        elif self.retail_network:
            return 2
        elif self.entrepreneur:
            return 3
        else:
            return 0

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "звено цепочки"
        verbose_name_plural = "звенья цепочки"
