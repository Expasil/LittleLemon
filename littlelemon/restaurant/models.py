from django.db import models

# Create your models here.

class booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(max_length=6)
    BookingDate = models.DateTimeField()


class menu(models.Model):
    Title = models.CharField( max_length=255 )
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    Inventory = models.IntegerField(max_length=5)

    