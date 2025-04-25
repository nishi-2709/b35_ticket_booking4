from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Count, Sum
from django.utils import timezone
from shows.models import Show
from bookings.models import Booking

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class AdminDashboardView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'admin_panel/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_shows'] = Show.objects.count()
        context['total_bookings'] = Booking.objects.count()
        context['total_revenue'] = Booking.objects.aggregate(Sum('total_price'))['total_price__sum'] or 0
        context['upcoming_shows'] = Show.objects.filter(date__gt=timezone.now()).count()
        return context

class ShowManagementView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Show
    template_name = 'admin_panel/show_management.html'
    context_object_name = 'shows'
    paginate_by = 10
    ordering = ['-date']

class ShowCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Show
    template_name = 'admin_panel/show_form.html'
    fields = ['title', 'description', 'date', 'venue', 'total_seats', 'available_seats', 'price', 'image']
    success_url = reverse_lazy('admin_panel:shows')

    def form_valid(self, form):
        messages.success(self.request, 'Show created successfully!')
        return super().form_valid(form)

class ShowUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Show
    template_name = 'admin_panel/show_form.html'
    fields = ['title', 'description', 'date', 'venue', 'total_seats', 'available_seats', 'price', 'image']
    success_url = reverse_lazy('admin_panel:shows')

    def form_valid(self, form):
        messages.success(self.request, 'Show updated successfully!')
        return super().form_valid(form)

class ShowDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Show
    template_name = 'admin_panel/show_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:shows')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Show deleted successfully!')
        return super().delete(request, *args, **kwargs)

class BookingManagementView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = Booking
    template_name = 'admin_panel/booking_management.html'
    context_object_name = 'bookings'
    paginate_by = 10
    ordering = ['-booking_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shows'] = Show.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        show_id = self.request.GET.get('show')
        if show_id:
            queryset = queryset.filter(show_id=show_id)
        return queryset 