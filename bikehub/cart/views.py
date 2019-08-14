from django.shortcuts import render, get_object_or_404
import time
# from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User, auth

from django.urls import reverse
from django.http import HttpResponse
from .forms import CartItemForm, OrderItemForm
from django.contrib import messages
from cart.models import Bike, Cart, Order, CartItem
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
from django.db.models import FloatField
from django.db.models import Count
from django.shortcuts import redirect
from django.db.models import Q

# Create your views here.


def bike_view(request, id=None):
    bike = Bike.objects.get(id=id)
    context = {
        'bike': bike
    }
    return render(request, 'cart/bike.html', context)


@login_required(login_url='/admin/login/')
def add_to_cart(request):
    carts = CartItem.objects.all()
    total = 0
    bike_ids = []
    bike_id = None
    user = request.user
    cart = Cart.objects.get(user_id=user.id)
    for each in carts:
        bike_ids.append(each.bike_id.id)
        indvidual_price = each.bike_id.price * each.quantity
        total += indvidual_price
        print(bike_ids)
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        # form.data['cart_id'] = cart.id
        print(form.data)
        if form.is_valid():
            print("form valid")
            # print(form.data)
            form.save(commit=False)
            form.user = request.user
            form.date = timezone.now()
            form.cart_id = cart.id
            bike_id = form.data['bike_id']
            bike = Bike.objects.get(id=bike_id)
            bike_id = int(bike_id)

            if bike_id in bike_ids:
                # bike_id = request.POST.get('bike_id')
                c1 = CartItem.objects.get(bike_id=bike_id)
                c1.quantity += 1
                c1.save()
                messages.success(
                    request, 'You have successfully added your items in cartbox')
            else:
                c1 = CartItem.objects.create(
                    bike_id=bike,
                    quantity=1,
                    cart_id=cart,
                    price=bike.price
                )
        else:
            messages.error(
                request, 'Error adding items in cartbox')

    context = {
        "carts": carts,
        "total": total,
        "bike_id": bike_id,

    }
    return render(request, 'cart/add_to_cart.html', context)


def bike_delete(request, id=None):
    obj = get_object_or_404(CartItem, id=id)
    print(obj.id)
    obj.delete()

    return redirect('/cart/add_to_cart/')


def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Bike.objects.filter(Q(name__icontains=srch) |
                                        (Q(price__icontains=srch))
                                        )
            if match:
                return render(request, 'cart/search.html', {'sr': match})
            else:
                messages.error(request, 'no result found')
        else:
            return redirect('cart/search/')
    return render(request, 'cart/search.html')


def checkout(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        user = auth.authenticate(first_name=first_name,
                                 last_name=last_name, email=email)
        if user.is_authenticated:
            if user.is_active:
                return redirect('/ratings/')
            else:
                return HttpResponse('You dont have an account with us')

        form = CartItemForm(request.POST)
        forms = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
            forms.save()
            print(form.data)
            print(forms.data)
            user = request.user
            cart = Cart.objects.get(user_id=user.id)
            if user_id in user_id:
                carts = CartItem.objects.all()
                order = OrderItem.objects.all()
                if order in order:
                    c1 = carts.copy()
                    c2 = c1.save()

                    new_order, created = order.objects.get_or_create(
                        order=order)
                    if created:
                        new_order.order_id = str(time.time())
                        new_order.save()
                    if new_order.status == "Finished":
                        cart.delete()
    context = {
        # "form": form,
        # "forms": forms
    }
    return render(request, 'cart/checkout.html', context)


def ratings(request):
    return render(request, 'cart/ratings.html')
