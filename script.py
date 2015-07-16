#!/usr/bin/python
import sys
import random

if len(sys.argv) < 2: 
	print 'Usage: python script.py <count>'
	quit()

count = sys.argv[1];
print 'Making ' + count + ' heart requests'

for i in range(0,int(count)):
	rand_sec = random.randint(1,180) # 3 minute videos
	rand_video_id = random.randint(1,3) # just 3 videos 
	print 'rand_sec: ' + str(rand_sec) + ' rand_video_id: ' + str(rand_video_id)




