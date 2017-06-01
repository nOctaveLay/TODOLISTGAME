from datetime import date
import json
# BETA
class MustList:
	def __init__(self,name):
		self.name = name
		self.date = date.today().isoformat()
		self.check = None

	def return_list(self):
		return {'date':self.date,'check':self.check,'name':self.name}

class Do(MustList):
	def __init__(self):
		r_file = open("dolist.txt","r")
		r_string = r_file.readline()
		r_file.close()
		if r_string == "":
			r_string = "{}"
		self.r_list = json.loads(r_string)
		self.key = self.r_list.keys()
		for x in range(len(self.key)):
			self.r_list[x+1] = self.r_list[str(x+1)]
			del self.r_list[str(x+1)]

	def list(self):
		[print(x+1,":",self.r_list[x+1]['name']) for x in range(len(self.r_list))]

	def add(self):
		work = input("write the work: ")
		while work.replace(" ","") == "":
			print("no works on here")
			work = input("write the work: ")
		dolist = MustList(work)
		self.r_list[len(self.key)+1] = dolist.return_list()

	def clear(self):
		self.list()
		if self.r_list == []:
			print("no list")
			return
		else:
			print("check the work")
			print("if you exit the clear, press 0")
			input_number = input("choose the number: ")
			while input_number.isdigit() == False or int(input_number) > len(self.r_list) or int(input_number) < 0:
				print("input again")
				input_number = input("choose the number: ")
			
			if int(input_number) == 0:
				print("ending the clearing")
				return

			else:
				i = 0
				last = len(self.r_list)
				print(self.r_list)
				del self.r_list[int(input_number)]
				while int(input_number) != last and i+int(input_number) < last:
					print(self.r_list.keys())
					self.r_list[int(input_number)+i] = self.r_list[int(input_number)+1+i]
					if int(input_number)+1+i == last:
						del self.r_list[last]
					i += 1
				print("clearly removed")

	def update(self):
		w_file = open("dolist.txt","w")
		string = json.dumps(self.r_list)
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
