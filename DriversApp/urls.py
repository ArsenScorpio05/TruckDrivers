from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ExportCSVView, ExportPenaltiesCSVView



urlpatterns = [
    path('', views.login_view, name='login'),
    path('create_truck_driver/', views.create_truck_driver, name='create_truck_driver'),
    path('success/', views.success_page, name='success_page'),  # Add this line
    path('list_drivers/', views.list_truck_drivers, name='list_drivers'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('driver/<int:driver_id>/', views.driver_detail, name='driver_detail'),
    path('delete_driver/<int:driver_id>/', views.delete_driver, name='delete_driver'),
    path('upcoming_health_document_expirations/', views.upcoming_health_document_expirations, name='upcoming_health_document_expirations'),
    path('upcoming_driving_licences_expirations/', views.upcoming_driving_licences_expirations, name='upcoming_driving_licences_expirations'),
    path('upcoming_driver_report_expirations/', views.upcoming_driver_report_expirations, name='upcoming_driver_report_expirations'),
    path('driver_list/', views.driver_list, name='driver_list'),
    path('penalty_details/<int:driver_id>/', views.penalty_details, name='penalty_details'),
    path('register_penalty/', views.register_penalty, name='register_penalty'),
    path('edit_penalty/<int:penalty_id>/', views.edit_penalty, name='edit_penalty'),
    path('delete_penalty/<int:penalty_id>/', views.delete_penalty, name='delete_penalty'),
    path('export-csv/', ExportCSVView.as_view(), name='export_csv'),
    path('export-penalties-csv/', ExportPenaltiesCSVView.as_view(), name='export_penalties_csv'),
]


