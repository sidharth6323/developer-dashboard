from __future__ import unicode_literals

from django.db import models

# Create your models here.
class registration(models.Model):
	f_name=models.CharField(max_length=50)
	l_name=models.CharField(max_length=50)
	gender=models.CharField(max_length=50)
	github=models.CharField(max_length=50)
	course=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	usn=models.CharField(max_length=50)
	mobile=models.CharField(max_length=50)
	year=models.CharField(max_length=50)
	branch=models.CharField(max_length=50)

	def __str__(self):
		return self.f_name+" "+self.l_name