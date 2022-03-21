import code
from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    
    def __str__ (self):
        return f"{self.id} code: {self.code} city: {self.city}"

class Flight(models.Model):
    #origin = models.CharField(max_length=64)
    origin = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrivals")
    duration = models.IntegerField()

    def __str__ (self):
        return f"id:{self.id} Miainga {self.origin.city} mankany {self.destination.city}"
        



