# -*- coding: utf-8 -*-

from django.db import models

class Joke(models.Model):
	joke_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
