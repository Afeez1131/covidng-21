from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Total
from .serializer import TotalSerializer, Serializer#, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.renderers import StaticHTMLRenderer
# from total.decorators import add_get_request
# from django.views.decorators.http import require_http_methods
# Create your views here.
	

def home(request):

	return render(request, 'index.html', {})

def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		print(name, email, message)
		# send_mail(subject='API message',
  #   			message= message,
  #   			from_email= email,
  #   			recipient_list= [settings.EMAIL_HOST_USER])
		messages.success(request, 'Message sent Successfully')
		return redirect('home')
	else:
		return render(request, 'index.html', {})


class endpoints(APIView):

	def get(self, request):

		return Response([
		{"endpoint": 'description',
		"api/v2/": 'endpoints home'},
		{"register": 'Page to register user'},
		{"login": 'Login Page, to get token after login'},
		{"login/username=<username>&password=<password>/": 'a GET reqest to this endpoint with a registered users username & pasword return the token for the user'},

		{"api/v2/all/token": 'return all data from the beginning of corona virus till today'},

		{"api/v2/today/token": 'return the data for today'},

		{"api/v2/dates/2020-10-1:2020-11-10:2020-12-10/token": 'return the data for the three dates seperated by :'},

		{"api/v2/from/2020-22-10/token": 'return the datas starting from 2020-22-10',},

		{"api/v2/yesterday/token": 'return the data for yesterday'},

		{"api/v2/date/2020-10-20/token": 'return the data for the specify date'},

		])


def login_user(request):
	next = request.GET.get('next')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			
		else:
			messages.warning(request, 'Incorrect Username and / or Password')
	# else:
	#     form = LoginForm()
	return render(request, 'login.html', {'form': form,})

def logout_user(request):
	logout(request)

	return redirect('home')

@login_required
def profile(request):
	user = request.user
	return render(request, 'profile.html', {'user': user})

def register_user(request):
	new_user = None
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			new_user = form.save(commit=False)
			new_user.set_password(password)
			new_user.save()
			Token.objects.create(user=new_user)
			messages.info(request, 'registration successfull, Login First')
			return redirect('profile')
			# return render(request, 'register_success.html', {'new_user': new_user})
	else:
		form = RegisterForm()
	return render(request, 'register.html', {'form': form})

class LoginView(APIView):
	permission_classes = ()

	def post(self, request, username, password):
		username = username
		password = password
		# username = request.data.get('username')
		# password = request.data.get('password')
		user = authenticate(username=username, password=password)
		if user:
			return Response({"token": user.auth_token.key})

		else:
			return Response({"error": "wrong credentials"})

class TotalListView(APIView):
	'''
	This will return all datas from the commencement of Corona Virus till today
	'''
	# permission_classes = (IsAuthenticated,)
	def get(self, request, token):
		try:
			user = get_object_or_404(User, auth_token=token)
		except Exception as DoesNotExist:
			user = None
		print(user)
		if user:
			obj = Total.objects.all()
			# lookup_field = 'hello'
			data = TotalSerializer(obj, many=True).data
			return Response(data)
		else:
			return Response({'error': 'Invalid Token'})

class GetDateView(APIView):
	def get(self, request, day, token):
		try:
			user = get_object_or_404(User, auth_token=token)
		except Exception as DoesNotExist:
			user = None
		if user:
			obj = get_object_or_404(Total, day=day)
			data = Serializer(obj).data
			return Response(data)
		else:
			return Response({'error': 'Invalid Token'})


class GetFromDate(APIView):
	def get(self, request, day, token):
		try:
			user = get_object_or_404(User, auth_token=token)
		except Exception as DoesNotExist:
			user = None
		if user:
			q1 = get_object_or_404(Total, day=day).pk
			q = Total.objects.filter(id__gte=q1)
			# obj = get_list_or_404(q)
			data = Serializer(q, many=True).data
			return Response(data)
		else:
			return Response({'error': 'Invalid Token'})

class GetFirstOccurence(APIView):
	'''
	Will return the day of the first occurence of Covid19 in Nigeria
	'''
	def get(self, request, token):
		try:
			user = get_object_or_404(User, auth_token=token)
		except Exception as DoesNotExist:
			user = None
		if user:
			obj = Total.objects.all().filter(confirmed=1)
			data = Serializer(obj[0]).data 
			# print(obj)
			return Response(data)
		else:
			return Response({'error': 'Invalid Token'})

class GetToday(APIView):
	def get(self, request, token):
		try:
			user = get_object_or_404(User, auth_token=token)
		except Exception as DoesNotExist:
			user = None
		if user:
			query = Total.objects.all()
			obj = query[0]
			data = Serializer(obj).data
			return Response(data)
		else:
			return Response({'error': 'Invalid Token'})


class GetYesterday(APIView):
	def get(self, request, token):
		try:
			user = get_object_or_404(User, auth_token=token)
		except Exception as DoesNotExist:
			user = None
		if user:
			query = Total.objects.all().order_by('id')
			obj = query[len(query) - 2]
			data = Serializer(obj).data
			return Response(data)
		else:
			return Response({'error': 'Invalid Token'})

class GetSepDate(APIView):
	def get(self, request, days, token):
		try:
			user = get_object_or_404(User, auth_token=token)
		except Exception as DoesNotExist:
			user = None
		if user:
			d1 = days.split(':')[0]
			d2 = days.split(':')[1]
			d3 = days.split(':')[2]
			print(d1, d2, d3, days)
			obj = Total.objects.filter(day__in=[d1,d2,d3])
			print(obj,)
			data = Serializer(obj, many=True).data
			return Response(data)
		else:
			return Response({'error': 'Invalid Token'})
