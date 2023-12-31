# Generated by Django 4.2.6 on 2023-11-15 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DriversApp', '0012_alter_truckdriver_driving_licence_expiration_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='truckdriver',
            name='contract_expiration_date',
            field=models.DateField(default='2024-01-01', verbose_name='%d-%m-%Y'),
        ),
        migrations.AlterField(
            model_name='truckdriver',
            name='health_document_expiration_date',
            field=models.DateField(default='2024-01-01', verbose_name='%d-%m-%Y'),
        ),
    ]
