from django.db import models
from django.conf import settings
from django.utils import timezone

class Record(models.Model):
	name = models.CharField(max_length=50)
	rollno = models.CharField(max_length=10)
	out_time = models.DateTimeField(default=timezone.now)
	in_time = models.DateTimeField(blank=True, null=True)

	def checkin(self):
		self.in_date = timezone.now()
		self.save()
  
	def __str__(self):
		return self.rollno


# Create your models here.
