from django import forms
from .models import TruckDriver
from django.forms.widgets import ClearableFileInput




class TruckDriverForm(forms.ModelForm):
        
    class Meta:
        model = TruckDriver
        fields = ['photo', 'first_name', 'last_name', 'birthday', 'email', 'phone_number', 'truck_license', 'health_document_expiration_date', 'driving_licence_expiration_date', 'health_document', 'driving_license']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'health_document_expiration_date': forms.DateInput(attrs={'type': 'date'}),
            'driving_licence_expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
        labels = {
            'photo': 'Driver Photo',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'birthday': 'Date of Birth',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'truck_license': 'Truck Licence Number',
            'health_document_expiration_date': 'Health Document Expiration Date',
            'driving_licence_expiration_date': 'Driving Licence Expiration Date',
            'health_document': 'Picture for Health Document',
            'driving_license': 'Picture for Driving Licence'
        }