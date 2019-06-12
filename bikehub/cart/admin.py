from django.contrib import admin
from .models import Cart
# Register your models here.


class CartModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "name", "date", "image", "content"]
    list_display_links = ["__str__"]
    list_filter = ["date"]

    class Meta:
        model = Cart


admin.site.site_header = 'BikeHub Administration'
admin.site.register(Cart, CartModelAdmin)
