import json
class Star:
	def __init__(self):
		self.name = "star"
		self.desp = "별은 사람이 볼 수 없을 정도로 아주 먼 곳에 있어 모두들 사용할 수 없을 것이라고 보았다. 하지만 미칠듯하게 천재인 자가 나타나 이 별을 발전시키는 방법을 알려주었다. 그리하여 별의 개발이 시작되었다."
		self.list = []
		file = open("itemtest.txt","r")
		for line in file:
			line = line.strip("\n")
			line = json.loads(line)
			self.list.append(line)
		file.close()
	
	def add(self):
		name = input("name? ")
		des = input("plz description")
		rank = input("rank? ")
		dict_item = {'name':name,'des':des,'rank':rank}
		self.list.append(dict_item)

	def update(self):
		file = open("star_item.txt","w")
		for x in range(len(self.list)):
			json_f = json.dumps(self.list[x])
			self.list[x] = json_f
		string = "\n".join(self.list)
		file.write(string)
		file.close()