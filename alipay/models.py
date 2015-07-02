# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.utils import timezone

class Product(models.Model):
	user_name = models.CharField(max_length=50)
	out_trade_no = models.CharField(max_length=50)
	trade_no = models.CharField(max_length=50)
	subject = models.CharField(max_length=200)
	total_fee = models.DecimalField(max_digits=6, decimal_places=2)
	created_date = models.DateTimeField(auto_now_add=True)
	payment_date = models.DateTimeField(auto_now=True)
	payment_status = models.IntegerField()

	class Meta:
        ordering = ['payment_date', 'trade_no']

	def __unicode__(self):
		return self.user_name + ' | ' + self.out_trade_no