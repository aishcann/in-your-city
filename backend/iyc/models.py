from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    time = models.TimeField(
        auto_now=False, auto_now_add=False, blank=True)
    location = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
