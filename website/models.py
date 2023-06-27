from django.db import models


# Create your models here.

class Menuitem(models.Model):
    name = models.CharField(max_length=49)
    is_active = models.BooleanField(default=True)
    is_menu = models.BooleanField(default=True)
    html_file = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sport(models.Model):
    company = models.CharField(max_length=59)
    contact = models.IntegerField()
    country = models.CharField(max_length=59)

    def __str__(self):
        return self.company
