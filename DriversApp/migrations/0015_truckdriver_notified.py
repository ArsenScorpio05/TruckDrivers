# Generated by Django 4.2.6 on 2023-11-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DriversApp', '0014_remove_truckdriver_contract_expiration_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='truckdriver',
            name='notified',
            field=models.BooleanField(default=False),
        ),
    ]
