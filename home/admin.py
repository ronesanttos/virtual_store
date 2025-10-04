from django.contrib import admin
from home import models
from .models import Product
from django import forms

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class ProductAdminForm(forms.ModelForm):
    image_url = forms.URLField(required=False, label="Imagem por URL")

    class Meta:
        model = Product
        fields = "__all__"
    
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    
    def save_model(self, request, obj, form, change):
        # Se o usuário digitou uma URL
        image_url = form.cleaned_data.get("image_url")
        if image_url:
            obj.set_image_from_url(image_url)
        super().save_model(request, obj, form, change)

admin.site.register(Product, ProductAdmin)
