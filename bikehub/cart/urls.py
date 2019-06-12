from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.index, name='index'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('cart/account/', views.account, name='account'),
    path('cart/register/', views.register, name='register'),
    path('cart/search', views.search, name='search'),

]
