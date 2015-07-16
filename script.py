#!/usr/bin/python
import sys

if len(sys.argv) < 2: 
	print 'Usage: python script.py <count>'
	quit()

count = sys.argv[1];
print 'count : ' + str(count)
