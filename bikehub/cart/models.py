from django.db import models

# Create your models here.


class Cart(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='cart/',
                              default='', blank=True, null=True)
    date = models.DateTimeField()
    content = models.TextField()
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.name
