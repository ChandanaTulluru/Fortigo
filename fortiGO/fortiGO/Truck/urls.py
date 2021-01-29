from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from Truck.views import MyBookingsView, MyCancellationsView#new

urlpatterns = [
    #path('', views.home, name='Truck-home'),
    path('',views.register,name = 'Truck-register'),
    path('UserPage/', views.UserPage, name='UserPage-home'),
    #path('UserPage/Bookings/',views.Bookings, name = 'Bookings-home'),
    path('UserBookings/',views.UserBookings, name='Routes-home'),
    path('login/',auth_views.LoginView.as_view(template_name = 'Truck/login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'Truck/logout.html'),name = 'logout'),
    path('Faq/',views.Faq, name = 'faq'),
    path('Payments/',views.HomePageView.as_view(),name='Payments'),
    path('charge/', views.charge, name='charge'),
    path('email/',views.Email, name='eemail'),
    path('feedback/', views.Feedback, name="Feedback.Portal"),
    path('result/', views.FeedbackResult, name="Feedback.Result"),
    path('rentals/',views.RentTruck,name = "Truck-Rentals"),
    path('mybookings/', MyBookingsView.as_view(template_name = 'Truck/mybookings.html'), name = 'mybookings'),
    path('mycancellations/', MyCancellationsView.as_view(template_name = 'Truck/mycancellations.html'), name = 'cancelled'),
    path('mybookings/cancelled/', views.MyBookings_delete, name = 'cancel_bookings'),
    path('refund/', views.refund, name='refund'),

]
