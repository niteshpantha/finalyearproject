from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


# Create your models here.


class Bike(models.Model):
    name = models.CharField(default="new bike", max_length=150)
    image = models.ImageField(upload_to='cart/',
                              default='', blank=True, null=True)
    price = models.FloatField(default=0.0)
    date = models.DateTimeField(blank=True, null=True)
    # content = models.TextField(max_length=250)
    content = RichTextUploadingField(default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cart:bike_view", kwargs={"id": self.id})


class Cart(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )

    def ___str__(self):
        return self.user_id


class CartItem(models.Model):
    bike_id = models.ForeignKey(Bike, on_delete=models.CASCADE, default=None)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, default=None)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.cart_id


STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished")
)


class Order(models.Model):

    bike_id = models.ForeignKey(
        Bike, on_delete=models.CASCADE, default=None)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    # date = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.TextField(
        max_length=120, choices=STATUS_CHOICES, null=True)
    first_name = models.CharField(max_length=120, default="nitesh")
    last_name = models.CharField(max_length=120, default="pantha")
    email = models.EmailField("email", max_length=250,
                              default="niteshraz619@gmail.com")
    address = models.CharField(
        max_length=250, default="Bhaktapur-5 , Ghattaghar")
    city = models.CharField(max_length=120, default="Bhaktapur")
    payment_method = models.CharField(
        max_length=250, default="Cash On Delivery")

    def __str__(self):
        return self.bike_id


class OrderItem(models.Model):
    bike_id = models.ForeignKey(
        CartItem, on_delete=models.CASCADE, default=None)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.order_id
