# Generated by Django 3.2.5 on 2021-08-04 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_simbol_currency_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='symbol',
            field=models.CharField(default='', max_length=6),
        ),
    ]
