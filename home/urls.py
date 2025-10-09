from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    
    path('location/', views.location, name='location'),
    path('cheap_product/', views.cheap_product, name='cheap_product'),
    path('payment/', views.payment, name='payment'),
    
    path('products/', views.products, name='products'),
    path('products/<int:product_id>/', views.product_id, name='product_id'),
    
    path('favorite/', views.favorites, name='favorite'),
    path('favorite/<int:product_id>/', views.toggle_favorite, name='toggle_favorite'),
    
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path("cart/remove/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),
    
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    
]
