from django.urls import path
from .views import (
    AdminDashboardView,
    ShowManagementView,
    ShowCreateView,
    ShowUpdateView,
    ShowDeleteView,
    BookingManagementView
)

app_name = 'admin_panel'

urlpatterns = [
    path('', AdminDashboardView.as_view(), name='dashboard'),
    path('shows/', ShowManagementView.as_view(), name='shows'),
    path('shows/create/', ShowCreateView.as_view(), name='show_create'),
    path('shows/<int:pk>/update/', ShowUpdateView.as_view(), name='show_update'),
    path('shows/<int:pk>/delete/', ShowDeleteView.as_view(), name='show_delete'),
    path('bookings/', BookingManagementView.as_view(), name='bookings'),
] 