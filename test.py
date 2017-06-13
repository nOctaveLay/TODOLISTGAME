from todolist import *
from random_item import Item
if __name__ == '__main__':
	a = Do()
	pick = Item()
	count,not_clear_list = a.check_date()
	[(print("You didn't finish <<"+not_clear_list[x]+">>"),pick.user_rm()) for x in range(count)]
	pick.show_my_item()
	while True:
		print()
		a.list()
		a.update()
		print()
		print("0 : end")
		print("1 : list my item")
		print("2 : add the work")
		print("3 : success the work")
		print()
		input_number = input("choose the number: ")
		if input_number.isdigit() == False or int(input_number) < 0 or int(input_number) > 3:
			print("input again")

		elif int(input_number) == 1:
			pick.show_my_item()

		elif int(input_number) == 2:
			a.add()
			a.update()
			print("successfully add")
		
		elif int(input_number) == 3:
			a.clear_work()
			print("misson clear!")
			a.update()
			choice_item = pick.item_pick()
			pick.user_add(choice_item)

		else: #int(input_number) == 0
			pick.update_user()
			break
