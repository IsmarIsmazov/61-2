from django.shortcuts import redirect, render

from product.models import Category, Product

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
    if request.method == "GET":
        products = Product.objects.all()
        category_id = request.GET.get("category_id")
        if category_id:
            products = Product.objects.filter(category_id=category_id)
        return render(
            request, "products/product_list.html", context={"products": products}
        )


def product_detail(request, product_id):
    if request.method == "GET":
        product = Product.objects.get(id=product_id)
        return render(
            request, "products/product_detail.html", context={"product": product}
        )


def product_create(request):
    if request.method == "GET":
        return render(request, "products/product_create.html")
    elif request.method == "POST":
        print(request.POST)
        Product.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description"),
        )
        return redirect("/products/")


def base(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "base.html", context={"categories": categories})
