from django.core.management.base import BaseCommand
from home.models import Product, Category

class Command(BaseCommand):
    help = "Popula o banco de dados com 30 produtos de exemplo"

    def handle(self, *args, **kwargs):
        products = [
            # --- Eletrônicos ---
            {"name": "Notebook Dell Inspiron 15", "description": "Notebook com processador Intel i5, 8GB de RAM e SSD de 256GB.", "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8", "category": "Eletrônicos", "price": 3500.00, "stock": 12},
            {"name": "Smartphone Samsung Galaxy S22", "description": "Smartphone Android com câmera tripla e tela AMOLED de 6.1 polegadas.", "image_url": "https://images.unsplash.com/photo-1606813902910-3be86f786b8f", "category": "Eletrônicos", "price": 4200.00, "stock": 8},
            {"name": "Fone de Ouvido Bluetooth JBL", "description": "Fone de ouvido sem fio, bateria de longa duração e graves potentes.", "image_url": "https://images.unsplash.com/photo-1518444026580-48c1e9d8a6f4", "category": "Eletrônicos", "price": 299.90, "stock": 50},
            {"name": "Câmera Fotográfica Canon EOS", "description": "Câmera DSLR com sensor de 24.1MP e gravação em Full HD.", "image_url": "https://images.unsplash.com/photo-1519183071298-a2962be90b8e", "category": "Eletrônicos", "price": 3200.00, "stock": 7},
            {"name": "Tablet iPad 9ª Geração", "description": "Tablet Apple com tela Retina de 10.2 polegadas e chip A13 Bionic.", "image_url": "https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd", "category": "Eletrônicos", "price": 2800.00, "stock": 15},
            {"name": "Smartwatch Apple Watch SE", "description": "Relógio inteligente com GPS, monitor de batimentos e resistência à água.", "image_url": "https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b", "category": "Eletrônicos", "price": 1700.00, "stock": 20},

            # --- Moda ---
            {"name": "Camiseta Básica Branca", "description": "Camiseta 100% algodão, confortável e leve para o dia a dia.", "image_url": "https://images.unsplash.com/photo-1523381210434-271e8be1f52b", "category": "Moda", "price": 49.90, "stock": 100},
            {"name": "Relógio Analógico Casio", "description": "Relógio de pulso clássico, resistente à água e com pulseira de aço.", "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30", "category": "Moda", "price": 199.90, "stock": 25},
            {"name": "Tênis Nike Air Max", "description": "Tênis esportivo com amortecimento a ar e design moderno.", "image_url": "https://images.unsplash.com/photo-1600185365926-3a2ce0a1b9f5", "category": "Moda", "price": 399.90, "stock": 60},
            {"name": "Jaqueta Jeans", "description": "Jaqueta jeans unissex, resistente e estilosa.", "image_url": "https://images.unsplash.com/photo-1521335629791-ce4aec67dd47", "category": "Moda", "price": 249.90, "stock": 40},
            {"name": "Bolsa de Couro Feminina", "description": "Bolsa de ombro em couro legítimo, cor marrom, com compartimentos internos.", "image_url": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246", "category": "Moda", "price": 499.90, "stock": 30},

            # --- Móveis ---
            {"name": "Sofá Retrátil 3 Lugares", "description": "Sofá retrátil e reclinável, tecido suede cinza, super confortável.", "image_url": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7", "category": "Móveis", "price": 1899.90, "stock": 5},
            {"name": "Cadeira Gamer Vermelha", "description": "Cadeira ergonômica reclinável, com apoio lombar e design gamer.", "image_url": "https://images.unsplash.com/photo-1624705002806-88d798e6fbd2", "category": "Móveis", "price": 999.90, "stock": 10},
            {"name": "Mesa de Jantar 6 Lugares", "description": "Mesa retangular em madeira maciça com espaço para 6 pessoas.", "image_url": "https://images.unsplash.com/photo-1505691723518-36a5ac3be353", "category": "Móveis", "price": 1499.90, "stock": 6},
            {"name": "Cama Box Casal", "description": "Cama box casal com colchão de molas ensacadas e pillow top.", "image_url": "https://images.unsplash.com/photo-1616627783479-95a90d34aaad", "category": "Móveis", "price": 2399.90, "stock": 4},
            {"name": "Estante de Livros Moderna", "description": "Estante com design minimalista, acabamento branco fosco.", "image_url": "https://images.unsplash.com/photo-1586105251261-72a756497a12", "category": "Móveis", "price": 699.90, "stock": 15},

            # --- Acessórios ---
            {"name": "Mochila Escolar", "description": "Mochila resistente com divisórias internas e compartimento para notebook.", "image_url": "https://images.unsplash.com/photo-1598032895398-58f38b30f7a9", "category": "Acessórios", "price": 149.90, "stock": 50},
            {"name": "Óculos de Sol Ray-Ban", "description": "Óculos de sol modelo aviador, lentes polarizadas.", "image_url": "https://images.unsplash.com/photo-1503341455253-b2e723bb3dbb", "category": "Acessórios", "price": 399.90, "stock": 25},
            {"name": "Carteira Masculina Couro", "description": "Carteira compacta em couro legítimo, com porta-cartões.", "image_url": "https://images.unsplash.com/photo-1600172454219-1a49e39e3d9c", "category": "Acessórios", "price": 129.90, "stock": 40},
            {"name": "Chapéu Fedora", "description": "Chapéu elegante em feltro, ideal para ocasiões formais.", "image_url": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab", "category": "Acessórios", "price": 199.90, "stock": 30},
            {"name": "Pulseira Masculina Couro", "description": "Pulseira casual em couro trançado com fecho magnético.", "image_url": "https://images.unsplash.com/photo-1607462109229-8c26f8f1cc02", "category": "Acessórios", "price": 89.90, "stock": 60},

            # --- Livros ---
            {"name": "Livro: Clean Code", "description": "Guia prático para escrever código limpo e sustentável.", "image_url": "https://images.unsplash.com/photo-1512820790803-83ca734da794", "category": "Livros", "price": 129.90, "stock": 100},
            {"name": "Livro: Django for APIs", "description": "Aprenda a construir APIs RESTful usando Django e Django REST Framework.", "image_url": "https://images.unsplash.com/photo-1516979187457-637abb4f9353", "category": "Livros", "price": 149.90, "stock": 80},
            {"name": "Livro: Python Crash Course", "description": "Introdução prática à programação com Python.", "image_url": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f", "category": "Livros", "price": 139.90, "stock": 90},
            {"name": "Livro: The Pragmatic Programmer", "description": "Clássico da engenharia de software, cheio de boas práticas.", "image_url": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e", "category": "Livros", "price": 159.90, "stock": 70},
            {"name": "Livro: Artificial Intelligence Basics", "description": "Uma introdução simples e prática à inteligência artificial.", "image_url": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f", "category": "Livros", "price": 179.90, "stock": 60},

            # --- Esportes ---
            {"name": "Bola de Futebol Adidas", "description": "Bola oficial de futebol com revestimento em poliuretano.", "image_url": "https://images.unsplash.com/photo-1521412644187-c49fa049e84d", "category": "Esportes", "price": 249.90, "stock": 50},
            {"name": "Bicicleta Mountain Bike", "description": "Bicicleta aro 29, 21 marchas, ideal para trilhas.", "image_url": "https://images.unsplash.com/photo-1605719125063-07c0fb0a68fd", "category": "Esportes", "price": 2899.90, "stock": 12},
            {"name": "Tênis de Corrida Asics", "description": "Tênis leve e confortável, ideal para corridas longas.", "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff", "category": "Esportes", "price": 349.90, "stock": 40},
        ]

        for item in products:
            category, _ = Category.objects.get_or_create(name=item["category"])

            if not Product.objects.filter(name=item["name"]).exists():
                product = Product(
                    name=item["name"],
                    description=item["description"],
                    category=category,
                    price=item["price"],
                    stock=item["stock"],
                )
                product.set_image_from_url(item["image_url"])
                product.save()
                self.stdout.write(self.style.SUCCESS(f"✅ Produto criado: {product.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠️ Produto já existe: {item['name']}"))
