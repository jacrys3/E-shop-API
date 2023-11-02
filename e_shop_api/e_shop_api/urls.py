from django.contrib import admin
from django.urls import path, include
from e_shop.routing import products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(products)),
]
