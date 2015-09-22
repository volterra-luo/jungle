# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
	user = models.OneToOneField(User)
	is_verified = models.BooleanField(default=False)
	is_admitted = models.BooleanField(default=False)
	role = models.CharField(default='P', max_length=1)

	def __unicode__(self):
		return self.user.username