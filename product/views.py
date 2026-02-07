from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from product.forms import CreateProductForm
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
@login_required(login_url="/login/")
def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        category_id = request.GET.get("category_id")
        if category_id:
            products = Product.objects.filter(category_id=category_id)
        return render(
            request, "products/product_list.html", context={"products": products}
        )


@login_required(login_url="/login/")
def product_detail(request, product_id):
    if request.method == "GET":
        product = Product.objects.get(id=product_id)
        return render(
            request, "products/product_detail.html", context={"product": product}
        )


@login_required(login_url="/login/")
def product_create(request):
    if request.method == "GET":
        forms = CreateProductForm()
        return render(request, "products/product_create.html", context={"forms": forms})
    elif request.method == "POST":
        forms = CreateProductForm(request.POST, request.FILES)
        if forms.is_valid():
            Product.objects.create(
                name=forms.cleaned_data.get("name"),
                description=forms.cleaned_data.get("description"),
                image=forms.cleaned_data.get("image"),
                price=forms.cleaned_data.get("price"),
            )
            return redirect("/products/")
        return HttpResponse("Error")


def base(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "base.html", context={"categories": categories})
