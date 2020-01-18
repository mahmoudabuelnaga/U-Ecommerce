from django.contrib import admin
from .models import Product,Color

# Register your models here.
admin.site.site_header=("Online Shop")

admin.site.register(Product)
admin.site.register(Color)