from http.client import ImproperConnectionState
from operator import index
from re import sub
from telnetlib import PRAGMA_HEARTBEAT
from tkinter import N

'''
print(1!=3)
print((3>0) | (3>5))
print(5>4>7)

print(2+3*4)
print((2+3)*5)

number = 2+3*4
print(number)
number = number +2
print(number)
number += 2
print(number)
number *= 2 
print(number)
number /= 2
print(number)

number %= 5
print(number)'''


'''
print(abs(-5))
print(pow(4,2))
print(max(5,12))
print(min(5,12))
print(round(4.99))

from math import *

print(floor(4.99))# 내림
print(ceil(3.14))# 올림
print(sqrt(16))# 제곱근
'''

#랜덤함수 - 난수
from random import *
# print(random()) #0.0 이상 1.0 미만의 임의의 값을 생성
# print(random()*10) # 0~10.0 미만의 임의의수

# #소숫점 제거
# print(int(random()*10))#0~10 임의이 숫자
# print(int(random()*10)+1)#1 ~10 이하의 임의이 숫자
# pr

# print(int(random() * 45 + 1))
# print(int(random() * 45 + 1))
# print(int(random() * 45 + 1))
# print(int(random() * 45 + 1))
# print(int(random() * 45 + 1))
# print(int(random() * 45 + 1))


# print(randrange(1,46)) # 1 ~ 45이하의 랜덤 출력
# print(randrange(1,46)) # 1 ~ 45이하의 랜덤 출력
# print(randrange(1,46)) # 1 ~ 45이하의 랜덤 출력
# print(randrange(1,46)) # 1 ~ 45이하의 랜덤 출력
# print(randrange(1,46)) # 1 ~ 45이하의 랜덤 출력
# print(randrange(1,46)) # 1 ~ 45이하의 랜덤 출력


# print(randint(1,45))#randint 1~45 이하의값을 생성

# quiz 2
# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별날 짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

#day = randint(4,28)
#print("스터디 날짜는 "+str(day)+"입니다.")


# 문자열
# sentence = "나는 소년"
# print(sentence)
# sentence2 = "vktlTjsdms tnldnjdy"
# print(sentence2)
# sentence3 = """

# 나는 소년이고 ,
# 파이썬은 쉬워요
# """
# print(sentence3)




#슬라이싱
# jumin = "930903-1111111"
# #정보 중에 필요한 정보만 찾아서 쓰는것
# print("성별 : " + jumin[7]) # 자료는 0번째 자리 부터 시작
# print("년 : "+jumin[0:2])#0부터 2 직전 까지 가져온다.
# print("월 : " + jumin[2:4])#4뒷자리 부터 6 직전 까지
# print("생년월일: "+jumin[:6])# 6미만의 자리까지.

# print("뒷 자리 : " + jumin[7:])# [7:14], [7:] 둘다 사용가능
# #뒤에서 부터 가져 올수도있다
# print("뒤 7자리 (뒤에서 부터) :" + jumin[-7:]) # 맨뒤에서 끝까지



# 문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower())#소문자
# print(python.upper())#대문자
# print(python[0].isupper())#0번쨰 위치 문자가 대문자 인지 # True
# print(len(python))#문자열의 길이 반환 # 17
# print(python.replace("Python","Java")) # replace 변환

# index = python.index("n")
# print(index) # 문장에서 해당 문자 찾기

# index = python.index("n",index +1) # 2번재 n 찾기
# print(index)

# print(python.find("n"))
# print(python.find("Java"))  #못 찾으면 -1 출력하고 진행

# #차이점 , find 못찾으면 -1 출력하고 진행 index는 프로그램 오류로 후속 진행 불가 
# #print(python.index("Java"))
# print(python.count("n")) # 해당 문자가 몇글자 나오는지 카운트


#문자열 포멧
#print("a","b")
#print("a"+"b")

#방법1
# print("나는 %d살입니다"% 20)#정수
# print("나는 %s을 좋아해요"%"파이썬")#문자열
# print("Apple은 %c로 시작해요"%"A")#한단어
# # %s로 사용하면 모든게 다 해당된다
# print("나는 %s색과 %s을 종아해요" %("파란","빨간"))


#방법2
# print("나는 {}살입니다".format(20))
# print("나는 {}색과 {}을 종아해요".format("파란","빨간"))
# print("나는 {0}색과 {1}을 종아해요".format("파란","빨간"))
# print("나는 {2}색과 {0}을 종아해요".format("파란","빨간","초록","노랑"))
# 중괄호 안에는 배열이 들어갈수 있다


#방법3

#print("나는 {age}살이며, {color}색을 좋아해요".format(age =20, color="빨간"))
#변수를 지정하고 format에서 변수를 지정해준다

#방법4
# age = 20
# color = "빨간"
# # 미리 선언 하고 가져다 쓴다
# print("나는 {age}살이며, {color}색을 좋아해요")


# #탈출 문자
# print("백문이 불여일견\n 백견이 불여일타")
# #탈출문자중 하나인 \n 문장내에서 줄바꿈

# print("저는 '나도코딩'입니다.")
# #문장내에 큰 따옴표를 사용하고 싶으면 '로 감싸고 "를 안으로
# # " 앞으로\를 붙히면 "를 출력 해준다
# # \" \'
# print("저는 \"파이썬\"입니다.")

# # \\ : 문장 내에서 \
# # \\두개를 붙혀줘야 실행 된다

# # \r  : 커서를 맨앞으로 이동
# print("Red Apple\rPine") # Red 가 지워지고 Pine이 들어온다

# # \b는 백스페이스 역활 ( 앞한글자 삭제)
# print("Redd\bApple")

# # \t : 탭
# print("Red\tapple")



#quiz 사이트별로 비번 만드는 프로그램
# url = "http://google.com"
# my_str = url.replace("http://","") # 규칙1
# #print(my_str)
# my_str = my_str[:my_str.index(".")] # 규칙2
# #print(my_str)
# passward = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

# print("{0} 의 비밀번호는 {1}입니다.".format(url, passward))




#리스트 []
# 지하철 칸 별로 10명, 20명, 30명
# subway = [10,20,30]
# print(subway)
# subway = ["유재석","조세호","박명수"]
# print(subway)

# #조세호 찾기
# print(subway.index("조세호"))


# #리스트 추가
# subway.append("하하")
# print(subway)


# #리스트 중간에 추가
# subway.insert(1,"정형돈") #중간에 추가
# print(subway)

# #한명씩 뒤에서 꺼냄
# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# num_list = [4,3,2,1,5,6]
# num_list.sort() #오름차순으로 정렬
# print(num_list)


# #꺼꾸로 정렬
# num_list.reverse()
# print(num_list)

# 모두지우기
# num_list.clear()
# print(num_list)

#list는 다양한 자료형에 사용가능하다
# mix_list = ["조세호",1,True]
# num_list = [4,3,2,1,5,6]
# num_list.extend(mix_list)
# #리스트 합치기
# print(num_list)



#사전#
#단어를 찾으면 단어에 대한 설명이 나온다
#키와 벨류 형태로 나오게된다
#cabinet = {3:"유재석",100:"김태호"} # 키 : 벨류 식으로 구성
# print(cabinet[3])
# print(cabinet[100])
# #리스트 처럼 사용가능

# print(cabinet.get(3))
# #get 함수로도 사용가능

# #print(cabinet[5])
# print(cabinet.get(5))
# #리스트 형식은 에러 뜨지만 .get 형식은 none출력후 지속

# print(cabinet.get(5,"사용가능"))
# #즉석으로 삽입 가능
# print("hi")

#print(3 in cabinet)
#print(5 in cabinet)
# 자료에 값이 있는지도 확인 가능

# cabinet = {"a-3":"유재석",'B-100':"김태호"}
# cabinet["a-3"] = "김종국" #김종국으로 변경
# cabinet["c-20"]= "조세호" #조세호 추가


# #키 삭제
# del cabinet["a-3"]

# #현재 사용중인 kEY만 출력 할려면
# print(cabinet.keys())
# # value 만 출력
# print(cabinet.values())

# #key,value 모두 출력
# print(cabinet.items())

# # 모두 삭제
# cabinet.clear()
# print(cabinet)

#print(cabinet)




####### 튜플 ## 리스트 처럼 편집이 불가능 하지만 속도가 빠르다
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# #에드 안됨

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name,age,hobby)

# (name, age, hobby) = ("김종국",20,"코딩")
# print(name,age,hobby)



#####################세트
