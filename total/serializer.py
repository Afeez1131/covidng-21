from rest_framework import serializers
from .models import Total
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# class UserSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ('username', 'email', 'password')
# 		extra_kwargs = {'password': {'write_only': True}}

# 	def create(self, validated_data):
# 		user = User(
# 			email=validated_data['email'], 
# 			username=validated_data['username'])
# 		user.set_password(validated_data['password'])
# 		user.save()
# 		Token.objects.create(user=user)
# 		return user

class TotalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Total
		fields = ('day', 'confirmed', 'death', 'discharged')
		# extra_kwargs = {'url': {'lookup_field': 'day'}}

class Serializer(serializers.ModelSerializer):
	class Meta:
		model = Total
		fields = ('day', 'confirmed', 'death', 'discharged')

class TotalViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Total 
		fields = ('__all__')

