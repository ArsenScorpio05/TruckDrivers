# Generated by Django 4.2.6 on 2023-11-01 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DriversApp', '0005_alter_truckdriver_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truckdriver',
            name='photo',
            field=models.ImageField(blank=True, default='media/images/Default-avatar.jpg', null=True, upload_to='driver_photos/'),
        ),
    ]
