from django.db import models
from core.models import Core
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Product(Core):
    class Meta:
        sorting = ('sort', 'title')
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')

    producer = models.ForeignKey('Producer', verbose_name=_('products'), null=False, blank=False,
                                    related_name='products', on_delete=models.CASCADE)

    category = models.ManyToManyField('Category', verbose_name=_('products'), null=True, blank=True,
                                     related_name='products', on_delete=models.CASCADE)

class Category(Core):
    class Meta:
        sorting = ('sort', 'title')
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
    pass

class Producer(Core):
    class Meta:
        sorting = ('sort', 'title')
        verbose_name = _('Производитель')
        verbose_name_plural = _('Производители')
    pass

# изучить документацию