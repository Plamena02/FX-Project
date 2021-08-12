# Generated by Django 3.2.5 on 2021-08-11 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210811_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_id', models.IntegerField(default='', primary_key='')),
                ('cr_name', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='forex',
            fields=[
                ('forex_id', models.IntegerField(default='', primary_key='True', serialize=False)),
                ('from_currency_id', models.IntegerField(default='')),
                ('to_currency_id', models.IntegerField(default='')),
            ],
        ),
        migrations.AlterField(
            model_name='forex_quotes',
            name='date',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='forex_quotes',
            name='rate',
            field=models.FloatField(default=''),
        ),
    ]
