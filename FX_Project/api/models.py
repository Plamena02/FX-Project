from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Currency (models.Model): 
    forex_id = models.CharField(max_length=4, default="")
    symbol = models.CharField(max_length=6, default="")
    date = models.CharField(max_length=10, default="")
    rate = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.name

    def _get_(self, sym):
        self.symbol = sym
        return self.rate
        
