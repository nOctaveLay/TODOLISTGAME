from datetime import date
import random
import os
import json

class PickUpTheme:
	def __init__(self):
		self.list_theme = ['dark','water','wind','insect','fruit','light','plant','animal','metal','etc']
		self.theme_pick()
		# self.set_theme()

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

	# temporary method
	def set_theme(self):
		print("press the number if you want")
		num = input("'dark','water','wind','insect','fruit','light','plant','animal','metal','etc' ")
		while num.isdigit() == 0:
			print("again")
			num = input("'dark','water','wind','insect','fruit','light','plant','animal','metal','etc' ")
		self.pick_theme = self.list_theme[int(num)]

class Item(PickUpTheme):
	def __init__(self):
		super().__init__()
		self.list = [] # item's list
		self.user = [] # user's item
		self.item_list(os.getcwd()+"/item/"+self.pick_theme+"_item"+".txt",self.list)
		self.item_list("user.txt",self.user)

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
	#temp
	def add(self):
		name = input("name? ")
		while name == '':
			print("input again")
			name = input("name? ")
		des = input("plz description: ")
		rank = input("rank? ")
		while rank.isdigit() == 0 or int(rank) < 0 or int(rank) > 5:
			print("input again")
			rank = input("rank? ")
		dict_item = {'name':name,'des':des,'rank':rank,'type':self.pick_theme}
		self.list.append(dict_item)

	#temp
	def add_small(self):
		name = input("name? ")
		while name == '':
			print("input again")
			name = input("name? ")
		des = input("plz description: ")
		where = input("Where is it?")
		dict_item = {'name':name,'des':des,'where':where}

	def user_add(self,choice_item):
		name_user = [x["name"] for x in self.user]
		if choice_item["name"] in name_user:
			where = name_user.index(choice_item["name"])
			self.user[where]["num"] += 1
		else:	
			choice_item["num"] = 1
			self.user.append(choice_item)


		#temp
	def revise(self):
		num = input("What would you want to change? ")
		while num.isdigit() == 0 or int(num) < 0 or int(num) > len(self.list):
			print("again")
			num = input("What would you want to change? ")
		change = input("What would you want to change? [name, des, rank] ")
		while change != 'name' and change != 'des' and change != 'rank':
			print("input again")
			change = input("What would you want to change? [name, des, rank] ")
		input_sig = input("write you want to change ")
		while change == "rank" and (input_sig.isdigit() == 0 or int(input_sig) > 5 or int(input_sig) < 1 ):
			print("error")
			input_sig = input("write you want to change ")
		self.list[int(num)][change] = input_sig

	#temp
	def update(self):
		file = open(os.getcwd()+"/item/"+self.pick_theme+"_item"+".txt","w")
		for x in range(len(self.list)):
			json_f = json.dumps(self.list[x])
			self.list[x] = json_f
		string = "\n".join(self.list)
		file.write(string)
		file.close()

	#later it's name update
	def update_user(self):
		file = open("user.txt","w")
		for x in range(len(self.user)):
			json_f = json.dumps(self.user[x])
			self.user[x] = json_f
		string = "\n".join(self.user)
		file.write(string)
		file.close()

	#temp
	def show_item_list(self,what):
		[print(what.index(x),x["name"]) for x in what]

	def show_my_item(self):
		[print(self.user.index(x)+1,x["name"],x["num"]) for x in self.user]

	#temp
	def full_show_item(self):
		for x in self.list:
			print(self.list.index(x),x["name"])
			print(x["des"])
			print(x["rank"])
			print()

	def item_list(self,filename,what):
		if os.path.exists(filename) == 0:
			file = open(filename,"w")
			file.close()
		file = open(filename,"r")
		for line in file:
			line = line.strip("\n")
			line = json.loads(line)
			what.append(line)
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
		return item


