import random
import os
class PickUpTheme:
	def __init__(self):
		self.list_theme = ['star','dark','water','fire','wind','earth','moon','sun','light','tree']
		self.pick_theme = ''

	def theme_pick(self):	
		random.shuffle(self.list_theme)
		self.pick_theme = self.list_theme.pop()
		self.list_theme.append(self.pick_theme)
		print("You pick the theme: ",self.pick_theme)

class Item(PickUpTheme):
	def __init__(self):
		super().__init__()

	def item_pick(self):
		num = self.list_theme.index(self.pick_theme)
		# if num == 0:

		# elif num == 1:

		# elif num == 2:

		# elif num == 3:

		# elif num == 4:

		# elif num == 5:

		# elif num == 6:

		# elif num == 7:

		# elif num == 8:

		# elif num == 9:

		# elif num == 10:
# read_file = open("item_list.txt","r")
# have_theme_list = read_file.readline()
# if have_theme_list != '':
# 	have_theme_list = have_theme_list.split("/")
# else:
# 	have_theme_list = []
# write_file = open("item_list.txt","w")
# if have_theme_list == []:
# 	print("Welcome to the memory world.")
# 	print("you grow up the flower - to protect the world.")
# 	print("if you do the work, you can get the item.")
# 	print("I recommend you don't handle the game, if you can do this.")
# have_theme_list.append(pick_theme)
# print("You have this item: ",end = '')
# [print(x,end = ' ') for x in have_theme_list]
# print()
# have_theme = "/".join(have_theme_list)
# write_file.write(have_theme)
# write_file.close()
# read_file.close()