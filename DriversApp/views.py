from django.shortcuts import render, redirect
from .forms import TruckDriverForm, PenaltyForm
from .models import TruckDriver, Penalty
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_control
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models import Count
import csv
from django.http import HttpResponse
from django.views import View

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('success_page')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials!!!'})
    return render(request, 'login.html')

@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
@login_required
def create_truck_driver(request):
    if request.method == 'POST':
        form = TruckDriverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_truck_driver')
            # return redirect('success_page')  # Create a URL pattern for the success page
    else:
        drivers = TruckDriver.objects.all()
        form = TruckDriverForm()
        
        context = {
            'drivers': drivers,
            'form': form
        }
    return render(request, 'truck_driver_form.html', context)

@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
@login_required
def list_truck_drivers(request):
    drivers = TruckDriver.objects.order_by('first_name')
    
    context = {
        'drivers': drivers
    }
    return render(request, 'truck_driver_list.html', context)

@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
@login_required
def driver_detail(request, driver_id):
    driver = get_object_or_404(TruckDriver, pk=driver_id)
    
    if request.method == 'POST':
        form = TruckDriverForm(request.POST, request.FILES, instance=driver)
        if form.is_valid():
            form.save()
        context = {
            'driver': driver,
            'form': form
        }    
    else:
        form = TruckDriverForm(instance=driver)
        is_driver_detail = True
        context = {
            'driver': driver,
            'form': form,
            'is_driver_detail': is_driver_detail
        }
        
    return render(request, 'driver_detail.html', context)

@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
@login_required
def delete_driver(request, driver_id):
    driver = get_object_or_404(TruckDriver, pk=driver_id)
    driver.delete()
    return redirect('list_drivers')

@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
@login_required
@login_required
def success_page(request):
    context = {
            'username': request.user.username
        }
    return render(request, 'success_page.html', context)


# @cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
# @login_required
# @csrf_exempt
# def upcoming_health_document_expirations(request):
#     today = timezone.now().date()
#     two_weeks_from_now = today + timezone.timedelta(weeks=2)

#     drivers = TruckDriver.objects.filter(health_document_expiration_date__gte=today, health_document_expiration_date__lte=two_weeks_from_now).order_by('health_document_expiration_date')
    
#     context = {
#         'drivers': drivers
#     }
#     return render(request, 'upcoming_health_document_expirations.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
@login_required
@csrf_exempt
def upcoming_driving_licences_expirations(request):
    if request.method == 'POST':
        # Notify drivers via email
        notify_drivers_via_email()
        return redirect('upcoming_driving_licences_expirations')

    today = timezone.now().date()
    two_weeks_from_now = today + timezone.timedelta(weeks=2)

    drivers = TruckDriver.objects.filter(driving_licence_expiration_date__gte=today, driving_licence_expiration_date__lte=two_weeks_from_now).order_by('driving_licence_expiration_date')

    context = {
        'drivers': drivers
    }
    return render(request, 'upcoming_driving_licences_expirations.html', context)


def notify_drivers_via_email():
    today = timezone.now().date()
    two_weeks_from_now = today + timezone.timedelta(weeks=2)
    drivers = TruckDriver.objects.filter(driving_licence_expiration_date__gte=today, driving_licence_expiration_date__lte=two_weeks_from_now).order_by('driving_licence_expiration_date')

    for driver in drivers:
        if not driver.notified:
            formatted_date = driver.driving_licence_expiration_date.strftime('%A, %d - %B - %Y')
            subject = 'Driving License Expiration Notification'
            message = f'Hello {driver.first_name},\n\nYour driving license will expire on: \n{formatted_date}. \nPlease renew it in time.\n\nBest regards,\nThe Truck Drivers App Team'
            from_email = 'cenopython@gmail.com'  # Replace with your sender email
            recipient_list = [driver.email]

            send_mail(subject, message, from_email, recipient_list)
            
            driver.notified = True
            driver.notified_date = timezone.now().date()
            driver.save()
            
            
# Health care notifyier -------------------------------


@cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
@login_required
@csrf_exempt
def upcoming_health_document_expirations(request):
    if request.method == 'POST':
        # Notify drivers via email
        notify_drivers_via_email_for_health_doc()
        return redirect('upcoming_health_document_expirations')

    today = timezone.now().date()
    two_weeks_from_now = today + timezone.timedelta(weeks=2)

    drivers = TruckDriver.objects.filter(health_document_expiration_date__gte=today, health_document_expiration_date__lte=two_weeks_from_now).order_by('health_document_expiration_date')

    context = {
        'drivers': drivers
    }
    return render(request, 'upcoming_health_document_expirations.html', context)



def notify_drivers_via_email_for_health_doc():
    today = timezone.now().date()
    two_weeks_from_now = today + timezone.timedelta(weeks=2)
    drivers = TruckDriver.objects.filter(health_document_expiration_date__gte=today, health_document_expiration_date__lte=two_weeks_from_now).order_by('health_document_expiration_date')

    for driver in drivers:
        if not driver.health_document_notified:
            formatted_date = driver.health_document_expiration_date.strftime('%A, %d - %B - %Y')
            subject = 'Health Document Expiration Notification'
            message = f'Hello {driver.first_name},\n\nYour health document will expire on: \n{formatted_date}. \nPlease renew it in time.\n\nBest regards,\nThe Truck Drivers App Team'
            from_email = 'cenopython@gmail.com'  # Replace with your sender email
            recipient_list = [driver.email]

            send_mail(subject, message, from_email, recipient_list)
            
            driver.health_document_notified = True
            driver.health_document_notified_date = timezone.now().date()
            driver.save()
#----------------------------------------------- 
@cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
@login_required
@csrf_exempt
def upcoming_driver_report_expirations(request):
    if request.method == 'POST':
        # Notify drivers via email
        notify_drivers_via_email_for_driver_report()
        return redirect('upcoming_driver_report_expirations')

    today = timezone.now().date()
    two_weeks_from_now = today + timezone.timedelta(weeks=2)

    drivers = TruckDriver.objects.filter(driver_record_service_report_expiration_date__gte=today, driver_record_service_report_expiration_date__lte=two_weeks_from_now).order_by('driver_record_service_report_expiration_date')

    context = {
        'drivers': drivers
    }
    return render(request, 'upcoming_driver_report_expirations.html', context)



def notify_drivers_via_email_for_driver_report():
    today = timezone.now().date()
    two_weeks_from_now = today + timezone.timedelta(weeks=2)
    drivers = TruckDriver.objects.filter(driver_record_service_report_expiration_date__gte=today, driver_record_service_report_expiration_date__lte=two_weeks_from_now).order_by('driver_record_service_report_expiration_date')

    for driver in drivers:
        if not driver.driver_report_notified:
            formatted_date = driver.driver_record_service_report_expiration_date.strftime('%A, %d - %B - %Y')
            subject = 'Driver Report Expiration Notification'
            message = f'Hello {driver.first_name},\n\nYour driver report will expire on: \n{formatted_date}. \nPlease renew it in time.\n\nBest regards,\nThe Truck Drivers App Team'
            from_email = 'cenopython@gmail.com'  # Replace with your sender email
            recipient_list = [driver.email]

            send_mail(subject, message, from_email, recipient_list)
            
            driver.driver_report_notified = True
            driver.driver_report_notified_date = timezone.now().date()
            driver.save()  
  
  
@cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
@login_required
@csrf_exempt           
def driver_list(request):
    drivers = TruckDriver.objects.all()

    # Calculate the total amount of penalties for each driver
    for driver in drivers:
        drivers = TruckDriver.objects.annotate(total_penalties=Count('penalty')).order_by('-total_penalties')
        
    context = {
        'drivers': drivers,
    }

    return render(request, 'penalty_list.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
@login_required
@csrf_exempt
def penalty_details(request, driver_id):
    driver = get_object_or_404(TruckDriver, pk=driver_id)
    penalties = Penalty.objects.filter(driver=driver).order_by('-penalty_date')
    total_amount = sum(penalty.amount_charged for penalty in penalties)
    
    context = {
        'driver': driver, 
        'penalties': penalties,
        'total_amount': total_amount
    }

    return render(request, 'penalty_details.html', context)



@cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
@login_required
@csrf_exempt
def register_penalty(request):
    if request.method == 'POST':
        form = PenaltyForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the penalty details page for the newly created penalty's driver
            return redirect('penalty_details', driver_id=form.instance.driver.pk)
    else:
        form = PenaltyForm()

    return render(request, 'register_penalty.html', {'form': form})


def edit_penalty(request, penalty_id):
    penalty = get_object_or_404(Penalty, pk=penalty_id)

    if request.method == 'POST':
        form = PenaltyForm(request.POST, instance=penalty)
        if form.is_valid():
            form.save()
            return redirect('penalty_details', driver_id=penalty.driver.pk)
    else:
        form = PenaltyForm(instance=penalty)

    return render(request, 'edit_penalty.html', {'form': form, 'penalty': penalty})


def delete_penalty(request, penalty_id):
    penalty = get_object_or_404(Penalty, pk=penalty_id)
    driver_id = penalty.driver.pk  # Store the driver ID before deleting the penalty
    penalty.delete()
    return redirect('penalty_details', driver_id=driver_id)


class ExportCSVView(View):
    def get(self, request, *args, **kwargs):
        # Retrieve all TruckDriver instances
        drivers = TruckDriver.objects.all()

        # Create a response object with CSV content
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="truck_drivers.csv"'

        # Create a CSV writer
        writer = csv.writer(response)

        # Write header row
        header = [field.name for field in TruckDriver._meta.fields if field.name not in ['photo', 'health_document', 'driving_license', 'pdf_file']]
        writer.writerow(header)

        # Write data rows
        for driver in drivers:
            row = [getattr(driver, field) for field in header]
            writer.writerow(row)

        return response
    
    
class ExportPenaltiesCSVView(View):
    def get(self, request, *args, **kwargs):
        # Retrieve all Penalty instances
        penalties = Penalty.objects.all()

        # Create a response object with CSV content
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="penalties.csv"'

        # Create a CSV writer
        writer = csv.writer(response)

        # Write header row
        header = [field.name for field in Penalty._meta.fields if field.name != 'driver']
        header.append('driver_full_name')  # Add driver_full_name
        writer.writerow(header)

        # Write data rows
        for penalty in penalties:
            row = [getattr(penalty, field) for field in header[:-1]]  # Exclude the last field (driver)
            row.append(f"{penalty.driver.first_name} {penalty.driver.last_name}")  # Add driver_full_name
            writer.writerow(row)

        return response