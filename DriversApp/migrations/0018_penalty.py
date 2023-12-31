# Generated by Django 4.2.6 on 2023-11-15 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DriversApp', '0017_truckdriver_health_document_notified_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalty_date', models.DateField()),
                ('amount_charged', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DriversApp.truckdriver')),
            ],
        ),
    ]
