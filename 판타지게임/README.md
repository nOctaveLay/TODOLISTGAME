
### 1.게임의 목적.
이 게임은 할 일은 많지만 그 일이 정말정말 하기 싫은 사람들을 위해서 만들어진 게임이다.
자신의 할 일을 추가한 뒤 자신의 할 일을 클리어 함으로서 보상을 얻고, 그 보상으로 생산을 하는 게임이며, 레벨도 올릴 수 있고 집도 꾸밀 수 있고 이런 생산 지향형 게임이 목적이다.

### 2. 주의 사항
아직 완성되지 않은 게임이다. GUI도 갖추어져 있지 않으며, 상업적인 이용은 불허한다. 단, 깃허브 full requ.는 언제든지 허용이며, 언제든지 받아들일 준비가 되어있다. 만약 더 좋은 아이디어가 있으면 idea에 써주길 바란다.

### 3. 해야할 일이 많은 사람에게 경배를!!!!

### 4.Full-MVC는 아니지만  MVC 형식으로 만들어져 있다. 아직 덜 완성되었기 때문에 test.py를 임시로 C로 한다.


### 5. item, to do list는 
 
### 6. 구조에 대하여
####	1. test
	test는 아이템을 선출하는 random_item.py파일과 할 일을 입력하고 출력하는 todolist.py파일의 class를 받아 할 일을 추가하고, 할 일이 끝나면 아이템을 획득하게끔 만든다.
	
####	2. random_item
##### PickUpTheme : 
+ theme를 뽑게하는 class이다. self.pick_theme는 오늘 뽑은 theme이고, self.list_theme는 theme의 list가 들어있는 list이다. 원래는 각각을 class로 만드려 했으나, 그러면 너무 복잡해질 것 같아서 단순하게 만들었다.
+ def theme_pick : 테마를 뽑은 것을 어떤 방식으로 저장할까 생각하다가 json file로 저장하면 나중에 dict타입으로 불러오기가 쉽다는 것을 알았다. (method dumps, loads 덕분에) 그래서 json파일로 만들었다. if문은 처음에 저 안에 아무런 문서도 없을 때 readline으로 호출하면 공백이 되고, 그 때 loads를 하면 error가 발생하기 때문에 저런 식으로 만들어줬다. 두번째 if문은 하루에 한 번만 뽑게 하기 위해서 오늘과 날짜가 같으면 못 뽑게끔 만들어줬다. 파이썬은 indent로 구분이 되기 때문에 저 else는 두번째 if에 걸린다. 따라서 처음 만들때를 가정한다. 랜덤함수로 돌리긴 하지만 뽑는 기분을 내기 위해서 input()으로 만들었다. 나머지는 dict타입으로 만들고 json파일로 변형해서 theme.ini에 써서 저장하는 방법일 뿐이다.


##### Item:
+ __init__ : self.list는 테마들에 해당하는 아이템을 import해서 저장할 공간이다. super().__init__()은 앞의 pickuptheme의 __init__을 받게끔했다.
+ random(): rank의 확률은 다음과 같다.  
1 :12%
2 :16%
3 :20%
4 : 24%
5 : 28%
따라서 이를 누적확률로 변환해 random함수를 만들고, 이를 rank로 반환하도록 했다.

+ add: dict타입으로 저장하기 힘들어서 만들어버렸다. 그냥 테스트함수니 최종 때에는 지울 예정.

+ update: add한 내용을 update하는 것이다. 이것도 테스트 함수.

+ item_list: self.list를 초기화 시키는 함수. 각 theme의 파일을 불러다가 아이템을 읽는다.

+ item_pick: random()함수로 rank값 받아서 self.list의 원소의 각 키값이랑 같은지 확인한 후 새로운 리스트 choice_list에 append함. 그리고 random.choice()로 랜덤하게 값을 뽑아줌. 만약 item이 없다면 "no item"을 출력하게 함. 

#### 3. todolist

##### MustList
+ __init__ : 해야될 일이 들어있다. 일단 배타버전이기 때문에 기한같은 것은 무시하고 오늘 할 일을 저장하고 오늘 할 일을 check하는 걸로만 만들었다.
+ return_list : MustList를 dict타입으로 바꿔준다.

##### Do
+__init__ : r_list : 오늘의 해야 할 일. 오늘의 해야할 일은 dolist.txt에 json파일로 저장되어 있기 때문에 그것을 json method loads를 이용해서 dict타입으로 변형시켜준다. 처음 할 때에는 파일 안에 아무것도 없기 때문에 에러가 날 수 있다. 그를 막기 위해 r_string에 아무것도 없을 때에는 r_string을 "{}"로 초기화 시켰다.
+ json으로 저장할 때 숫자키가 문자키로 변해버린다. 이걸 다시 숫자키로 만들어 주기 위해서 밑에 for문을 썼다.
+ list : 출력해 주는 함수이다. 시간을 줄이기 위해서 저런 식으로 만들었다.
+ add : 일을 삽입하는 함수이다. 나중에 GUI로 들어가면 label등으로 조금조금 수정할 예정.
+ clear : 일을 지우는 함수이다. 일이 완벽하게 지워진다. 일단은 이렇게 했지만 나중엔 check가 활성화 되면 clear가 자동으로 실행되게 만들 예정이다.
+ update : 일을 dolist.txt라는 곳에 올린다. 이 때 json으로 바꿔서 올린다.

#### 4. 추가적인 method/구현
+ item_add.py : item을 {}로 넣기 힘들어서 item넣기를 수월하기 위해서 만들었다. 이를 위해서 Item class에 add랑 update가 있다.


