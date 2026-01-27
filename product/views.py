from django.http import HttpResponse
from django.shortcuts import render

from product.models import Product

# select * from product;
# Product.objects.create()


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the product index.")


def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", context={"products": products})
