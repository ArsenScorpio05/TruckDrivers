from django.db import models
from multiupload.fields import MultiFileField
from django.utils import timezone

today = timezone.now().date()
class TruckDriver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField(default='2000-01-01')
    photo = models.ImageField(upload_to='driver_photos/', null=True, blank=True)
    email = models.EmailField(default='@example.com')
    phone_number = models.CharField(max_length=15)
    truck_license = models.CharField(max_length=10)
    health_document_expiration_date = models.DateField()
    driving_licence_expiration_date = models.DateField()
    health_document = models.FileField(upload_to='driver_files/', null=True, blank=True)
    driving_license = models.FileField(upload_to='driver_files/', null=True, blank=True)
    
    # Add more fields as needed
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

