from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.login_view, name='login'),
    path('create_truck_driver/', views.create_truck_driver, name='create_truck_driver'),
    path('success/', views.success_page, name='success_page'),  # Add this line
    path('list_drivers/', views.list_truck_drivers, name='list_drivers'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('driver/<int:driver_id>/', views.driver_detail, name='driver_detail'),
    path('delete_driver/<int:driver_id>/', views.delete_driver, name='delete_driver'),
]


