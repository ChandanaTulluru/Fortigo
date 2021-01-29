from rest_framework import serializers
from Truck.models import Booking

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['user_name','user_email','booking_id','source','destination']
