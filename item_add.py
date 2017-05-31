from random_item import *
item = Item()
item.show_item_list()
while True:
	a = input("0")
	if a == "0":
		item.update()
		break
	item.add()