from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "email", "address", "message", "timestamp"]
    list_display_links = ["__str__"]
    list_filter = ["timestamp"]

    class Meta:
        model = Contact


admin.site.register(Contact, ContactModelAdmin)
