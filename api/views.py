from django.shortcuts import render
from .models import Heart,Video
from django.http import HttpResponse 
# Create your views here.

def heart(request,video_id,hearted_time): 
	try: 
		video = Video.objects.get(id=video_id)
		Heart.objects.create(video=video,sec=hearted_time)
	except Video.DoesNotExist:
		pass 
	return HttpResponse('OK')
