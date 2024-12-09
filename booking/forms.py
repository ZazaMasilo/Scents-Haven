from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'booking_date', 'special_requests']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'booking_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }