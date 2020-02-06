from django.db import models
from django.utils.translation import gettext_lazy as _

class Core(models.Model):
    class Meta:
        sorting = ('sort', 'title')
        verbose_name = _('Ядро')
        verbose_name_plural = _('Ядра')

    title = models.CharField(_('Заголовок объекта'), max_length=250, blank=True, null=True)
    description = models.TextField(_('описание объекта'), blank=True, null=True)
    sort = models.IntegerField(_('номер объекта для сортировки'), default=0, blank=True, null=False)
    is_active = models.BooleanField(_('Активен ли объект'), default=True, db_index=True)
    # делаем так чтобы при вызове пустого title отображалось пустая строка
    def __str__(self):
        return f'{self.title}' if self.title else ' '
    # при функции удаления объект становиться неактивным, но не удаляем
    def delete(self):
        self.is_active = False
        self.save()

class Picture(Core):
    class Meta:
        sorting = ('sort', 'title')
        verbose_name = _('Картинка')
        verbose_name_plural = _('Картинки')

    image = models.ImageField(upload_to='pictures')
    related_obj = models.ForeignKey(Core, verbose_name =_('pictures'), null=True, blank=True,
                                    related_name='pictures', on_delete=models.CASCADE )