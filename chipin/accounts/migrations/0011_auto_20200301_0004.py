# Generated by Django 3.0.2 on 2020-03-01 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200229_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlydonation',
            name='amount',
            field=models.IntegerField(),
        ),
    ]