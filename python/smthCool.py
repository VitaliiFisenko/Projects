import random as rand
import time as ti
s = ''
simbwols = list('$S▓╣&█╗╜')
while True:
	s = ''
	for i in range(80):
		s+=simbwols[rand.randint(0,7)]
	print(s)
	ti.sleep(0.08)