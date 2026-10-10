from django.db import models

class Turf(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    fee=models.IntegerField()
    phone_no=models.CharField(max_length=200)

    def __str__(self):
        return self.name
