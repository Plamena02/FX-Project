# Generated by Django 3.2.5 on 2021-08-14 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_currency_cr_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='cr_short_name',
            field=models.TextField(default=''),
        ),
    ]
