from django.urls import path

from .views import RegistrationAPIView

app_name = 'authentication'
url_patterns = [
		path('users', RegistrationAPIView.as_view(), name='authentication'),	
	]