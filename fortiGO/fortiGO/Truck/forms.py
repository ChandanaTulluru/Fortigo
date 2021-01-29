from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Booking,Routes, Payments, Rental

class DateInput(forms.DateInput):
	input_type = 'date'



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    pincode = forms.IntegerField()
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username','email','password1','password2','pincode']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

class BookingForm(forms.ModelForm):

	class Meta:
		model = Booking
		fields = ['user_name', 'user_email', 'source', 'destination', 'load_weight', 'date_journey']
		widgets = {'date_journey':DateInput()}


class PaymentForm(forms.ModelForm):
	class Meta:
		model = Payments
		fields = ['amount','email','date_payment']

class TruckRentalForm(forms.ModelForm):
	class Meta:
		model = Rental
		fields = ['date','purpose','duration','username','email']
