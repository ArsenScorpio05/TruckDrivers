# Generated by Django 4.2.6 on 2023-11-15 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DriversApp', '0013_truckdriver_contract_expiration_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truckdriver',
            name='contract_expiration_date',
        ),
        migrations.AlterField(
            model_name='truckdriver',
            name='health_document_expiration_date',
            field=models.DateField(),
        ),
    ]
