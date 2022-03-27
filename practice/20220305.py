# #집합 (set)
# #중복이 안되고 순서가 없음
# my_set = {1,2,3,3,3}
# print(my_set) #12333 출력되는게 아니라 123만 출력

# java = {"유재석","김태호","양세형"}
# python = set(["유재석","박명수"])


# #교집합 (java와  python 모두 사용할수 있는 사람)
# print(java &python)
# print(java.intersection(python))

# #합집합 자바와 파이썬 둘중 하나 사용 가능한것
# print(java | python)
# print(java.union(python))

# # 차집합 ( 자바는 가능, 파이썬은 할줄 아는 개발자)
# print(java-python)
# print(java.difference(python))


# #python 할줄 아는 사람 늘어남
# python.add("김태호")
# print(python)

# #python 뺴기
# java.remove("김태호")
# print(java)



# ################## 자료구조의 변경
# menu = {"커피","주스","우유"}
# print(menu, type(menu))

# menu = list(menu) #타입이 리스트 형식으로 바뀜
# print(menu, type(menu))


# menu = tuple(menu) #타입이 튜플 형식으로 바뀜
# print(menu, type(menu))


# menu = set(menu)
# print(menu, type(menu))





'''퀴즈'''

#당첨자 발표 프로그램, 20명 중에 치킨 1명 커피 3명

# from random import *
# user = range(1,21)
# # print(type(user))
# user = list(user)
# shuffle(user)

# winners = sample(user, 4)

# print("치킨 :{0}".format(winners[0]))
# print("커피 :{0}".format(winners[1:]))



####### if
#분기 이런 상황에서는 이런 코드 저런 상황에서는 저런 코드
#비 = 우산, 미세먼지 = 마스크

# weather = input("오늘 날씨는 어때요? ")
# if weather =="비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")



# temp = int(input("기온은 어때요?"))
# if 30 <= temp :
#     print("너무 더워요")

# elif 10<= temp and temp< 30:
#     print("야외활동하기 좋아요")
# elif 0<= temp<10:
#     print("너무 추워요 나가지마세요")
# else:
#     print("박에 ㄴㄴ")

# 범위 제한하는걸 잘 해봐야 한다




################for

#for waiting_no in [0,2,3,4]:

#for waiting_no in range(1,6):
#   print("대기번호 : {0}".format(waiting_no))
#for 문에 들어가서 0~4 까지 출력
#순차적으로 커지게 되면 range 함수 사용가능

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0},커피가 준비가 되었습니다.".format(customer))


#while문
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기 처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index +=1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")



#반복문 컨디뉴와 브레이크

# absent = [2,5] # 결석
# no_book = [7] #책을 깜빡
# for student in range(1,11):
#     if student in absent :
#         continue  #계속 진행
#     if student in no_book:
#         print("오늘 수업 여기까지, {0}은 교무실로".format(student))
#         break # 7번에서 브레이크로 반복문 탈출
#     print("{0}, 책을 읽어줘".format(student))



##########한줄로 끝내는 for 문

#출석 번호가 1,2,3,4,5, 앞에  100을 붙히기로 -> 101,102,103
# student = [1,2,3,4,5,]
# print(student)
# student = [i+100 for i in student]
# print(student)

# #학생들 이름을 길이로 바꾸는 연슴
# students = ["아이언맨","토르","아이엠그루트"]
# students = [len(i) for i in students]
# print(students)

#학생이름을 대문자로

# student = ["Iron man","Thor","I am groot"]
# student = [i.upper() for i in student]
# print(student)




'''퀴즈5'''
#cocoa 서비스를 이용하는 택시 기사님
#50명의 승객과 매칭 기회가 있을때, 총 탑승 승객수를 구하는 프로그램을 작성하시오
#조건 1: 승객별 운행 소요시간은 5분 ~50분 사이의 난수로 정해집니다.
#조건 2: 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

#출력문 예제
#[0] 1번째 손님 (소요시간 : 15분)
#[ ] 2번째 손님 (소요시간 : 50분)
#[0] 3번째 손님 (소요시간 : 5분)
#...
#[ ] 50번째 손님 (소요시간 : 16분)

#총 탑승 승객 : 2분

# from random import *
# cnt = 0 # 총 탑승 승객수
# for i in range(1, 51): # 1~50 이라는 승객수
#     time = randrange(5, 51)# 5~50 분 사이의 시간
#     if 5 <= time <=15: # 5~15분 이내의 손님, 탐승 승객 수 증가 처리
#         print("[0] {0}번쨰 손님 (소요시간 : {1}분)".format(i,time))
#         cnt +=1
#     else: #소요시간이 15분 이상이라 매칭 실패한 경우
#         print("[] {0}번째 손님 (소요시간 : {1}분)".format(i,time))

# print("총 탑승 승객 : {0}분".format(cnt))





'''함수'''
# #함수 
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# # 입금 하는 함수
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}입니다.".format(balance+money))
#     return balance + money

# #출금 하는 함수
# def withdraw(balance, money):
#     if balance >= money :
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
#         return balance - money
#     else:
#         print("출금이 완료 되지 않았습니다. 잔액은 {0}입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money): # 저녁에 출금
#     commission = 100
#     return commission, balance -money - commission


# balance = 0
# balance = deposit(balance, 1000)
# #balance = withdraw(balance, 2000)
# #balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원 이며, 잔액은 {1}입니다.".format(commission, balance))






##############기본값 설정 함수

# def profile(name, age, main_lang):
#     print("이름 : {0}\t 나이 : {1}\t 주사용언어{2}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")


#만약 같은 하교 같은반 같은 수업 이라면
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t 나이 : {1}\t 주사용언어{2}".format(name, age, main_lang))

# profile("유재석")
# profile("김태호", 20, "자바")


# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="자바", age=20)
# profile(name="김태호")

####가변 함수

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}, 나이 : {1}".format(name, age),end="")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20,"python","Jave","c","C++","C#")
# profile("김태호",25,"kotlin", "swift","","","")

# def profile(name, age, *lan):
#     print("이름 : {0}, 나이 : {1}\t".format(name, age),end=" ")
#     for lang in lan:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "python", "Jave", "c", "C++", "C#", "javascript")
# profile("김태호", 25, "kotlin", "swift")



####### 지역 변수와 전역 변수
# 지역변수 = 함수 에서만 사용, 전역 변수 = 프로그래밍 전체에서 사용되는 함수
# gun = 10

# def checkpoint(soldiers): # 경계 근무
#     global gun #지역 변수 gun을 체크 포인트 함수 내에서 사용하겠다는 뜻
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

#     return gun
    
# print("전체 총 : {0}".format(gun))
# #checkpoint(2)#경계근무 나감
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))
### 위 코딩으로 하면 에러뜸, gun이라는 변수가 지역 변수이기 때문에
### 지역 변수를 쓰게 되면 코딩이 어려워 지기 떄문에 많이 안씀


'''표준 체중을 구하는 퀴즈'''
#표중 체중 : 각 개인의 키에 적당한 체중
#성별에 따른 공식


# def std_weight(height, gender): # 키는 미터단위 (실수 단위), 성별은 "남""여"

    
#     if gender == "남" :
#         return height* height*22
#     else:
#         return height* height*21

# height = 175
# gender = "남"
# weight = round(std_weight(height/100, gender),2) # m 단위로 바꿔야 하기 때문에 나눠준다

# print("키 {0}cm {1}의 표중 체중은 {2}kg 입니다.".format(height, gender, weight))

    

########표준 입출력


# print("python","Java", sep=",", end="?") #sep은 사이사이에 들어가는걸 결정 가능
# print("무엇이 더 재밌을 까요?")#end는 원래 줄바꿈 이였지만 지정해주면 줄바꿈이 다른걸로 바꿔진다

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# #시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
##ljust 왼쪽 정렬, rjust 오른쪽 정렬, sep 띄어진 공간에 넣어줄것

#은행 대기 순번표
# # 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호 :" + str(num).zfill(3))
###### zfill(숫자) 3자리에서 값이 없는 곳은 0으로 채워달라


#############표준 입력
###사용자 입력으로 받게 되면 기본적으로 str 타입으로 받는다.

# answer = input("아무 값이나 입력 하세요 :")
# print(type(answer))
#print("입력하신 값은 {0} 입니다.".format(answer))



###### 다양한 출력 포멧
# # 빈 자리는 빈공간으로 두고 오른쪽 정렬을 하되, 총 10 자리 공간을 확보
# print("{0: >10}".format(500))

# # 양수일때는 +로 표시 음수일때는 -로 표시
# # 위 방법도 -출력은 가능 다만, +는 출력 불가
# print("{0: >10}".format(500))
# print("{0: >+10}".format(-80))

# # 왼쪽 정렬 하고, 빈칸으로 _로 채움
# print("{0:_<10}".format(500))


# # 큰숫자 입력시 3자리 마다 콤마 찍어주기
# print("{0:,}".format(10000000000000000))

# #3자리 마다 콤마도 찍어주지만  + - 부호 붙히기
# print("{0:+,}".format(10000000000000000))
# print("{0:+,}".format(-10000000000000000))

# #3자리 마다 콤마도 찍고, 부호도 붙히고, 자릿수도 확보
# # 빈자리는 ^로 채우기
# print("{0:^<+30,}".format(10000000000000))

# #소숫점을 출력 하는 방법
# print("{0:f}".format(5/3))
# #소숫점을 특정 자리까지만 (소수점 3째 자리에서 반올림 해달라)
# print("{0:.2f}".format(5/3))


#########################파일 입출력
#파일을 열어서 점수 정보를 변경하는것

# score_file = open("score.txt","w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# w는 덮어 쓰기, a는 수정

# score_file = open("score.txt","a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()


# #r은 읽기 전용
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기 동작, 커서는 다음줄로
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()


# #몇줄인줄 모를때
# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line :
#         break
#     print(line, end="")
# score_file.close()

# #리스트에 값을 넣어서 처리 readlines
# score_file = open("score.txt","r",encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line)
# score_file.close()



####################피클
#프로그램상에서 이용하고 있는것을 파일로 저장
#피클을 이용해서 협업 가능

# import pickle

# profile_file = open("profile.pickle","wb")
# profile = {"이름":"박명수","나이":30,"취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile 정보를 profile_file에 저장
# profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

#우리가 가지고 있는 데이터를 피클에다 저장, 노드에 저장
#변수에 입혀서 사용 가능


########위드 파일을 읽고 쓰도 닫고 편하게 사용가능
# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
# #열었던 파일에 대해서 닫을 필요가 없음

# with open("study.txt", "w",encoding="utf8") as study_file:
#     study_file.write("파이썬을 공부중입니다.")

# with open("study.txt","r",encoding="utf8") as study_file:
#     print(study_file.read())


# import pickle

# for week in range(1,51):
#     with open(str(week)+"주차.txt","w",encoding="utf8") as report_file:
#         report_file.write("-{0} 주차 주간 보고서 \n\n부서 : \n이름 : \n업무요약 :\n".format(week))

