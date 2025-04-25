from django.urls import path
from .views import ShowListView, ShowDetailView

app_name = 'shows'

urlpatterns = [
    path('', ShowListView.as_view(), name='list'),
    path('<int:pk>/', ShowDetailView.as_view(), name='detail'),
] 