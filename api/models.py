from django.db import models
from django.utils import timezone


class Video(models.Model):
    title = models.CharField(max_length=200)
    
    def heart(self):
        self.save()

    def __str__(self):
        return self.title

class Heart(models.Model): 
	sec = models.IntegerField()
	count = models.IntegerField()

	def __str__(self): 
		return "(" + self.sec + "," + self.count + ")"
