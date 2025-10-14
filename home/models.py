from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import MediaCloudinaryStorage #type:ignore


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    image = models.ImageField(upload_to='products/', storage=MediaCloudinaryStorage())
   
    def __str__(self):
        return self.name
    
    
class Favorite(models.Model):
    session_key  = models.CharField( max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('session_key', 'product')
        
    def __str__(self):
        return f'{self.session_key } -> {self.product.name}'

   
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'product')
        
    def __str__(self):
        return f'{self.user.username} -> {self.product.name}'


