import math

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView

from product.forms import CreateProductForm, SearchForm
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


# Product.objects.all() -> products = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10]
# limit = 3
# page = 1
# product = products[(page-1)*limit:page*limit]
# max_page = int(len(products)/limit)
# срезы = [start:stop]
#
# FBV -> Function Based View
# CBV -> Class Based View


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["forms"] = SearchForm()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )
        category_id = self.request.GET.get("category_id")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        price_choice = self.request.GET.get("price_choice")
        if price_choice:
            if price_choice == "1":
                queryset = queryset.filter(price__gt=100)
            elif price_choice == "2":
                queryset = queryset.filter(price__lt=100)
        tags = self.request.GET.getlist("tags")
        if tags:
            queryset = queryset.filter(tags__in=tags)
        return queryset
    

class ProductCreateView(CreateView):
    model = Product
    template_name = "products/product_create.html"
    form_class = CreateProductForm
    success_url = "/class/products/"
    



@login_required(login_url="/login/")
def product_list(request):
    limit = 3
    if request.method == "GET":
        products = Product.objects.all()
        forms = SearchForm()
        if request.GET.get("search"):
            search = request.GET.get("search")

            products = Product.objects.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )
        category_id = request.GET.get("category_id")
        if category_id:
            products = Product.objects.filter(category_id=category_id)
        price_choice = request.GET.get("price_choice")
        if price_choice:
            if price_choice == "1":
                products = Product.objects.filter(price__gt=100)
            elif price_choice == "2":
                products = Product.objects.filter(price__lt=100)
        tags = request.GET.getlist("tags")
        if tags:
            products = Product.objects.filter(tags__in=tags)

        page = int(request.GET.get("page")) if request.GET.get("page") else 1
        max_page = math.ceil(len(products) / limit)
        start = (page - 1) * limit
        stop = page * limit
        list_pages = range(1, max_page + 1)
        products = products[start:stop]
        return render(
            request,
            "products/product_list.html",
            context={"products": products, "forms": forms, "list_pages": list_pages},
        )


@login_required(login_url="/login/")
def product_detail(request, product_id):
    if request.method == "GET":
        product = Product.objects.get(id=product_id)
        return render(
            request, "products/product_detail.html", context={"product": product}
        )


# @login_required(login_url="/login/")
# def product_create(request):
#     user = request.user
#     if user.is_staff: # permission for admin
#         if request.method == "GET":
#             forms = CreateProductForm()
#             return render(
#                 request, "products/product_create.html", context={"forms": forms}
#             )
#         elif request.method == "POST":
#             forms = CreateProductForm(request.POST, request.FILES)
#             if forms.is_valid():
#                 Product.objects.create(
#                     name=forms.cleaned_data.get("name"),
#                     description=forms.cleaned_data.get("description"),
#                     image=forms.cleaned_data.get("image"),
#                     price=forms.cleaned_data.get("price"),
#                 )
#                 return redirect("/products/")
#             return HttpResponse("Error")
#     return HttpResponse("Permission denied")


@login_required(login_url="/login/")
def product_create(request):

    if request.method == "GET":
        forms = CreateProductForm()
        return render(request, "products/product_create.html", context={"forms": forms})
    elif request.method == "POST":
        forms = CreateProductForm(request.POST, request.FILES)
        if forms.is_valid():
            Product.objects.create(
                profile=request.user.profile,
                name=forms.cleaned_data.get("name"),
                description=forms.cleaned_data.get("description"),
                image=forms.cleaned_data.get("image"),
                price=forms.cleaned_data.get("price"),
            )
            return redirect("/products/")
        return HttpResponse("Error")


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.user.profile != product.profile:
        return HttpResponse("Permission denied")
    product.delete()
    return redirect("/products/")


def base(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "base.html", context={"categories": categories})
