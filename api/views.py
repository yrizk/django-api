from django.shortcuts import render
from .models import Heart,Video
from django.http import HttpResponse 
from django.db.models import Count,Sum
import json 
import logging
# Create your views here.

def heart(request,video_id,hearted_time): 
	try: 
		video = Video.objects.get(id=video_id)
		Heart.objects.create(video=video,sec=hearted_time)
	except Video.DoesNotExist:
		pass 
	return HttpResponse('OK')

def getHearts(request,video_id): 
	hearts = Heart.objects.filter(video=video_id).values('sec').annotate(likes=Count('sec')) # get all the hearts that are assocated with that video 
	if not hearts : logging.warning('hearts is none')
	else : logging.warning(hearts)
	# aggregate the 
	
	response_data = [{
		"sec: " : h.get('sec'),
		"num_hearts" : h.get('likes')
	} for h in hearts]

	response = { 
		"video_id" : str(video_id),
		"num_count" : response_data
	}

	return HttpResponse(json.dumps(response), content_type="application/json")
	#return HttpResponse("hi there, we <3 python")


