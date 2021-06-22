from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20, blank=True)
    age = models.CharField(max_length=4, blank=True)
    address = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=20, blank=True)
    ph = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=20, blank=True)
    cd = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

