"""
URL configuration for onlinestore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import path

from product.views import (
    base,
    product_create,
    product_detail,
    product_list,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", base),
    path("products/", product_list),
    path("products/<int:product_id>/", product_detail),
    path("product_create/", product_create),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
