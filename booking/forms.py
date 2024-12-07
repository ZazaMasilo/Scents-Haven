from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'booking_date', 'special_requests']
        widgets = {
            'booking_date': forms.DateTimeInput(attrs={'date': 'datetime-local'}),
        }