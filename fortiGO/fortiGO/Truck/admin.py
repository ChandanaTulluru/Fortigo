from django.contrib import admin
from .models import UserLog, Booking, Routes, Trucks, Truck_status, Drivers, FeedbackModel,Rental,RentalTrucks,Cancellation
# Register your models here.
admin.site.register(UserLog)
admin.site.register(Booking)
admin.site.register(Routes)
admin.site.register(Trucks)
admin.site.register(Truck_status)
admin.site.register(Drivers)
#admin.site.register(FeedbackModel)
admin.site.register(Rental)
admin.site.register(RentalTrucks)
admin.site.register(Cancellation)