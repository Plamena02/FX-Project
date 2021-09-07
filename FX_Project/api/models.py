from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Currency (models.Model):
    id = models.AutoField(primary_key="True")
    cr_short_name = models.TextField(default="")
    cr_name = models.TextField(default="")
    cr_country = models.TextField(default="")

class Forex (models.Model):
    forex_id = models.IntegerField(primary_key="True")
    from_currency_id = models.ForeignKey(Currency, null=True, related_name='from_currency', on_delete=models.DO_NOTHING)
    to_currency_id = models.ForeignKey(Currency, null=True, related_name='to_currency', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Forex_quotes (models.Model): 
    id = models.AutoField(primary_key="True")
    forex_id = models.IntegerField(default="") 
    date = models.DateField(default="")
    rate = models.FloatField(default="", null=True)

