from django.db import models

# Create your models here.
class Currency(models.Model): 
    full_name = models.CharField(max_length=50, default="", unique=True)
    short_name = models.CharField(max_length=3, default="", unique=True)

    def __init__(self, full_name, short_name):
        self.full_name = full_name
        self.short_name = short_name


