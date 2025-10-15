from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from home.models import Product, Category, Favorite
from .forms import EnderecoForm
from django.db.models import Q



def index(req):
    category_id = req.GET.get('category')
    products = Product.objects.order_by('-id')
    
    #entender este trecho
    user_favorites = set()
    if not req.session.session_key:
        req.session.save()
    
    session_key = req.session.session_key
    
    user_favorites = set(
        Favorite.objects.filter(session_key=session_key)
        .values_list('product_id', flat=True)
    )
    
    if category_id:
        products = products.filter(category_id=category_id)
        
    categories = Category.objects.all()
    
    paginator = Paginator(products, 4)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    endereco = req.session.get('endereco', {})
    
    context = {
        'page_obj':page_obj, 
        'site_title': 'Home',
        'selected_category': category_id,
        'categories': categories,
        'user_favorites': user_favorites,
        'endereco':endereco
        ,}
    
    return render( req ,
        'home/index.html',
        context,)
   
def search(req):
    search_value = req.GET.get('q','').strip()
    
    user_favorites = set()
    if not req.session.session_key:
        req.session.save()
    
    session_key = req.session.session_key
    
    user_favorites = set(
        Favorite.objects.filter(session_key=session_key)
        .values_list('product_id', flat=True)
    )
    
    if search_value == '':
        return redirect('home:index')
    
    products = Product.objects.filter(
        Q(name__icontains=search_value) |
        Q(description__icontains=search_value) |
        Q(price__icontains=search_value) |
        Q(category__name__icontains=search_value)
    ).order_by('-id')
    
    paginator = Paginator(products, 10)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_value': search_value,
        'user_favorites': user_favorites,
    }
    
    return render(
        req,
        'home/index.html',
        context,
        
    )

def cart(req):
    cart = req.session.get("cart", {})
    category_id = req.GET.get('category')   
    
    products = Product.objects.all()
     
    if category_id:
        products = products.filter(category_id=category_id)
        
    categories = Category.objects.all()
    total = sum(float(item["price"]) * int(item["quantity"]) for item in cart.values())
    
    context = {
        "cart": cart,
        "total": total,
        "site_title": "Carrinho",
        'selected_category': category_id,
        'categories': categories,
    }
    
    return render(req,"home/cart.html", context)

def clear_cart(req):
    if "cart" in req.session:
        del req.session["cart"]
        req.session.modified = True
    return redirect("home:cart")

def add_to_cart(req,product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = req.session.get("cart", {})
    
    if str(product_id) in cart:
        cart[str(product_id)]["quantity"] += 1
        
    else:
        cart[str(product_id)] = {
            "name": str(product.name),              # string simples
            "price": float(product.price),          # número simples
            "quantity": 1,                          # número simples
            "image": str(product.image.url) if product.image else "",  # string simples
        }
        
    req.session["cart"] = cart
    req.session.modified = True
    return redirect("home:cart")

def remove_from_cart(req,product_id):
    cart = req.session.get("cart", {})
    if str(product_id) in cart:
        cart[str(product_id)]["quantity"] -= 1
        req.session["cart"] = cart
        req.session.modified = True
        
    if  cart[str(product_id)]["quantity"] <= 0:
        del cart[str(product_id)]
        
    return redirect("home:cart")
    
def favorites(req):
    if not req.session.session_key:
        req.session.create()
        
    session_key = req.session.session_key
    
    favorites = Favorite.objects.filter(session_key=session_key).select_related("product")
    products = Product.objects.all()
    
    category_id = req.GET.get('category')    
    if category_id:
        products = products.filter(category_id=category_id)
        
    categories = Category.objects.all()
    
    context = {
        'selected_category': category_id,
        'categories': categories,
        'favorites': favorites,
    }
    return render(req, "home/favorites.html", context)

def toggle_favorite(req,product_id):
    if not req.session.session_key:
        req.session.create()
        
    session_key = req.session.session_key
    product = get_object_or_404(Product, id=product_id)
    
    favorite, created = Favorite.objects.get_or_create(session_key=session_key, product=product)

    if not created:
        # Já era favorito → remove
        favorite.delete()
        
    return redirect('home:products')

def products(req):
    category_id = req.GET.get('category')
    products = Product.objects.order_by('-id')
    
     #entender este trecho
    user_favorites = set()
    if not req.session.session_key:
        req.session.save()
    
    session_key = req.session.session_key
    
    user_favorites = set(
        Favorite.objects.filter(session_key=session_key)
        .values_list('product_id', flat=True)
    )
     
    if category_id:
        products = products.filter(category_id=category_id)
        
    categories = Category.objects.all()

    paginator = Paginator(products, 12)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj, 
        'selected_category': category_id,
        'categories': categories,
        'site_title': 'Produtos',
        'user_favorites': user_favorites
        ,}
    
    return render( req ,
        'home/products.html',
        context,) 
    
def product_id(req,product_id):
    try:
        single_product = Product.objects.get(pk=product_id)
        categories = Category.objects.all()
        
        if not req.session.session_key:
            req.session.save()
        
        session_key = req.session.session_key
        
        user_favorites = set(
            Favorite.objects.filter(session_key=session_key)
            .values_list('product_id', flat=True)
        )    
        
        context = {
            'categories': categories,
            'product': single_product,
            'site_title':f"{single_product.name} - Detalhes",
            'user_favorites':user_favorites,
        }
    
    except Product.DoesNotExist:
        return redirect('home:products')
    
    return render(
        req,
        'home/product_id.html',
        context,
    )
    
def sobre(req):
    products = Product.objects.all()
    
    category_id = req.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
        
    categories = Category.objects.all()
    return render( req ,
        'home/sobre.html',{'categories': categories,})

def contato(req):
    products = Product.objects.all()
    
    category_id = req.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
        
    categories = Category.objects.all()
    return render( req ,
        'home/contato.html',{'categories': categories,})
    
def location(req):
    endereco_session = req.session.get("endereco", {})
    form = EnderecoForm(req.POST or None)
    
    if form.is_valid():
        endereco = {
            'cep': form.cleaned_data['cep'],
            'logradouro': form.cleaned_data.get('logradouro'),
            'bairro': form.cleaned_data.get('bairro'),
            'cidade': form.cleaned_data.get('cidade'),
            'uf': form.cleaned_data.get('uf'),
        }
        
        # ✅ Salva o dicionário na sessão
        req.session['endereco'] = endereco
        req.session.modified = True
    
        endereco_session = endereco
    
    products = Product.objects.all()
    category_id = req.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
        
    categories = Category.objects.all()
    
    context = {
        'categories': categories,
        'form': form,
        'endereco': endereco_session,
    }
    return render( req ,
        'home/forms/location.html',context)
    
    
def payment(req):
    products = Product.objects.all()
    
    category_id = req.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
        
    categories = Category.objects.all()
    return render( req ,
        'home/forms/payment.html',{'categories': categories,})
    
def cheap_product(req):
    category_id = req.GET.get('category')
    products = Product.objects.filter(price__lte=100).order_by('-id')
    
     #entender este trecho
    user_favorites = set()
    if not req.session.session_key:
        req.session.save()
    
    session_key = req.session.session_key
    
    user_favorites = set(
        Favorite.objects.filter(session_key=session_key)
        .values_list('product_id', flat=True)
    )
    if category_id:
        products = products.filter(category_id=category_id)
        
    categories = Category.objects.all()

    paginator = Paginator(products, 10)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj, 
        'selected_category': category_id,
        'categories': categories,
        'user_favorites': user_favorites
        ,}
    return render( req ,
        'home/forms/cheap_product.html',context)