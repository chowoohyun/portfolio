# #스타 3종족 서로 전쟁 하는 게임 테란을 예로 든다
# #마린 : 공격 유닛 군인, 총을 쏜다

# name = "마린" #이름
# hp = 40 # 유닛의 체력
# damage = 5  #유닛의 공격력

# print("{0} 유닛이 생성 되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# #탱크 유닛
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성 되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank_name2 = "탱크"
# tank_hp2 = 150
# tank_damage2 = 35
# print("{0} 유닛이 생성 되었습니다.".format(tank_name2))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp2, tank_damage2))

# def attack (name, location, damage):
#     print("{0}:{1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location,damage))

# attack(name,"1시",damage)
# attack

### 유닛이 여러개 이기 때문에 클래스로 만든다



# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))


#m1 = Unit("마린",40, 5)

####init 생성자 클래스로 부터 만들어지는게 객체, 마린과 탱크는 유닛 클래스의 인스턴스
####self를 제외하곤 동일한 값을 넣어야 한다. 부족하거나 과하게 넣으면 안된다
######init 함수에 정의된 갯수 만큼 정해야 한다

#레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
# #.으로 멤버변수에 접근 가능


# #마인드 컨트롤 : 상대방 유닛을 내것으로
# w2 = Unit("레이스", 80, 5)
# w2.clocking = True
# #클래스 외부에서도 확장 가능
# if w2.clocking == True:
#     print("{0}는 현재 클로킹 상태".format(w2.name))



#####메소드

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
       
# #공격 유닛
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
    
#     def attack (self, location):
#         print("{0} :{1} 방향으로 적군을 공격 합니다. [공격력{2}]"
#         .format(self.name, location, self.damage))
    
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴되었습니다.".format(self.name))


# #공격 유닛,

# f1 = AttackUnit("f",50, 16)
# f1.attack("5시")

# f1.damaged(25)
# f1.damaged(25)






#########상속

# 유닛중 공격력이 없는 유닛도 있다.

#일반유닛
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# ## 두개의 유닛에서 이름이나 HP는 같이 사용가능
# ### 공격 유닛

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack (self, location):
#         print("{0} :{1} 방향으로 적군을 공격 합니다. [공격력{2}]"
#         .format(self.name, location, self.damage))
    
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴되었습니다.".format(self.name))


# #공격 유닛,

# f1 = AttackUnit("f",50, 16)
# f1.attack("5시")

# f1.damaged(25)
# f1.damaged(25)



# #################### 다중 상속

# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# ## 두개의 유닛에서 이름이나 HP는 같이 사용가능
# ### 공격 유닛

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack (self, location):
#         print("{0} :{1} 방향으로 적군을 공격 합니다. [공격력{2}]"
#         .format(self.name, location, self.damage))
    
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴되었습니다.".format(self.name))


# # 드랍쉽, 공중  수송기, 공격은 불가

# #공중유닛 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):

#         print("{0} :{1} 방향으로 날아갑니다. [속도{2}]"
#         .format(name, location, self.flying_speed))


# class FlayableAttack(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

    
############연산자 오버로딩
##자식 클래스에서 하는것


# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
        

# ## 두개의 유닛에서 이름이나 HP는 같이 사용가능
# ### 공격 유닛

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack (self, location):
#         print("{0} :{1} 방향으로 적군을 공격 합니다. [공격력{2}]"
#         .format(self.name, location, self.damage))
    
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{0} : 파괴되었습니다.".format(self.name))


# # 드랍쉽, 공중  수송기, 공격은 불가

# #공중유닛 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):

#         print("{0} :{1} 방향으로 날아갑니다. [속도{2}]"
#         .format(name, location, self.flying_speed))


# class FlayableAttack(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)


# # 건물

# class BUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self, name, hp)
#         super().__init__(name, hp)### super는 self를 받지 않음






#pass # pass는 그냥 넘어가는것


# class Unit :
#     def __init__(self):
#         print("Unit 생성자")

# class Fly:
#     def __init__(self):
#         print("Fly 생성자")

# class FlyUnit(Fly, Unit):
#     def __init__(self):
#         #super().__init__()# 다중 상속 받으면 처음 받은것만 호출 한다
#         #모든 부모 클래스에서 초기화가 필요하다
#         Unit.__init__(self)
#         Fly.__init__(self)

# drop = FlyUnit()

# class House :
#     def __init__(self, location, house_type, deal, price, year):
#         self.location = location
#         self.house_type = house_type
#         self.deal = deal
#         self.price = price
#         self.year = year

#     def show_detail(self):
#         print(self.location, self.house_type, self.deal, self.price, self.year)


# house = []

### 솔드 아웃 에러
# class SoldOutError(Exception):
#     pass


# chicken = 10
# waiting = 1
# while(True):
#     try:
#         print("[남은치킨 :{0}]".format(chicken))
#         order = int(input(" 몇 마리 주문 하시겠습니까?"))
#         if order > chicken:
#             print("재료가 부족합니다.")

#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료 되었습니다.".format( waiting,order))
            
#             waiting += 1
#             chicken -= order


#         if chicken == 0:
#             raise SoldOutError


#     except ValueError:
#         print("잘못된 값을 입력")
#     except SoldOutError:
#         print("재고가 소진되어 더이상 주문을 받지 않습니다")
#         break


######################## 모듈
#필요한것 끼리 잘 묶여진 파일
#필요한것 끼지 부품처럼 잘 만들어진 파일
#자동차를 이용하다가 타이어가 마모되면 타이어만 교채 하면 된다
# 범퍼만 교체 하면된다/ 하지만 엔진까지 연결되어 있었다면 수리 기간이나 비용이 많이 든다
# 위와 같은 상황을 방지하기 위해 모듈을 만든다

#극장에서 현금만 받는다. 잔돈은 안바꿔준다
# 영화 티켓이 3.5인데 4만원을 줘도 안거슬러준다
# 사람수에 따라 가격 측정 가능한 모듈

# import moive_module

# moive_module.price(3) #3명이서 영화 보러옴
# moive_module.price_morning(4)

####v패키지 모듈의 집합
#신규여행사 프로젝트
#태국과 베트남의 패키지 여행
#패키지 여행을 