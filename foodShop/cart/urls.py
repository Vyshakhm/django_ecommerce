from django.urls import path
from . import views

urlpatterns = [

    path('add/<int:product_id>/',views.add_cart,name='add'),
    path('min/<int:product_id>/',views.min_cart,name='min'),
    path('delete/<int:product_id>/',views.cart_delete,name='delete'),
    path('checkout/',views.checkout,name='checkout'),
    path('cartdetails/',views.cart_details,name='cartdetails'),
]