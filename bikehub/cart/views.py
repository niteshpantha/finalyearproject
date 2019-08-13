from django.shortcuts import render, get_object_or_404
import time
# from django.shortcuts import HttpResponseRedirect
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


def checkout(request):

    if request.method == 'POST':
        form = CartItemForm(request.POST)
        user = request.user
        cart = Cart.objects.get(user_id=user.id)
        if user_id in user_id:
            carts = CartItem.objects.all()
            order = OrderItem.objects.get(id=order_id)
            new_order, created = Order.objects.get_or_create(order=order)
            if created:
                new_order.order_id = str(time.time())
                new_order.save()
            if new_order.status == "Finished":
                cart.delete()

            return render(request, 'cart/checkout.html')
            # c1 = carts.append(user_id.order_id)
            # c1.save()

    # if request.method == 'POST':
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     email = request.POST['email']
    #     address = request.POST['address']
    #     city = request.POST['city']
    #     return render(request, "home/index.html")
    #     if form.is_valid():
    #         form.save()

    #         print(fork)
    #         cart = CartItemForm.objects.get(id=user_id)
    #         order = OrderItemForm.objects.get(id=order_id)
    #         new_order, created = Order.objects.get_or_create(cart=cart)
    #         if created:
    #             new_order.order_id = str(time.time())
    #             new_order.save()
    #         if new_order.status == "Finished":
    #             cart.delete()
    #             return render(request, 'cart/checkout.html')
    # else:
    #     return redirect("/cart/add_to_cart/")

    # def checkout(request):
    #     pass
    # selected_cart =
    # if request.method == "POST":
    #     if form.is_valid():
    #         form = CartItemForm(request.POST)
    #         selected_cart = request.form['carts']
    #         cart_here = CartItem.objects.get['selected_cart']
    #         del request.form['selected_cart']

    #     else:
    #         selected_cart = None
    #         return redirect('cart/add_to_cart/')

    #         new_order, created = Order.objects.get_or_create(cart=cart)
    #         if created:
    #             new_order.save()
    #             cart_here.save()
    #         if new_order.status == "Finished":
    #             del request.form['carts']
    # return render(request, 'cart/checkout.html')

    # @login_required(login_url='/admin/login/')
    # def add_to_cart(request, id=None):
    #     carts = Cart.objects.all()
    #     if request.method == 'POST':
    #         form = CartForm(request.POST)
    #         if form.is_valid():
    #             print("form valid")
    #             form.save(commit=False)
    #             form.user = request.user
    #             form.date = timezone.now()
    #             form.save()
    #             messages.success(
    #                 request, 'You have successfully added your items in cartbox')
    #         else:
    #             messages.error(request, 'Error adding items in cartbox')

    #     instance = get_object_or_404(Cart, id=id)
    #     if request.method == 'GET':
    #         form = CartForm(request.GET or None,
    #                         request.FILES or None, instance=instance)
    #         if form.is_valid():
    #             instance.delete()
    #             messages.success(
    #                 request, 'You have successfully deleted the selected cart')
    #         else:
    #             messages.error(
    #                 request, 'You have failed deleting the previously selected cart')
    #     context = {
    #         "carts": carts,
    #         "instance": instance,
    #         "form": form
    #     }
    #     return render(request, 'cart/add_to_cart.html', context)

    # def search(request):
    #     return render(request, '../search.html')
