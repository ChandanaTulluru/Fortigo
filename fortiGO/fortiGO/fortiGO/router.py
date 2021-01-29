from Truck.api.viewsets import BookingViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Truck',BookingViewSet,base_name = 'Truck')
