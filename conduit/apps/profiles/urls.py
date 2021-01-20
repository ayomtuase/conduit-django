from .views import ProfileRetrieveAPIView
from django.urls import path

app_name = 'profiles'

urlpatterns = [
		path('profiles/<str:username>', ProfileRetrieveAPIView.as_view(), name='profile'),
		
	]