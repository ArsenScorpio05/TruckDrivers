# Generated by Django 4.2.6 on 2023-11-01 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DriversApp', '0002_truckdriver_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truckdriver',
            name='email',
            field=models.EmailField(default='@example.com', max_length=254),
        ),
    ]
