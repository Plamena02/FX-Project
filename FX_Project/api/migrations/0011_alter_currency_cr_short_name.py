# Generated by Django 3.2.5 on 2021-08-14 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210814_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='cr_short_name',
            field=models.IntegerField(default=''),
        ),
    ]