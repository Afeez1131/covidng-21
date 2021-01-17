from django.db import models
from datetime import datetime

# Create your models here.


class Total(models.Model):
	day = models.DateField(max_length=200)
	# day = models.CharField()
	confirmed = models.CharField(max_length=200)
	discharged = models.CharField(max_length=200)
	death = models.CharField(max_length=200)

	class Meta:
	    ordering = ('-id', )

	def __str__(self):
		return str(self.day)

class Count(models.Model):
	count = models.IntegerField(default=0)

	def __str__(self):
		return str(self.count)