import uuid
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=100)
	content = models.TextField()
	datetime = models.DateTimeField(default=timezone.now())
	author = models.ForeignKey(User)
