from django.shortcuts import render,redirect
from .models import Booking, FeedbackModel
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import BookingForm, PaymentForm, TruckRentalForm
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Routes,Truck_status,Trucks,Booking,Cancellation
from django.contrib.auth.models import User
import stripe
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login
import time,datetime
from django.http import HttpResponse,HttpResponseRedirect


from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string#new

from django.views.generic import ListView#new
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.core.mail import send_mail

stripe.api_key = settings.STRIPE_SECRET_KEY



def Email(request):

	subject = 'Thank you for making a booking with us'
	message = 'Hello'
	email_from = settings.EMAIL_HOST_USER
	#recipient_list = ['bhavana.t17@iiits.in',]
	#route = Routes.objects.all()
	recipient_list = [email,]
	amount = amount_route + load*5
	posts = [{'source':source,'destination':destination,'amount':amount, 'name':name,'date':date}]
	context = {'posts':posts}
	msg_html = render_to_string('Truck/email.html',context)
	send_mail( subject, message, email_from, recipient_list, html_message=msg_html, )

	return redirect('Payments')



class HomePageView(TemplateView):
	template_name = 'Truck/payment_stripe.html'

	def get_context_data(self, **kwargs): # new

		context = super().get_context_data(**kwargs)
		context['key'] = settings.STRIPE_PUBLISHABLE_KEY
		return context


def charge(request): # new
	if request.method == 'POST':
		charge = stripe.Charge.create(
			amount=5*load + amount_route,
			currency='usd',
			description='A Django charge',
			source=request.POST['stripeToken']
		)
		Posts = [{'amount':5*load + amount_route}]
		context = {'Posts':Posts}
		return render(request, 'Truck/charge.html',context)





def Faq(request):
	return render(request,'Truck/faq.html')



def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			new_user = authenticate(username=form.cleaned_data['username'],
									password=form.cleaned_data['password1'],
									)
			login(request, new_user)
			return redirect('Routes-home')

	else:
		form = UserRegistrationForm()
	return render(request,'Truck/index.html',{'form':form})

@login_required
def UserBookings(request):

	if request.method == 'POST':
		form_1 = BookingForm(request.POST)
		if form_1.is_valid():
			errors = []
			global source, destination, load, email, name,date
			source = form_1.cleaned_data.get('source')
			destination = form_1.cleaned_data.get('destination')
			load = form_1.cleaned_data.get('load_weight')
			email = form_1.cleaned_data.get('user_email')
			name = form_1.cleaned_data.get('user_name')
			date = form_1.cleaned_data.get('date_journey')

			#posts = [{'source':source,'destination':destination,}]
			#context = {'posts':posts}
		  #context = {'posts':posts}
			date_1 = time.strptime(date,"%Y-%m-%d")
			date_2 = str(datetime.date.today())
			date_3 = time.strptime(date_2,'%Y-%m-%d')
			if validate_route(source,destination) == 0 and date_1 > date_3:
				form_1.save()
				#x, str1 = 
				if allocateTruck(source,destination,load,date) == 0:
					#truck_id = str1
					#Booking_data = Booking.objects.filter(user_name=User).first()
					#print(User.username)
					return redirect('eemail')
			else:
				errors.append('You are out')
	else:
		form_1 = BookingForm()
	return render(request,'Truck/bookings_1.html',{'form_1':form_1})



def validate_route(source,destination):
	temp_source = source
	temp_destination = destination
	route_ids = ['MUMHYD','MUMCHE','MUMBAN','HYDMUM','HYDBAN','HYDCHE','CHEMUM','CHEHYD','CHEBAN','BANMUM','BANHYD','BANCHE']
	route = Routes.objects.all()
	start =[]
	int_1 = []
	int_2 = []
	int_3 = []
	end = []

	route_list = Routes.objects.all()
	for route in route_list:
		start.append(route.start)
		int_1.append(route.int_st2)
		int_2.append(route.int_st3)
		int_3.append(route.int_st4)
		end.append(route.end)

	for i in range(12):
		temp_source = -1
		temp_destination = -1

		routes = [start[i],int_1[i],int_2[i],int_3[i],end[i]]
		for j in range(5):
			if source == routes[j]:
				temp_source = j
			if destination == routes[j]:
				temp_destination = j

		if temp_source < temp_destination and temp_source != -1 and temp_destination != -1 :
			return 0

	return 1



#from Truck import signup
# Create your views here.

def home(request):
	return render(request, 'Truck/MainPage.html')
def signup(request):
	return render(request,'Truck/signup.html')

'''def register(request):
	print(request.POST)
	email = request.POST['email']
	password = request.POST['password']
	name = request.POST['name']
	pincode = request.POST['pincode']
	if UserLog.objects.filter(email = email):
		#messages.info(request,f'User Already Exists')
		return render(request,'Truck/signup.html',)
	userlog = UserLog.objects.create(email = email,password = password,name = name,pincode = pincode)
	print("You are Registered Successfully")
	return render(request,'Truck/base.html')'''

@login_required
def Payment_valid(request):
	if request.method == 'POST':
		form_2 = PaymentForm(request.POST)
		form_2.fields['email'] = 'bhavana.t17@iiits.in'
		form_2.fields['amount'] = 500
		if form_2.is_valid():
			messages.success(request, f'Payment successful!')
			form_2.save()
			User_1 = User.username
			Booking_data = Booking.objects.filter(user_name=User).first()
			#Booking_1=Booking_data
			#return render(request, 'Truck/UserPage.html')
			return redirect('register')
	else:
		form_2 = PaymentForm()
	User_1 = User.username
	Booking_data = Booking.objects.filter(user_name=User_1).first()
	#Booking_1=Booking_data
	return render(request,'Truck/payments.html',{'form_2':form_2,'Booking_1':Booking_data})


def UserPage(request):
	return render(request, 'Truck/UserPage.html')

def Bookings(request):
	return render(request, 'Truck/bookings_1.html')

'''def UserBookings(request):
	print("Request Object :{}".format(request.POST))
	fullname = request.POST['field1']
	email = request.POST['field2']
	source = request.POST['field4']
	destination = request.POST['field5']
	load = request.POST['field6']
	booking = Booking.objects.create(user_name=fullname,user_email=email,source=source,destination=destination,load_weight=load)
	return render(request, 'Truck/MainPage.html')'''

@login_required
def Feedback(request):
	Rating_Qs = [
		"How likely are you to recommend our service to your friends and/or family?",
		"How was your experience with our services?",
		"How was your experience with our website?",
		"How was your interaction with our drivers?"
	]

	Text_Qs = [
		"What other features would you like to see in our website?",
		"Is there anything else you would like to tell us?"
	]

	context = {
		'r_qs': Rating_Qs,
		't_qs': Text_Qs,
		'r_len': range(len(Rating_Qs)),
		't_len': range(len(Text_Qs))
	}
	print(context)
	return render(request, 'Truck/contact1.html', context=context)

def FeedbackResult(request):
	if request.method == "POST":
		print(request.POST)

		ratings = {}
		texts = {}

		# parsing the request object
		for i in request.POST:
			if i.startswith('rb'):
				ratings['rating_Q' + i[-1]] = int(request.POST[i])
			elif i.startswith('text'):
				texts['text_Q' + i[-1]] = request.POST[i]

		final_dict = {**ratings, **texts}
		print("final_dict:", final_dict)
		# parsing the user object
		user = request.user
		print("user:", user, type(user))
		# creating a new record
		try:
			new_feedback = FeedbackModel.objects.create(user=user, **final_dict)
			print("new_feedback:", new_feedback)
		except Exception as e:
			print(e, type(e))
	else:
		print("Don't have anything ...")

	return render(request, 'Truck/FeedbackResult.html')

def RentTruck(request):
	if request.method == 'POST':
		form_4 = TruckRentalForm(request.POST)
		if form_4.is_valid():
			form_4.save()
			return redirect('UserPage-home')
	else:
		form_4 = TruckRentalForm()

	return render(request,'Truck/rentals.html',{'form_4' : form_4})

#def allocateRentaltruck(date,duration):
def getValidroutes(source,destination):
	start =[]
	int_1 = []
	int_2 = []
	int_3 = []
	end = []
	keys = []
	valid_routes = []

	route_list = Routes.objects.all()
	for route in route_list:
		start.append(route.start)
		int_1.append(route.int_st2)
		int_2.append(route.int_st3)
		int_3.append(route.int_st4)
		end.append(route.end)
		keys.append(route.routeid)

	for i in range(12):
		temp_source = -1
		temp_destination = -1

		routes = [start[i],int_1[i],int_2[i],int_3[i],end[i]]
		for j in range(5):
			if source == routes[j]:
				temp_source = j
			if destination == routes[j]:
				temp_destination = j

		if temp_source < temp_destination and temp_source != -1 and temp_destination != -1 :
			valid_routes.append(keys[i])

	return valid_routes

def allocateTruck(source,destination,load,date):
	valid_routes = getValidroutes(source,destination)
	trucks = []
	global amount_route
	for i in range(len(valid_routes)):
		trucks.append(Trucks.objects.filter(route_id = valid_routes[i]))

	#print(trucks)
	#print(len(trucks[0]))
	dates = Truck_status.objects.filter(starting_date=date)
	if len(dates) == 0:
		Truck_status.objects.create(truck_id = (Trucks.objects.filter(route_id = valid_routes[0]))[0],route_id = (Routes.objects.filter(routeid = valid_routes[0]))[0],starting_date = date,arriving_date = date,truck_weight = load)
		route_amount = Routes.objects.filter(routeid = valid_routes[0])
		print("payment")
		amount_route = route_amount[0].price
		print (route_amount[0].price)
		#str1 = str(Truck_status.truck_id)
		return 0 
	else:
		min_load = 1000
		min_truck = 0
		#print(len(trucks))
		for i in range(len(trucks[0])):

			status_1 = Truck_status.objects.filter(truck_id = trucks[0][i],starting_date = date)
			#print(status)
			if len(status_1) == 0:
				load_occupied = 0
			else:
				status = Truck_status.objects.get(truck_id = trucks[0][i],starting_date = date)
				load_occupied = status.truck_weight



			if (1000-load_occupied) >= load and (1000-load_occupied) <= min_load:
				min_truck = trucks[0][i]
				min_load = 1000-load_occupied
				load_occupied = min_load
		#print(load_occupied)
		#print((Trucks.objects.filter(truck_id = min_truck))[0])
		#print((Trucks.objects.filter(truck_id = min_truck)))
		#print(min_truck.truck_id)
		if min_truck!=0:
			truck_check = Truck_status.objects.filter(truck_id = (Trucks.objects.filter(truck_id = min_truck.truck_id))[0],starting_date = date)


			if len(truck_check)!=0:
				if min_truck != 0:
					print((Trucks.objects.filter(truck_id = min_truck.truck_id)))
					t = Truck_status.objects.get(truck_id = (Trucks.objects.filter(truck_id = min_truck.truck_id))[0],starting_date = date)
					t.truck_weight += load
					t.save()
			else:
				Truck_status.objects.create(truck_id = (Trucks.objects.filter(truck_id = min_truck.truck_id))[0],route_id = (Routes.objects.filter(routeid = valid_routes[0]))[0],starting_date = date,arriving_date = date,truck_weight = load)
				route_amount = Routes.objects.filter(routeid = valid_routes[0])
				print("payment")
				amount_route = route_amount[0].price
				print (route_amount[0].price)
			

			#str1 = str(Truck_status.truck_id)
			return 0#, str1



class MyBookingsView(ListView):
	model = Booking

	def head(self, *args, **kwargs):
		response = HttpResponse('')
		return response


def MyBookings_delete(request):
	if request.method == 'POST':
		c = request.POST['Cancelled']
		obj = Booking.objects.get(booking_id=c)
		model = Booking
		global date_21
		date_21 = str(datetime.date.today())
		us = obj.user_name
		ue = obj.user_email
		bi = c#obj.booking_id
		s = obj.source
		d = obj.destination
		lw = obj.load_weight
		db = obj.date_booked
		dj = obj.date_journey
		Cancelled = Cancellation.objects.create(user_name=us, user_email = ue, booking_id = bi, source = s, destination = d, load_weight = lw, date_booked = db, date_journey= dj)
						
		Cancelled.save()
		recipient_list = [ue,]
		send_mail("fortigo cancellation mail","Your cancellation is successful..!Your refund amount will reflect in your account within 6 bussiness days,Thank You.","fortigotruck@gmail.com",recipient_list)
				

		obj.delete()
		objs = Booking.objects.all()
		context = {'objs':objs}

		#return redirect('../')
	
	return render(request, 'Truck/refund.html',context=context)


class MyCancellationsView(ListView):
	model = Cancellation

	def head(self, *args, **kwargs):
		response = HttpResponse('')
		return response

def refund(request):
	if request.method == "POST":
		Posts = [{'amount':5*load + amount_route}]
		context = {'Posts':Posts}
		return render(request,'Truck/refund.html')