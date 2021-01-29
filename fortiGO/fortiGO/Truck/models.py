from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from django.conf import settings
#from django.db.models.signals import post_save, pre_save

# Create your models here.
class UserLog(models.Model):
    userlogid = models.AutoField(primary_key = True)
    email = models.CharField(max_length = 150)
    password = models.CharField(max_length = 150)
    name = models.CharField(max_length = 150)
    pincode = models.IntegerField()
    date_registered = models.DateTimeField(default = timezone.now)

class Routes(models.Model):
    routeid = models.CharField(primary_key=True, max_length=150)
    start = models.CharField(max_length = 150)
    int_st2 = models.CharField(max_length = 150)
    int_st3 = models.CharField(max_length = 150)
    int_st4 = models.CharField(max_length = 150)
    end = models.CharField(max_length = 150)
    price = models.IntegerField()

class Drivers(models.Model):
	driver_id = models.AutoField(primary_key=True)
	driver_name = models.CharField(max_length=150)
	driver_mobile = models.CharField(max_length=150)
	driver_email = models.CharField(max_length=150)



class Trucks(models.Model):
	truck_id = models.CharField(primary_key=True, max_length=150)
	driver_id = models.ForeignKey(Drivers, on_delete=models.PROTECT)
	max_load = models.IntegerField()
	route_id = models.ForeignKey(Routes, on_delete = models.PROTECT)


class Booking(models.Model):
    user_name = models.CharField(max_length=150)
    user_email = models.CharField(max_length=150)
    booking_id = models.AutoField(primary_key = True)
    #user_id = models.ForeignKey(User,on_delete = models.PROTECT)
#    route_id = models.ForeignKey(Routes,on_delete = models.PROTECT)
   # truck_id = models.ForeignKey(Trucks,on_delete = models.PROTECT,default = 0)
    ROUTES = (
        ('HYDERABAD', 'HYDERABAD'),
        ('CHENNAI', 'CHENNAI'),
        ('MUMBAI', 'MUMBAI'),
        ('BANGALORE', 'BANGALORE'),
        ('PUNE', 'PUNE'),
        ('SHAHBAD', 'SHAHBAD'),
        ('TANDUR', 'TANDUR'),
        ('RAICHUR', 'RAICHUR'),
        ('CUDDAPAH', 'CUDDAPAH'),
        ('ARAKKONAM', 'ARAKKONAM'),
        ('ADONI', 'ADONI'),
        ('HINDUPUR', 'HINDUPUR'),
        ('WARANGAL', 'WARANGAL'),
        ('VIJAYAWADA', 'VIJAYAWADA'),
        ('NELLORE', 'NELLORE'),
        ('KURNOOL', 'KURNOOL'),
        ('ANANTAPUR', 'ANANTAPUR'),
        ('GAURIBIDANUR', 'GAURIBIDANUR'),
        ('SHOLINGHUR', 'SHOLINGHUR'),
        ('AMBUR', 'AMBUR'),
        ('WHITEFIELD', 'WHITEFIELD'),
    )

    source = models.CharField(
        max_length=30,
        choices=ROUTES,
        blank=True,
        default='HYDERABAD',
        help_text='Routes',
    )
    #source = models.CharField(max_length = 150)

    destination = models.CharField(
        max_length=30,
        choices=ROUTES,
        blank=True,
        default='HYDERABAD',
        help_text='Routes',
    )
    #destination = models.CharField(max_length = 150)
    choices_1 = (
        (250,250),
        (500,500),
        (750,750),
        (1000,1000),
    )
    #payment_status = models.CharField(max_length = 150)
    load_weight = models.IntegerField(choices = choices_1)
    date_booked = models.DateTimeField(default = timezone.now)
    date_journey = models.CharField(max_length=150)




class Truck_status(models.Model):
    truck_id = models.ForeignKey(Trucks, on_delete=models.PROTECT)
    route_id = models.ForeignKey(Routes, on_delete=models.PROTECT)
    starting_date = models.CharField(max_length=150)
    arriving_date = models.CharField(max_length=150)
    truck_weight = models.IntegerField()


class Payments(models.Model):
	#mode_payment = models.CharField(max_length = 150)
	amount = models.FloatField()
	date_payment = models.DateTimeField(default=timezone.now)
	email = models.CharField(max_length=150)


class FeedbackModel(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT) # foreign key from userlog

	# rating 1 to 5 questions
	rating_Q1 = models.IntegerField() # likeliness of recommendation
	rating_Q2 = models.IntegerField() # experience with services
	rating_Q3 = models.IntegerField() # experience with website
	rating_Q4 = models.IntegerField() # interaction with drivers

	# text area questions
	text_Q1 = models.TextField() # other features you'd like to see
	text_Q2 = models.TextField() # anythong else you'd like to tell u

class RentalTrucks(models.Model):
    truck_id = models.CharField(primary_key = True,max_length = 150)
    driver_id = models.ForeignKey(Drivers, on_delete=models.PROTECT)
    max_load = models.IntegerField()



class Rental(models.Model):
    #truck_id = models.ForeignKey(RentalTrucks,on_delete = models.PROTECT)
    #user_id = models.ForeignKey(User,on_delete = models.PROTECT)
    username = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 150)
    date = models.CharField(max_length = 150)
    purpose = models.TextField(max_length = 300)
    duration = models.IntegerField()



class Cancellation(models.Model):
    user_name = models.CharField(max_length=150)
    user_email = models.CharField(max_length=150)
    booking_id = models.IntegerField()
    cancellation_id = models.AutoField(primary_key = True)
#    user_id = models.ForeignKey(UserLog,on_delete = models.PROTECT)
#    route_id = models.ForeignKey(Routes,on_delete = models.PROTECT)
    #truck_id = models.ForeignKey(Trucks,on_delete = models.PROTECT,default = 0)
    ROUTES = (
        ('HYDERABAD', 'HYDERABAD'),
        ('CHENNAI', 'CHENNAI'),
        ('MUMBAI', 'MUMBAI'),
        ('BANGALORE', 'BANGALORE'),
        ('PUNE', 'PUNE'),
        ('SHAHBAD', 'SHAHBAD'),
        ('TANDUR', 'TANDUR'),
        ('RAICHUR', 'RAICHUR'),
        ('CUDDAPAH', 'CUDDAPAH'),
        ('ARAKKONAM', 'ARAKKONAM'),
        ('ADONI', 'ADONI'),
        ('HINDUPUR', 'HINDUPUR'),
        ('WARANGAL', 'WARANGAL'),
        ('VIJAYAWADA', 'VIJAYAWADA'),
        ('NELLORE', 'NELLORE'),
        ('KURNOOL', 'KURNOOL'),
        ('ANANTAPUR', 'ANANTAPUR'),
        ('GAURIBIDANUR', 'GAURIBIDANUR'),
        ('SHOLINGHUR', 'SHOLINGHUR'),
        ('AMBUR', 'AMBUR'),
        ('WHITEFIELD', 'WHITEFIELD'),
    )

    source = models.CharField(
        max_length=30,
        choices=ROUTES,
        blank=True,
        default='HYDERABAD',
        help_text='Routes',
    )
    #source = models.CharField(max_length = 150)

    destination = models.CharField(
        max_length=30,
        choices=ROUTES,
        blank=True,
        default='HYDERABAD',
        help_text='Routes',
    )
    #destination = models.CharField(max_length = 150)
    choices_1 = (
        (250,250),
        (500,500),
        (750,750),
        (1000,1000),
    )
    #payment_status = models.CharField(max_length = 150)
    load_weight = models.IntegerField(choices = choices_1)
    date_booked = models.CharField(max_length=150)
    date_journey = models.CharField(max_length=150)
    date_cancelled = models.DateTimeField(default = timezone.now)
    
