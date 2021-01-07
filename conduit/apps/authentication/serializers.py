from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.ModelSerializer):

	password = serializers.CharField(min_length=8, max_length=128, write_only=True)
	token = serializers.CharField(read_only=True)

	class Meta:
		model = User
		fields = ['email', 'username', 'password', 'token']

	def create(self, validated_data):
		return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
	email = serializers.CharField(max_length=255)
	username = serializers.CharField(max_length=255, read_only=True)
	password = serializers.CharField(max_length=255, write_only=True)
	token = serializers.CharField(max_length=255, read_only=True)

	def validate(self, data):

		email = data.get('email', None)
		password = data.get('password', None)

		if email is None:
			raise serializers.ValidationError('An email address is required to log in')

		if password is None:
			raise serializers.ValidationError('A password is required to log in')

		user = authenticate(username=email, password=password)

		if user is None:
			raise serializers.ValidationError('Invalid email address or password')

		if not user.is_active:
			raise serializers.ValidationError('This user has been deactivated')

		return {
			'email' : user.email,
			'username' : user.username,
			'token' : user.token
			}
