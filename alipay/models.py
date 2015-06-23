import datetime

from django.db import models
from django.utils import timezone

class Product(models.Model):
	user_name = ''
	out_trade_no = ''
	subject = ''
	total_fee = 0.01
	created_date = ''
	payment_date = ''
	payment_status = ''

	def __unicode__(self):
		return self.user_name + ' | ' + self.out_trade_no