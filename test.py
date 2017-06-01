from todolist import *
from random_item import Item
if __name__ == '__main__':
	a = Do()
	pick = Item()
	while True:
		print()
		a.list()
		print()
		print("0 : end")
		print("1 : add the work")
		print("2 : clear the work")
		print()
		input_number = input("choose the number: ")
		if input_number.isdigit() == False or int(input_number) < 0 or int(input_number) > 3:
			print("input again")

		elif int(input_number) == 1:
			a.add()
			a.update()
			print("successfully add")
		
		elif int(input_number) == 2:
			a.clear()
			a.update()
			choice_item = pick.item_pick()
			# for x in range()
			pick.user_add(choice_item)
		else: #int(input_number) == 0
			pick.update_user()
			break
