from django.urls import path, include
from . import views#, StateDeleteView
from rest_framework import routers


urlpatterns = [
	# path('', views.home, name='home'),
	path('', views.endpoints.as_view(), name='endpoint'),
	path('all/<token>/', views.TotalListView.as_view(), name='total'),
	#api/v2/all/1233444234243
		#all datas from the beginning of corona
	path('login/username=<username>&password=<password>/', views.LoginView.as_view(), name='login_api'),
	#api/v2/login/username=aname&password=password
	# path('create/', views.UserCreate.as_view(), name='create'),

	#api/v2/register
	path('dayone/<token>/', views.GetFirstOccurence.as_view(), name='dayone'),
	#api/v2/dayone/1233444234243
	#get the first day of occurence

	path('today/<token>/', views.GetToday.as_view(), name='today'),
	#api/v2/today/1233444234243

	path('dates/<days>/<token>/', views.GetSepDate.as_view(), name='sep-day'),
	#api/v2/dates/2020-10-1:2020-10-15:2020-11-30/1233444234243
	#get the data for today

	path('from/<day>/<token>/', views.GetFromDate.as_view(), name='from'), 
	#api/v2/from/2020-10-20/1233444234243

	path('yesterday/<token>/', views.GetYesterday.as_view(), name='yesterday'),
	#api/v2/yesterday/1233444234243

	path('date/<day>/<token>/', views.GetDateView.as_view(), name='get-by-date'),
	#api/v2/date/2020-10-1/1233444234243
	#get data for this date alone




	# path('2/<int:pk>', views.TotalView.as_view(), name='two'),

	# path('after/<date>', views.GetDateView.as_view(), name='date')
]