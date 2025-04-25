from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction
from .models import Booking
from shows.models import Show

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    template_name = 'bookings/booking_create.html'
    fields = ['number_of_tickets', 'seat_numbers']
    success_url = reverse_lazy('bookings:history')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        show_id = self.kwargs.get('show_id')
        context['show'] = get_object_or_404(Show, pk=show_id)
        return context

    def form_valid(self, form):
        show = get_object_or_404(Show, pk=self.kwargs.get('show_id'))
        if not show.is_available():
            messages.error(self.request, 'Sorry, this show is no longer available.')
            return self.form_invalid(form)

        with transaction.atomic():
            booking = form.save(commit=False)
            booking.user = self.request.user
            booking.show = show
            booking.total_price = show.price * booking.number_of_tickets

            if booking.number_of_tickets > show.available_seats:
                messages.error(self.request, 'Not enough seats available.')
                return self.form_invalid(form)

            show.available_seats -= booking.number_of_tickets
            show.save()
            booking.save()

            messages.success(self.request, 'Booking confirmed successfully!')
            return super().form_valid(form)

class BookingHistoryView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/booking_history.html'
    context_object_name = 'bookings'
    paginate_by = 10

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'bookings/booking_detail.html'
    context_object_name = 'booking'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user) 