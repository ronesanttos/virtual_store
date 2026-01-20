# 🛒 Virtual Store

Aplicação web de **e-commerce** desenvolvida com **Django**, com foco em organização, usabilidade e boas práticas de desenvolvimento web.

O projeto simula uma loja virtual completa, servindo como base para estudos, portfólio ou expansão para um produto real.

---

## 🚀 Funcionalidades

- Página inicial com listagem de produtos
- Visualização de detalhes do produto
- Estrutura de carrinho de compras
- Organização de produtos por categorias
- Templates reutilizáveis com Django
- Painel administrativo do Django para gerenciamento
- Estrutura pronta para autenticação e pagamentos

---

## 🛠️ Tecnologias Utilizadas

### Back-end
- **Python**
- **Django**

### Front-end
- **HTML5**
- **CSS3**

### Banco de Dados
- **SQLite** (padrão do Django)

---

🌐 Deploy

O projeto possui arquivo render.yaml, permitindo deploy fácil no Render.

Basta conectar o repositório ao Render, configurar as variáveis de ambiente e iniciar o serviço.

---

## ⚙️ Como Rodar o Projeto Localmente
1. `git clone ...`
2. `cd virtual_store`
3. `python -m venv venv`
4. `pip install -r requirements.txt`
5. `python manage.py migrate`
6. `python manage.py runserver`
7. `Painel administrativo: http://127.0.0.1:8000/admin
` 

## 📂 Estrutura do Projeto

virtual_store/
│
├── manage.py
├── requirements.txt
├── project/
│ └── settings.py
├── home/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/
├── base_templates/
├── base_static/
│ ├── css/
│ └── images/
├── db.sqlite3
└── render.yaml
