from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer
from .renderers import UserJSONRenderer

class RegistrationAPIView(APIView):
	permission_classes = (AllowAny,)
	renderer_classes = (UserJSONRenderer,)
	serializer_class = RegistrationSerializer

	def post(self, request):
		user = request.data.get('user', {})		
		serializer = self.serializer_class(data=user)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
	permission_classes = (AllowAny,)
	renderer_classes = (UserJSONRenderer,)
	serializer_class = LoginSerializer

	def post(self, request):
		user = request.data.get('user', {})		
		serializer = self.serializer_class(data=user)
		serializer.is_valid(raise_exception=True)		

		return Response(serializer.data, status=status.HTTP_200_OK)

class UserRetrieveUpdateAPIView(APIView):
	permission_classes = (IsAuthenticated,)
	renderer_classes = (UserJSONRenderer,)
	serializer_class = UserSerializer

	def get(self, request):
		serializer = self.serializer_class(request.user)

		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, *args, **kwargs):
		user_data = request.data.get('user', {})
		serializer_data = {			
			"username" : user_data.get('username', request.user.username),
			"email" : user_data.get('email', request.user.email),
			"password" : user_data.get('password', request.user.password),

			"profile" : {
				"bio" : user_data.get('bio', request.user.profile.bio),
				"image" : user_data.get('image', request.user.profile.image),
			}


		}
		serializer = self.serializer_class(request.user, data=serializer_data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data, status=status.HTTP_200_OK)





