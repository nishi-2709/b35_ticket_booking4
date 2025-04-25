from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('shows/', include('shows.urls')),
    path('bookings/', include('bookings.urls')),
    path('admin-panel/', include('admin_panel.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 