from django.contrib.auth.models import User
from rest_framework import serializers
from muster.models import Person


class UserSerializer(serializers.ModelSerializer):
	person = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'person')


class PersonSerializer(serializers.HyperlinkedModelSerializer):

	user = serializers.ReadOnlyField(source='user.username')

	class Meta:
		model = Person
		fields = ('is_verified', 'is_admitted', 'user')