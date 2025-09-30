from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):  # Pode ser renomeado para Product
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Corrigido

    def __str__(self):
        return self.name


# Carrinho de Compras
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrinho de {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Contact, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"


# Favoritos
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    product = models.ForeignKey(Contact, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "product")  # Não deixar duplicado

    def __str__(self):
        return f"{self.user.username} favoritou {self.product.name}"


📌 views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Contact, Cart, CartItem, Favorite


# Lista de produtos
def product_list(request):
    products = Contact.objects.all()
    return render(request, "shop/product_list.html", {"products": products})


# ----------------- CARRINHO -----------------

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, "shop/cart_detail.html", {"cart": cart})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Contact, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("cart_detail")


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect("cart_detail")


# ----------------- FAVORITOS -----------------

@login_required
def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, "shop/favorites_list.html", {"favorites": favorites})


@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Contact, id=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)
    return redirect("favorites_list")


@login_required
def remove_from_favorites(request, product_id):
    favorite = get_object_or_404(Favorite, user=request.user, product_id=product_id)
    favorite.delete()
    return redirect("favorites_list")


📌 urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),

    # Carrinho
    path("cart/", views.cart_detail, name="cart_detail"),
    path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),

    # Favoritos
    path("favorites/", views.favorites_list, name="favorites_list"),
    path("favorites/add/<int:product_id>/", views.add_to_favorites, name="add_to_favorites"),
    path("favorites/remove/<int:product_id>/", views.remove_from_favorites, name="remove_from_favorites"),
]

templates
<h1>Produtos</h1>
<ul>
    {% for product in products %}
        <li>
            {{ product.name }} - R$ {{ product.price }}
            <a href="{% url 'add_to_cart' product.id %}">Adicionar ao carrinho</a> |
            <a href="{% url 'add_to_favorites' product.id %}">Favoritar</a>
        </li>
    {% endfor %}
</ul>

<a href="{% url 'cart_detail' %}">Ver Carrinho</a> |
<a href="{% url 'favorites_list' %}">Ver Favoritos</a>


cart_detail.html

<h1>Meu Carrinho</h1>

{% if cart.items.all %}
    <ul>
        {% for item in cart.items.all %}
            <li>
                {{ item.product.name }} - {{ item.quantity }}x = R$ {{ item.total_price }}
                <a href="{% url 'remove_from_cart' item.id %}">Remover</a>
            </li>
        {% endfor %}
    </ul>
{% else %}
    <p>Seu carrinho está vazio.</p>
{% endif %}

<a href="{% url 'product_list' %}">Voltar</a>

favorites_list.html
<h1>Meus Favoritos</h1>

{% if favorites %}
    <ul>
        {% for fav in favorites %}
            <li>
                {{ fav.product.name }} - R$ {{ fav.product.price }}
                <a href="{% url 'remove_from_favorites' fav.product.id %}">Remover</a>
            </li>
        {% endfor %}
    </ul>
{% else %}
    <p>Você ainda não tem favoritos.</p>
{% endif %}

<a href="{% url 'product_list' %}">Voltar</a>


