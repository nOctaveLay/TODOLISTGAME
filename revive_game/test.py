from to_do_list import *
from character import *
if __name__ == '__main__':
	do = Do()
	character = Character()
	count,not_clear_list = do.check_date()
	[(print("You didn't finish <<"+not_clear_list[x]+">>")) for x in range(count)]
	print("Your ")
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

		elif int(input_number) == 2:
			do.add_work()
			do.update()
			print("successfully add")
		
		elif int(input_number) == 3:
			do.clear_work()
			print("misson clear!")
			do.update()

		else: #int(input_number) == 0
			break
