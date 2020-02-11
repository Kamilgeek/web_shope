from django.db import models
from django.utils.translation import gettext_lazy as _

class Core(models.Model):
    """
    Суперкласс который служит базой для остальных, от него наследуются практически все классы
    """
    class Meta:
        ordering = ('sort', 'title')
        verbose_name = _('Ядро')
        verbose_name_plural = _('Ядра')

    title = models.CharField(_('Заголовок объекта'), max_length=250, blank=True, null=True)
    description = models.TextField(_('описание объекта'), blank=True, null=True)
    sort = models.IntegerField(_('номер объекта для сортировки'), default=0, blank=True, null=False)
    active = models.BooleanField(_('Активен ли объект'), default=True, db_index=True)
    # делаем так чтобы при вызове пустого title отображалось пустая строка
    def __str__(self):
        return f'{self.title}' if self.title else ' '
    # при функции удаления объект становиться неактивным, но не удаляем
    def delete(self):
        self.active = False
        self.save()

class Picture(Core):
    """
    Класс для хранение фотографий
    """
    class Meta:
        ordering = ('sort', 'title')
        verbose_name = _('Картинка')
        verbose_name_plural = _('Картинки')

    image = models.ImageField(upload_to='pictures')
    related_obj = models.ForeignKey(Core, verbose_name =_('pictures'), null=True, blank=True,
                                    related_name='pictures', on_delete=models.CASCADE )

class Address(Core):
    class Meta:
        ordering = ('sort', 'title')
        verbose_name = _('Адрес')
        verbose_name_plural = _('Адреса')

    address1 = models.CharField(_('Адрес-street' ),max_length=250, blank=True, null=True)
    address2 = models.CharField(_('Адрес-number'), max_length=250, blank=True, null=True)
    zip_code = models.CharField(_('Адрес-zip'), max_length=20, blank=True, null=True)
    city = models.CharField(_('Адрес-city'), max_length=250, blank=True, null=True)
    region = models.CharField(_('Адрес-region'), max_length=250, blank=True, null=True)
    country = models.CharField(_('Адрес-country'), max_length=250, blank=True, null=True)
    phone = models.CharField(_('Адрес-city'), max_length=250, blank=True, null=True)
    contact_person = models.CharField(_('Адрес-person'), max_length=250, blank=True, null=True)

    related_obj = models.ForeignKey(Core, verbose_name=('Пользователь'), null=True, blank=True,
                                    related_name='addresses', on_delete=models.CASCADE)