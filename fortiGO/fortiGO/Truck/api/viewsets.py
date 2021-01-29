from Truck.models import Booking
from .serializers import BookingSerializer
from rest_framework import viewsets
from rest_framework.response import Response

'''class BookingViewSet(viewsets.ViewSet):
    def list(self,request):
        query_set = Booking.objects.all()
        serializer = BookingSerializer(query_set,many = True)
        return Response(serializer.data)'''


class BookingViewSet(viewsets.ModelViewSet):
    query_set = Booking.objects.all()
    serializer_class = BookingSerializer
