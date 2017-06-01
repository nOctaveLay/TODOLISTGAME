from random_item import *
item = Item()
# for x in range(len(item.list)):
# 	item.list[x]["type"] = item.pick_theme
# item.update()
while True:
	print(item.list)
	item.full_show_item()
	a = input("0 ")
	if a == "0":
		item.update()
		break
	item.revise()
	print(item.list)