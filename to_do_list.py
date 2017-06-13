from datetime import date , datetime,timedelta
import calendar
import json
import os 
#BETA
class MustList:
	def __init__(self,name,finish_date,rotate = date.today().isoformat(),start_date = date.today().isoformat()):
		self.name = name
		self.start_date = date.today().isoformat()
		self.finish_date = finish_date.isoformat()
		self.rotate_date = rotate

	def return_list(self):
		return {'start_date':self.start_date,'finish_date':self.finish_date,'rotate':self.rotate_date,'name':self.name}

class Do(MustList):
	def __init__(self):
		self.path = os.getcwd()+"/data/"
		path_do_list = self.path+"do_list.txt"
		if os.path.exists(path_do_list) == 0:
			open(path_do_list,"w").close()
		r_file = open(path_do_list,"r")
		r_string = r_file.readline()
		r_file.close()
		if r_string == "":
			r_string = "{}"
		self.r_list = json.loads(r_string)
		self.key = self.r_list.keys()
		for x in range(len(self.key)):
			self.r_list[x+1] = self.r_list[str(x+1)]
			del self.r_list[str(x+1)]

	def do_list(self):
		if len(self.r_list) == 0 : print("<<Today's to do list is empty.>>")
		for x in range(len(self.r_list)):
			if self.r_list[x+1]['start_date'] == date.today().isoformat():
				print(x+1,":",self.r_list[x+1]['name'],"finish_date:",self.r_list[x+1]['finish_date'])

# if duration is ended, the work must be removed with demerit.
	def check_date(self):
		len_list = len(self.r_list)
		count,i = 0,1
		not_clear_list = []
		for _ in range(len_list):
			if self.r_list[i]["finish_date"] < (date.today()).isoformat():
				if self.r_list[i]["rotate"] >= date.today().isoformat():
					self.add(self.r_list[i])
				not_clear_list.append(self.r_list[i]["name"])
				self.clear(self.path+"not_do_work.txt",1,False)
				count += 1
			else: i += 1
		return (count,not_clear_list)
#rotate add
	def add(self,work):
		y,m,d = work['start_date']
		dolist = MustList(work['name'],date.today(),rotate = work['rotate'],today_date = date(int(y),int(m),int(d))+timedelta(days = 1))

#work add
	def add_work(self):
		def set_finish_date(work):
			finish_y = input("input finish year(if you press enter, the year == current year) ")
			if finish_y == '' :finish_y = date.today().year
			if len(str(finish_y)) == 2 : finish_y = "20"+finish_y 
			while str(finish_y).isdigit() == 0 or len(str(finish_y)) != 4 or int(finish_y) < 2016:
				print("input again")
				finish_y = input("input finish year(if you press enter, the year == current year) ")
			finish_m = input("input finish month(if you press enter, the year == current month) ")
			if finish_m == '' :finish_m = date.	today().month
			while str(finish_m).isdigit() == 0 or int(finish_m) > 12 or int(finish_m) < 1:
				print("input again")
				finish_m = input("input finish month(if you press enter, the year == current month) ")
			finish_d = input("input finish day(if you press enter, the day == current day) ")
			if finish_d == '' :finish_d = date.today().day
			day_cal = list(calendar.Calendar().itermonthdays(finish_y,finish_m))
			while 0 in day_cal:
				day_cal.remove(0)
			while str(finish_d).isdigit() == 0 or int(finish_d) < 1 or int(finish_d) > day_cal[-1]:
				finish_d = input("input finish day(if you press enter, the day == current day) ")
			return (work,date(int(finish_y),int(finish_m),int(finish_d)))
		work = input("write the work: ")
		while work.replace(" ","") == "":
			print("no works on here")
			work = input("write the work: ")
		duration = input("duration?(0) or input y/m/d?(1) or today?(2) or daily?(3) ")
		while duration.isdigit() == 0 or int(duration) > 3 or int(duration) < 0:
			print("press input again. ")
			duration = input("duration?(0) or input y/m/d?(1) or today?(2) or daily?(3) ")
		duration = int(duration)
		
		if duration == 0:
			time_delta = input("duration? ")
			while time_delta.isdigit() == 0 or int(time_delta) < 1:
				print("input again.")
				time_delta = input("duration? ")
			time_delta = int(time_delta) 
			dolist = MustList(work,date.today() + timedelta(days = time_delta))

		elif duration == 1:
			work,d = set_finish_date(work)
			dolist = MustList(work,d)
			# dolist.print_list()
		
		elif duration == 2:
			dolist = MustList(work,date.today())

		elif duration == 3:
			work,d = set_finish_date(work)
			dolist = MustList(work,date.today(),d.isoformat())

		self.r_list[len(self.key)+1] = dolist.return_list()

#clear the file & all
	def clear(self,file,input_number,finish):
		i = 0
		file = open(file,"a")
		if finish:
			file.write(datetime.today().replace(microsecond = 0).isoformat().replace("T"," ")+" finish ")
		else:
			file.write(self.r_list[int(input_number)]["start_date"]+" not finish ")
		file.write(self.r_list[int(input_number)]["name"]+"\n")
		file.close()
		last = len(self.r_list)
		del self.r_list[int(input_number)]
		while int(input_number) != last and i+int(input_number) < last:
			self.r_list[int(input_number)+i] = self.r_list[int(input_number)+1+i]
			if int(input_number)+1+i == last:
				del self.r_list[last]
			i += 1

# You finish the work
	def clear_work(self):
		self.do_list()
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
				self.clear(self.path+"did_do_list.txt",input_number,True)


	def update(self):
		w_file = open(self.path+"do_list.txt","w")
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
# 		self.start_date =
# 		self.work = 
