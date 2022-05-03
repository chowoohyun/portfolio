##그리드 알고리즘 공부
##그리드 알고리즘이란?
##선택의 순간마다 당장 눈앞에 보이는 최적의 상황만을 쫓아 최종적인 해답에 도달하는 방법
# 해결하는 방법
# 선택 절차(Selection Procedure): 현재 상태에서의 최적의 해답을 선택한다.
# 적절성 검사(Feasibility Check): 선택된 해가 문제의 조건을 만족하는지 검사한다.
# 해답 검사(Solution Check): 원래의 문제가 해결되었는지 검사하고, 해결되지 않았다면 선택 절차로 돌아가 위의 과정을 반복한다.


#프로그래머스
#https://programmers.co.kr/learn/courses/30/lessons/42576
#완주하지 못한 선수

# import collections


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

# #counter 함수를 이용하는 법

# ##sort ,zip 를 활용하는 방법 // 내 풀이법
# def solution(participant, completion):

#     participant.sort()
#     completion.sort()
    
#     for p,c in zip(participant, completion):
#         if p != c:
#             return p
    
#     answer = participant.pop()
#     return answer


