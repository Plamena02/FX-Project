# Generated by Django 3.2.5 on 2021-08-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forex_quotes',
            name='rate',
            field=models.FloatField(default=''),
        ),
    ]
