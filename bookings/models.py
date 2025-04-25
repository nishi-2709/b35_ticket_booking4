from django.db import models
from django.conf import settings
from shows.models import Show

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    number_of_tickets = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)
    seat_numbers = models.CharField(max_length=200)  # Comma-separated seat numbers

    def __str__(self):
        return f"{self.user.email} - {self.show.title}"

    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = self.show.price * self.number_of_tickets
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-booking_date'] 