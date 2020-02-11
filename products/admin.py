from django.contrib import admin

from .models import Producer, Product
admin.site.register(Product)
admin.site.register(Producer)


