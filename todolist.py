# from datetime import datetime
# BETA


class List_Do:
	def __init__(self):
		r_file = open("dolist.txt","r")
		self.r_list = r_file.readlines()
		r_file.close()

	def add(self):
		work = input("write the work: ")
		self.r_list.append(work+"\n")

	def clear(self):
		[print(x,self.r_list[x],end = '') for x in range(len(self.r_list))]
		print("check the work")
		input_number = input("choose the number: ")
		while input_number.isdigit() == False or int(input_number) > (len(self.r_list)-1) or int(input_number) < 0:
			print("input again")
			input_number = input("choose the number: ")
		self.r_list.remove(self.r_list[int(input_number)])
		print("clearly removed")

	def update(self):
		w_file = open("dolist.txt","w")
		string = "".join(self.r_list)
		w_file.write(string)
		w_file.close() 


# while True:
# 	add(r_list)
# 	break_point = input("stop?")
# 	if break_point == 'o':
# 		print(r_list)
# 		break
# class Do:
# 	def __init__(self):
# 		self.date =
# 		self.work = 
