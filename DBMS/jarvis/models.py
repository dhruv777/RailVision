from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Login(models.Model):
	username = models.CharField(max_length = 50)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	password = models.CharField(max_length = 90)

	def __unicode__(self):
		return self.username