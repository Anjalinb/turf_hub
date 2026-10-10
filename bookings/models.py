from django.db import models
from my_app.models import Turf

class Reservation(models.Model):
    team_name=models.CharField(max_length=200)
    contact_no=models.CharField(max_length=200)
    reservation_date=models.DateField()
    reservation_time=models.TimeField()
    turf=models.ForeignKey(Turf,on_delete=models.CASCADE,related_name="reservations")
    duration=models.DurationField()


def __str__(self):
    return self.team_name
