from django.urls import path
from .views import RegistrationAPIView, LoginAPIView

app_name = 'authentication'
urlpatterns = [
		path('users/', RegistrationAPIView.as_view(), name='authentication'),
		path('users/login/', LoginAPIView.as_view())	
	]