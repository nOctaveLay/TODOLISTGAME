import sys
from time import sleep
class Character:
	def __init__(self,name):
		self.name = name
		self.will = 0

class Guide:
	def __init__(self,name):
		self.name = self.set_name(name)

	def set_name(self,name):
		if name.islower():
			return "Aileen"
		elif name.isupper():
			return "Calix"
		else:
			return "Elroy"

	def init_message(self):
		typing_message("Hello?")
		typing_message("Welcome to the 'EMPTY SPACE.'")
		typing_message("Nothing.... is.... here, except you and me.")
		typing_message("Ah, Did you say who I am?")
		typing_message("well, you forgot about me! ")
		typing_message("I'm your guide,"+self.name)
		typing_message("I came here, to ENCOURAGE you.")
		typing_message(".....Sadly, I can't help you directly...")
		typing_message("but I know how to get out this place.")
		typing_message("Can you see the hole in your head?")
		typing_message("that is called 'MERCY'")
		typing_message("if you build the box, it can help you be able to leave this EMPTY SPACE.")
		typing_message("that's easy, calm down.")
		typing_message("you can make the box. by the power of will.")
		typing_message("you can fill the power by doing work.")
		typing_message("if you do this, you can get the power of 1 point.")
		typing_message("if you fill the 300 point, you can make the box.")
		typing_message("are you ready to start?")

	def typing_message(self,message):
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
