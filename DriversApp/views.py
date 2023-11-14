from django.shortcuts import render, redirect
from .forms import TruckDriverForm
from .models import TruckDriver
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_control
from django.utils import timezone


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