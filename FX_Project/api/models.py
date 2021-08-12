from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class forex_quotes (models.Model): 
    forex_id = models.IntegerField(default="")
    date = models.IntegerField(default="")
    rate = models.FloatField(default="")

    def __str__(self):
        return self.name

class forex (models.Model):
    forex_id = models.IntegerField(primary_key="True", default="")
    from_currency_id = models.IntegerField(default="")
    to_currency_id = models.IntegerField(default="")

    def __str__(self):
        return self.name

class currency (models.Model):
    cr_short_name = models.TextField(default="")
    cr_name = models.TextField(default="")