##웹크롤링

import requests
from bs4 import BeautifulSoup

res = requests.get('http://v.media.daum.net/v/20170615203441266')

print(res.content)

soup = BeautifulSoup(res.content, 'html.parser')

title = soup.find('title')

print(title.get_text())


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



