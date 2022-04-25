##웹크롤링

# import requests
# from bs4 import BeautifulSoup

# res = requests.get('http://v.media.daum.net/v/20170615203441266')

# print(res.content)

# soup = BeautifulSoup(res.content, 'html.parser')

# title = soup.find('title')

# print(title.get_text())


##프로그래머스 level 1 키패드 누르기

# def cal(num, now_l, now_r, pos, handed):
    
#     X,Y = 0,1
#     dist_l = abs(pos[now_l][X]-pos[num][X]) + abs(pos[now_l][Y]-pos[num][Y])
#     dist_r = abs(pos[now_r][X]-pos[num][X]) + abs(pos[now_r][Y]-pos[num][Y])
    
#     if dist_l == dist_r:
#         return 'R' if handed == 'right' else 'L'
#     return 'R' if dist_l > dist_r else 'L'

    
# def solution(numbers, hand):
    
#     HANDED = hand
#     position = {1:(0, 0), 2:(0, 1), 3:(0, 2),
#                 4:(1, 0), 5:(1, 1), 6:(1, 2),
#                 7:(2, 0), 8:(2, 1), 9:(2, 2),
#                 '*':(3, 0), 0:(3, 1), '#':(3, 2)}
#     left, right = set([1,4,7]), set([3,6,9])
    
#     now_l, now_r = '*', '#'
    
#     result = ''
    
#     for num in numbers:
#         if num in left:
#             result += 'L'
#             now_l = num
#         elif num in right:
#             if num in right:
#                 result +='R'
#                 now_r = num
                
#         else:
#             result += cal(num, now_l, now_r, pos, handed)
#             if result[-1] == 'L' :
#                 now_l = num
#             else:
#                 now_r = num
                
#     return result

# def solution(numbers, hand):
#     answer = ''
#     lastL = 10
#     lastR = 12
    
#     for n in numbers:
#         if n in [1,4,7]:
#             answer += 'L'
#             lastL=n
#         elif n in [3,6,7]:
#             answer += 'R'
#             lastR = n 
        
#         else:
#             if n == 0:
#                 n = 11
            
#             L_dis = abs(lastL-n)//3 + abs(lastL-n)%3
#             R_dis = abs(lastR-n)//3 + abs(lastR-n)%3
            
#             if L_dis > R_dis:
#                 answer += 'R'
#                 lastR = n
#             elif L_dis < R_dis:
#                 answer +='L'
#                 lastL = n
#             else:
#                 if hand == 'left':
#                     answer += 'L'
#                     lastL = n
#                 else:
#                     answer +='R'
#                     lastR = n
            
#     return answer



##codeup 6094 이상한 출석 번호 부르기3
'''
정보 선생님은 오늘도 이상한 출석을 부른다.

영일이는 오늘도 다른 생각을 해보았다.
출석 번호를 다 부르지는 않은 것 같은데... 가장 빠른 번호가 뭐였지?

출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

단, 
첫 번째 번호와 마지막 번호가 몇 번인지는 아무도 모른다.
음수(-) 번호, 0번 번호도 있을 수 있다.

참고
리스트에 출석 번호를 기록해 두었다가, 그 중에서 가장 작은 값을 찾아내면 된다.
그런데, 가장 작은 값은 어떻게 어떤 것과 비교하고, 어떻게 찾아야 할까?
'''


# min 함수를 사용하는방법
# num = int(input())
# numlist = map(int, input().split())

# a = min(numlist)
# print(a)

# 정석 풀이 리스트내에서 비교

# n = int(input())
# a = input().split()

# for i in range(n):
#     a[i] = int(a[i])

# min = a[0]
# for i in range(0, n):
#     if a[i] < min:
#         min = a[i]

# print(min)


##codeup 6087
'''
1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,
3의 배수인 경우는 출력하지 않도록 만들어보자.

예를 들면,
1 2 4 5 7 8 10 11 13 14 ...
와 같이 출력하는 것이다.
'''

# n = int(input())

# for i in range(1,n+1):
#     if i%3 == 0:
#         continue
#     print(i,end=' ')


##codeup 6080
'''
1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
나올 수 있는 모든 경우를 출력해보자.
'''
# a, b = map(int, input().split())

# for i in range(1, a+1):
#     for j in range(1, b+1):
#         print(i, j, end='\n')

##그리디 알고리즘 공부
##codeup 2001 최소대금
'''
파파 파스타 가게는 점심 추천 파스타와 생과일 쥬스 세트 메뉴가 인기가 좋다.

이 세트 메뉴를 주문하면 그 날의 3 종류의 파스타와 2 종류의 생과일 쥬스에서 하나씩 선택한다.

파스타와 생과일 쥬스의 가격 합계에서 10%를 더한 금액이 대금된다.

어느 날의 파스타와 생과일 쥬스의 가격이 주어 졌을 때, 그 날 세트 메뉴의 대금의 최소값을 구하는 프로그램을 작성하라.
'''

# p =[]
# b = []

# for i in range(3):
#     p.append(float(input()))

# for i in range(2):
#     b.append(float(input()))

# result = (min(p)+min(b))*1.1
# print('%.1f' % result)


##codeup 3120
'''컴퓨터실에서 수업 중인 정보 선생님은 냉난방기의 온도를 조절하려고 한다.

냉난방기가 멀리 있어서 리모컨으로 조작하려고 하는데, 리모컨의 온도 조절 버튼은 다음과 같다.

1) 온도를 1도 올리는 버튼

2) 온도를 1도 내리는 버튼

3) 온도를 5도 올리는 버튼

4) 온도를 5도 내리는 버튼

5) 온도를 10도 올리는 버튼

6) 온도를 10도 내리는 버튼

이와 같이 총 6개의 버튼으로 목표 온도를 조절해야 한다.

현재 설정 온도와 변경하고자하는 목표 온도가 주어지면 이 버튼들을 이용하여 목표 온도로 변경하고자 한다.

이 때 버튼 누름의 최소 횟수를 구하시오.

예를 들어, 7도에서 34도로 변경하는 경우,

7 -> 17 -> 27 -> 32 -> 33 -> 34

이렇게 총 5번 누르면 된다.
'''

# a ,b = input().split()
# a = int(a)
# b = int(b)
# cnt = 0

# temp = a-b
# result = 0 

# while True:
#     if temp == 0:
#         break
#     elif temp > 7:
#         temp -= 10
#     elif temp > 3:
#         temp -= 5

#     elif temp >= 1 :
#         temp -=1
#     elif temp < 0 :
#         temp *= -1
#         result -=1
#     result += 1


# print(result)


