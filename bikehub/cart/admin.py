from django.contrib import admin
from .models import Bike, Cart, Order, CartItem, OrderItem
# Register your models here.


class BikeModelAdmin(admin.ModelAdmin):
    list_display = ["__str__",
                    "image", "date", "content"]
    list_display_links = ["__str__"]
    list_filter = ["date"]

    class Meta:
        model = Bike


class CartModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "user_id"]
    list_display_links = ["__str__"]

    class Meta:
        model = Cart


class CartItemModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "bike_id", "cart_id", "quantity", "price"]
    list_display_links = ["__str__"]
    # list_filter = ["cart_id"]

    class Meta:
        model = CartItem


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "bike_id", "user_id", "status"]
    list_display_links = ["__str__"]

    class Meta:
        model = Order


class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "order_id", "bike_id", "price", "quantity"]
    list_display_links = ["__str__"]

    class Meta:
        model = OrderItem


admin.site.site_header = 'BikeHub Administration'
admin.site.register(Bike, BikeModelAdmin)
admin.site.register(Cart, CartModelAdmin)
admin.site.register(Order, OrderModelAdmin)
admin.site.register(CartItem, CartItemModelAdmin)
admin.site.register(OrderItem, OrderItemModelAdmin)
