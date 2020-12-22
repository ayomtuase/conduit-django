from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializers):

	password = models.CharField(min_length=8, max_length=128, write_only=True)
	token = models.CharField(read_only=True)

	class Meta:
		model = User
		fields = ['email', 'username', 'password', 'token']

	def create(self, validated_data):
		return User.objects.create_user(**validated_data)
