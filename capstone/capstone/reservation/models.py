from django.db import models

# Create your models here.
class Booking(models.Model):

    Name =models.CharField(max_length=255)
    No_of_guest =models.IntegerField()
    Date =models.DateField()


class menu(models.Model):
    Title =models.CharField(max_length=255)
    Price =models.DecimalField(max_digits = 10, decimal_places=2)
    Inventory =models.IntegerField()
    def __str__(self):
     return f'{self.title} : {str(self.price)}'