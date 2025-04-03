from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
#     path('products/', views.products, name='products'),
#     path('cart/', views.cart, name='cart'),
#     path('checkout/', views.checkout, name='checkout'),
#     path('search/', views.search, name='search'),
]