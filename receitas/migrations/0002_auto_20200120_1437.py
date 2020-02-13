# Generated by Django 3.0.2 on 2020-01-20 18:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 1, 20, 14, 37, 17, 3186)),
        ),
        migrations.AlterField(
            model_name='receita',
            name='ingredientes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='receita',
            name='modo_preparo',
            field=models.TextField(),
        ),
    ]
