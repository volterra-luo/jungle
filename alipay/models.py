# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.utils import timezone


def _trade_no_gen():
	pass


class Product(models.Model):
	
	user_name = models.CharField(
		'Username', 
		max_length=20, 
		unique=True, 
	)

	out_trade_no = models.CharField(
		max_length = 64, 
		help_text = 'An unique numbered transaction ID in merchant system', 
		default = _trade_no_gen(), 
	)

	trade_no = models.CharField(
		max_length=28, 
		help_text='The transaction ID in alipay system',
		default='0', 
	)

	course_id = models.IntegerField()

	subject = models.CharField(
		max_length=200,
		help_text='A short description for the product.', 
	)

	total_fee = models.DecimalField(
		max_digits=6, 
		decimal_places=2
	)

	created_date = models.DateTimeField(auto_now_add=True)
	payment_date = models.DateTimeField(auto_now=True)

	# not pay - 0
	# pay success - 1
	payment_status = models.IntegerField(default=0)

	
	class Meta:
		ordering = ['payment_date', 'trade_no']

	
	def save(self, *args, **kwargs):
		if self.user_name in ['admin', 'test']:
			return
		else:
			super(Product, self).save(*args, **kwargs)


	def __unicode__(self):
		return self.user_name + ' | ' + self.out_trade_no