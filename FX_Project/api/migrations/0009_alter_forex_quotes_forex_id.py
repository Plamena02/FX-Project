# Generated by Django 3.2.5 on 2021-08-14 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210814_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forex_quotes',
            name='forex_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.forex'),
        ),
    ]