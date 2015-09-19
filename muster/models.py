from django.db import models

from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User)
    school = models.CharField(max_length=100)

class Parent(models.Model):
    user = models.OneToOneField(User)
    kid = models.CharField(max_length=100)
