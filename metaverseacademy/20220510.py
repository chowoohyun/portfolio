##[AI 전공] 1차시 - 파이썬 기초 문법 (1)
#Short Hand if you
# a = 200
# b = 33

# if a > b : print('a is grater than b')

# print('A') if a > b else print('B')

# a = 330
# b = 330
# print('A') if a > b else print('=') if a==b else print('B')


#중첩if Nested if
# x = 41
# if x > 10:
#     print('above Ten,')
#     if x >20: print('')
#     else
# #pass state
#  a= 33
#  b = 200
#  if b>


#while Loop
# i = 0
# while i < 6:
#     i += 1
#     if i ==3:
#         continue
#     print(i)

# fruits = ['apple', 'banana', 'cherry']

# for x in fruits:
#     print(x)

# for x in 'banana': 
#     print(x)

# fruits = ['apple', 'banana', 'cherry']

# for x in fruits:
#     print(x)
#     if x == 'banana':
#         break


# fruits = ['apple', 'banana', 'cherry']
# for x in fruits:
#     if x == 'bnana':
#         break
#     print(x)
#15:26 강의 동영상에서 이상한점
#for 루프에서 break 가 되면 끝나는데
#if 문안에 banana를 일부러 틀리게 넣으신건지 문의

# fruits = ['apple', 'banana', 'cherry']
# for x in fruits:
#     if x == 'banana':
#         continue
#     print(x)

# for x in range(6):
#     print(x)

# for x in range(2,6):
#     print(x)


#range(시작, 끝, 뛰어넘는 갯수)
# for x in range(2, 30, 3):
#     print(x)

# ajd = ['red','big','testy']
# fruits = ['watermelon', 'banana','mango']

# for x in ajd:
#     for y in fruits:
#         print(x, y)


'''[AI 전공] 2차시 - 파이썬 기초 문법 (2)
리스트 튜플 자료형 사용방법

List 담아놓는 그릇 같은것
'''
# thelist = ['apple','banana','cherry']
# print(thelist)


# thelist = ['apple','banana','cherry','apple']
# print(thelist)

# print(len(thelist))

# #list 에는 문자, 숫자, 불리안
# #타입은 리스트

# #list에도 슬라이스가 가능
# print(thelist[1:3])
# print(thelist[-1])
# print(thelist[:3])
# print(thelist[1:])
# print(thelist[-3:-1])

# if 'cherry' in thelist:
#     print('yes')

# list1 = ['apple','banana','cherry']
# list1[1] = 'blackberry'
# print(list1)


# #새로운 아이템 추가
# list1[1:2] = ['banana','watermelon']
# print(list1)

#체인지
#add list item
# list2 = ['a','b','c']
# list2.append('orange')
# print(list2)

# list2.insert(1, 'watermelon')
# print(list2)

# list3 = ['mango','pine','papaya']
# list3.extend(list2)
# print(list3)

# list3.remove('orange')
# print(list3)

# list3.pop()
# print(list3)
# #pop은 스택의 형태

# #del
# del list3[0]
# print(list3)

# del list3
# # print(list3)#리스트를 지워버렸기 때문에 에러

# list3 = ['a','b']
# list3.clear()
# print (list3)

# list1 = ['apple', 'banana', 'cherry','mango']

# newlist = []

# for x in list1:
#     if 'a' in x:
#         newlist.append(x)

# print (newlist)



# #리스트안에 조건문을 넣어서 리스트를 생성가능
# list2 = ['apple', 'banana', 'cherry','mango']

# newlist2 = [x for x in list2 if 'a' in x]

# print (newlist2)

# newlist3 = [x for x in list2 if x != 'apple']
# print(newlist3)


# list3 = [ x for x in range(10)]
# print(list3)

# #Sort list

# list2.sort(reverse=True)
# print(list2)

'''
딕셔너리 집합
'''

#python sets
# myset = {"apple","banana","orange"}
#print(myset)
#우리가 입력한 대로 나오지 않는다.
#새로운 아이템 추가나 삭제는 가능
#듀플리케이트가 허락 되지 않음

#apple 추가 하면 중복을 제거
# thisset = {"apple", "banana", "orange","apple"}
#print(thisset)

#중복을 제거 하였기 때문에 길이는 3
#print(len(thisset))

#스트링, 숫자, 불리안 다 가능, 혼합도 가능

# for x in myset:
#     print(x)

# print("banana" in myset)

# myset.add("cherry")
# print(myset)

#set은 list랑 호환이 됨
#삭제 remove, update = 추가
#삭제 discard

# myset.discard("orange")
# print(myset)

# x = myset.pop()
# print(x) #리스트와 다르게 뭐가 나올지 모름
# print(myset)

#del도 사용가능

# for x in myset:
#     print(x)

thisset = {"1","2","3"}
myset = {"a","b","c","1"}

set3 = thisset.union(myset)
print(set3)
#union 을 통해 합칠수 있음

z= thisset.intersection(myset)
print(z)
#intersection 두개의 set에서 같은것을 찾는것

