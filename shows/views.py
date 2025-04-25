from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .models import Show

class ShowListView(ListView):
    model = Show
    template_name = 'shows/show_list.html'
    context_object_name = 'shows'
    paginate_by = 9

    def get_queryset(self):
        queryset = Show.objects.filter(date__gt=timezone.now())
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class ShowDetailView(DetailView):
    model = Show
    template_name = 'shows/show_detail.html'
    context_object_name = 'show'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        show = self.get_object()
        context['is_available'] = show.is_available()
        if self.request.user.is_authenticated:
            context['user_bookings'] = show.booking_set.filter(user=self.request.user)
        return context 