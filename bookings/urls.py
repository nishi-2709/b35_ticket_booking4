from django.urls import path
from .views import BookingCreateView, BookingHistoryView, BookingDetailView

app_name = 'bookings'

urlpatterns = [
    path('create/<int:show_id>/', BookingCreateView.as_view(), name='create'),
    path('history/', BookingHistoryView.as_view(), name='history'),
    path('detail/<int:pk>/', BookingDetailView.as_view(), name='detail'),
] 