from random_item import *
item = Item()
while True:
	item.show_item_list(item.list)
	a = input("0 ")
	if a == "0":
		item.update()
		break
	item.add()