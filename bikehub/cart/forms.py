from django import forms

from .models import CartItem


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        # fields = ['bike_id', 'cart_id', 'quantity', 'price']
        fields = ['bike_id']


class OrderItemForm(forms.ModelForm):
    class Meta:
        fields = ['bike_id', 'order_id', 'quantity', 'price']
