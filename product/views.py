from django.shortcuts import render

from product.models import Product

# select * from product;
# Product.objects.all()


# select * from product where id= '2';
# Product.objects.get(id=2)  == возвращает 1 обьект

# select * from product where name = 'laptop';
# Product.objects.filter(name='laptop')

# select * from product $LIKE where name = 'laptop' and price = '1000';
# Product.objects.filter(name__icontains='laptop', price=1000)

# Product.objects.create(name='laptop', price=1000, description='laptop')

# Product.objects.update(price=1000) - изменение всех продуктов

# Product.objects.delete()


def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", context={"products": products})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "products/product_detail.html", context={"product": product})


def base(request):
    return render(request, "base.html")
