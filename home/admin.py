from django.contrib import admin
from home import models
from .models import Product

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
   pass

