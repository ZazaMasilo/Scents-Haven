from django.db import models


# Create your models here.
class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    booking_date = models.DateTimeField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"booking for {self.full_name} on {self.booking_date}"

