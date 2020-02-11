from django.db import models
from core.models import Core
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Product(Core):
    """
    Класс для хранения информации о продукте, производителе продукта , категории товара
    """
    class Meta:
        ordering = ('sort', 'title')
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')

    maker = models.ForeignKey(
        'Producer', verbose_name=_('products'), null=False, blank=False,
                                    related_name='products', on_delete=models.CASCADE)

    categories = models.ManyToManyField(
        'Category', verbose_name=_('products'), blank=True,
                                     related_name='products')

class Category(Core):
    """
    Собственно категория товара
    """
    class Meta:
        ordering = ('sort', 'title')
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
    pass

class Producer(Core):
    """
    информаци о производителе
    """
    class Meta:
        ordering = ('sort', 'title')
        verbose_name = _('Производитель')
        verbose_name_plural = _('Производители')
    pass

