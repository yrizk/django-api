from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class Heart(models.Model): 
	sec = models.IntegerField()
	video = models.ForeignKey('Video')

	def __str__(self): 
		return "{},{}".format(self.sec,self.video)


