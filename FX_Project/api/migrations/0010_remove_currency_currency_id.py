# Generated by Django 3.2.5 on 2021-08-11 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_currency_cr_short_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='currency_id',
        ),
    ]
