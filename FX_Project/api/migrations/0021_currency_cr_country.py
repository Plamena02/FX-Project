# Generated by Django 3.2.5 on 2021-08-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_forex_quotes_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='cr_country',
            field=models.TextField(default=''),
        ),
    ]