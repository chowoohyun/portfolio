# 프로그래머스
# 마법의 엘레베이터
# 랩2


def use_magic_rock(floor):
    floor = str(floor)
    tmp = 0
    for i in floor:
        tmp += int(i)
    return tmp

def solution(storey):
    answer =0
    for i in range(1, storey+1):
        answer += use_magic_rock(i)
    return answer

solution(16)