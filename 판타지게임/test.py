from to_do_list import *
from random_item import Item
if __name__ == '__main__':
	do = Do()
	pick = Item()
	count,not_clear_list = do.check_date()
	def print_item():
		if len(pick.user) == 0:print("no item here") 
		else:pick.user_rm()
	[(print("You didn't finish <<"+not_clear_list[x]+">>"),print_item()) for x in range(count)]
	# else:[(print("You didn't finish <<"+not_clear_list[x]+">>")) for x in range(count)]
	
	print()
	print("<<show item list>>")
	pick.show_my_item()
	while True:
		print()
		do.do_list()
		do.update()
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
			do.add_work()
			do.update()
			print("successfully add")
		
		elif int(input_number) == 3:
			do.clear_work()
			print("misson clear!")
			do.update()
			choice_item = pick.item_pick()
			pick.user_add(choice_item)

		else: #int(input_number) == 0
			pick.update_user()
			break
