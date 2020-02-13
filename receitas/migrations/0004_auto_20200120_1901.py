# Generated by Django 3.0.2 on 2020-01-20 23:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('receitas', '0003_auto_20200120_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='pessoa',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pessoas.Pessoa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 1, 20, 19, 1, 29, 694696)),
        ),
    ]