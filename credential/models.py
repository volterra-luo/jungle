from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Credential(models.Model):
	user = models.ForeignKey(User)
	course = models.CharField('Course Name', max_length=100, default='Karel the Robot')
	level = models.IntegerField('Skill Level', default=1)
	issue_date = models.DateField('Issue Date')
	certify = models.ImageField()

	def __str__(self):
		return self.user.username + self.course
