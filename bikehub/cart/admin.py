from django.contrib import admin
from .models import Bike, Cart, Order
# Register your models here.


class BikeModelAdmin(admin.ModelAdmin):
    list_display = ["__str__",
                    "image", "date", "content"]
    list_display_links = ["__str__"]
    list_filter = ["date"]

    class Meta:
        model = Bike


class CartModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "bike_id", "user_id", "date", "quantity"]
    list_display_links = ["__str__", "bike_id"]
    list_filter = ["date"]

    class Meta:
        model = Cart


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "bike_id", "user_id", "date", "status"]
    list_display_links = ["__str__"]
    list_filter = ["date"]

    class Meta:
        model = Order


admin.site.site_header = 'BikeHub Administration'
admin.site.register(Bike, BikeModelAdmin)
admin.site.register(Cart, CartModelAdmin)
admin.site.register(Order, OrderModelAdmin)
