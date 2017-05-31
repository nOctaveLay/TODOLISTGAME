from datetime import date
import random
import os
import json

class PickUpTheme:
	def __init__(self):
		self.list_theme = ['dark','water','fire','wind','earth','moon','sun','light','tree']
		self.theme_pick()

	def theme_pick(self):
		json_file = open("theme.ini","r")
		json_string = json_file.readline()
		json_file.close()
		if json_string == '':
			json_string = '{}'
		json_dict = json.loads(json_string)
		if 'date' in json_dict and date.today().isoformat() == json_dict["date"]:
			self.pick_theme = json_dict["theme"]

		else:
			theme_file = open("theme.ini","w")
			input("press any key. if you do, you can pick up the TODAY's theme.")
			self.pick_theme = random.choice(self.list_theme)
			dict_ = {"date":date.today().isoformat(),"theme":self.pick_theme}
			dict_string = json.dumps(dict_)
			theme_file.write(dict_string)
			theme_file.close()
			print("select!")
		print("Your TODAY's theme: ",self.pick_theme)


class Item(PickUpTheme):
	def __init__(self):
		super().__init__()
		self.list = []
		self.item_list()
		

	def random(self):
		ran_number = round(random.random(),2) * 100
		if ran_number < 12:
			return "1"
		elif ran_number < 28:
			return "2"
		elif ran_number < 48:
			return "3"
		elif ran_number < 72:
			return "4"
		elif ran_number <= 100:
			return "5"
	
	def add(self):
		name = input("name? ")
		while name == '':
			print("input again")
			name = input("name? ")
		des = input("plz description: ")
		rank = input("rank? ")
		while rank.isdigit() == 0 or int(rank) <0 or int(rank)>5:
			print("input again")
			rank = input("rank? ")
		dict_item = {'name':name,'des':des,'rank':rank}
		self.list.append(dict_item)

	def update(self):
		file = open(self.pick_theme+"_item"+".txt","w")
		for x in range(len(self.list)):
			json_f = json.dumps(self.list[x])
			self.list[x] = json_f
		string = "\n".join(self.list)
		file.write(string)
		file.close()

	# def item_list(self):
	# 	[print(x) for x in self.list]

	def item_list(self):
		file = open(self.pick_theme+"_item"+".txt","r")
		for line in file:
			line = line.strip("\n")
			line = json.loads(line)
			self.list.append(line)
		file.close()

	def item_pick(self):
		rand = self.random()
		choice_list = []
		for x in range(len(self.list)):
			if self.list[x]["rank"] == rand:
				choice_list.append(self.list[x])
		item = random.choice(choice_list)
		if item == "": print("no item")
		else :print("you select",item["name"])



