# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

T = [2**(17-i) for i in range(17)]
T2 = [str((12-i)%11) for i in range(11)]
T2[2] = 'X'

def id_check(id):
	if len(id) != 18:
		return False

	id = list(id)
	t1 = id.pop()
	id = map(int, id)

	s = sum([id[i]*T[i] for i in range(17)])
	t2 = T2[s % 11]
	if t2 == t1:
		return True

	return False


class Person(models.Model):
	user = models.OneToOneField(User, related_name='person')
	id_cn = models.CharField()
	cellphone = models.CharField()
	is_verified = models.BooleanField(default=False)
	is_admitted = models.BooleanField(default=False)
	role = models.CharField(default='P', max_length=1)

	def _mailbox(self):
		return 'http://mail.' + self.user.email.split('@')[1]

	mailbox = property(_mailbox)

	def __unicode__(self):
		return self.user.username