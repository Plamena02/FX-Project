# Generated by Django 3.2.5 on 2021-09-01 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_alter_forex_quotes_forex_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forex_quotes',
            name='forex_id',
            field=models.IntegerField(default=''),
        ),
    ]