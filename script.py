#!/usr/bin/python
import sys
import random
import urllib.request

if len(sys.argv) < 2: 
	print('Usage: python script.py <count>')
	quit()

count = sys.argv[1];
print('Making ' + count + ' heart requests')

for i in range(0,int(count)):
	rand_sec = str(random.randint(1,180)) # 3 minute videos
	rand_video_id = str(random.randint(1,3)) # just 3 videos 
	print('rand_sec: ' + rand_sec + ' rand_video_id: ' + rand_video_id)
	html = urllib.request.urlopen('http://yorizk.pythonanywhere.com/api/heart/' + rand_video_id + '/' + rand_sec).read()
	if i == 0: print('html: ' + str(html))





