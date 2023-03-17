from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    # origin = models.CharField(max_length=64)
    # models.CASCADE does is that if the file/Airportcity is ever deleted from the Airport file then the file from the Flight table will be also deleted
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    # destination = models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    # Any model can implement the below function which return the string representation of that particular object
    def __str__(self):
        # This will be the string representation for the any flight
        return f"{self.id}: {self.origin} to {self.destination}"
    
#See `README.md` for the further instructions

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"