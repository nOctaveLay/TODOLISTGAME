from todolist import *
from random_item import Item
if __name__ == '__main__':
	a = List_Do()
	pick = Item()
	pick.theme_pick()
	while True:
		print("0 : end")
		print("1 : add the work")
		print("2 : clear the work")
		input_number = input("choose the number: ")
		if input_number.isdigit() == False or int(input_number) > 3 or int(input_number) < 0:
			print("input again")
		elif int(input_number) == 1:
			a.add()
			print(a.r_list)
		elif int(input_number) == 2:
			a.clear()
		else:
			a.update()
			break
