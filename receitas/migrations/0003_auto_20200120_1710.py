# Generated by Django 3.0.2 on 2020-01-20 21:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_auto_20200120_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 1, 20, 17, 10, 49, 221739)),
        ),
    ]