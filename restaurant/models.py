from django.db import models

# Create your models here.

class Restaurant(models.Model):
    username = models.CharField(blank=False, null=False, max_length=50)
    contact_no = models.CharField(null=True, max_length=13)
    email = models.EmailField(null=False, blank=False)
    active = models.BooleanField(default=True, null=False)
    role = models.CharField(null=False, default='restaurant', max_length=20)

    def __str__(self):
        return f'{self.name}'



class MenuItem(models.Model):
    name = models.CharField(null=False, blank=False, max_length=40)
    price = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=10)
    speciality = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

