import sys
from time import sleep
words = "I'm your guide,"
a_found,index = 0,0
for char in words:
	if char == '\'':
		if a_found != 1 and words[index-1].isalpha() == 0:
			sleep(0.5)
			a_found += 1
		else : a_found = 0
	sleep(0.05)
	sys.stdout.write(char)
	sys.stdout.flush()
	if char == ',':
		sleep(1)
	index += 1
input()