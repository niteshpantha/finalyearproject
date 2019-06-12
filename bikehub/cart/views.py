from django.shortcuts import render
from django.http import HttpResponse

from .models import Cart
# Create your views here.


def index(request):
    cart_list = Cart.objects.all()

    context = {
        "cart_list": cart_list,

    }
    return render(request, 'cart/cart.html', context)


def checkout(request):

    return render(request, 'cart/checkout.html')


def account(request):
    return render(request, 'cart/account.html')


def register(request):
    return render(request, 'cart/register.html')


def search(request):
    return render(request, '../search.html')
