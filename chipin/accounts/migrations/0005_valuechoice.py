# Generated by Django 3.0.2 on 2020-02-28 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200228_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValueChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]