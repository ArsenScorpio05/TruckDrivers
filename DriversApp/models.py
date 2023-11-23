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
    truck_license = models.CharField(max_length=100)
    health_document_expiration_date = models.DateField()
    driving_licence_expiration_date = models.DateField()
    driver_record_service_report_expiration_date = models.DateField(null=True, blank=True)
    health_document = models.FileField(upload_to='driver_files/', null=True, blank=True)
    driving_license = models.FileField(upload_to='driver_files/', null=True, blank=True)
    
    notified = models.BooleanField(default=False)
    health_document_notified = models.BooleanField(default=False)
    driver_report_notified = models.BooleanField(default=False)
    
    notified_date = models.DateTimeField(null=True, blank=True)
    health_document_notified_date = models.DateTimeField(null=True, blank=True)
    driver_report_notified_date = models.DateTimeField(null=True, blank=True)
    
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)
    
    
    def total_penalties(self):
        return Penalty.objects.filter(driver=self).count()
    
    # Add more fields as needed
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Penalty(models.Model):
    driver = models.ForeignKey(TruckDriver, on_delete=models.CASCADE)
    penalty_date = models.DateField()
    amount_charged = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.driver.first_name} {self.driver.last_name} - Penalty on {self.penalty_date}"