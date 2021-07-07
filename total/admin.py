from django.contrib import admin
from .models import product
from .models import customer
from .models import order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price',]


# Register your models here.
admin.site.register(product,AdminProduct)
admin.site.register(customer)
admin.site.register(order)
