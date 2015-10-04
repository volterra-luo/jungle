from django.contrib.auth.models import User
from rest_framework import serializers
from muster.models import Person


class UserSerializer(serializers.HyperlinkedModelSerializer):
	person = serializers.PrimaryKeyRelatedField(read_only=True)
	is_admitted = serializers.ReadOnlyField(source='person.is_admitted')
	is_verified = serializers.ReadOnlyField(source='person.is_verified')


	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'person', 'is_admitted', 'is_verified')


class PersonSerializer(serializers.HyperlinkedModelSerializer):

	user = serializers.ReadOnlyField(source='user.username')

	class Meta:
		model = Person
		fields = ('is_verified', 'is_admitted', 'user')