# 그리디 알고리즘
# 카드 정렳하기 

# 문제
'''
정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다. 이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.

매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 고르는 순서에 따라서 비교 횟수가 매우 달라진다. 예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다. 그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.

N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.
'''
'''
import sys

n = int(sys.stdin.readline())
cart = []
for _ in range(n):
    cart.append(int(sys.stdin.readline()))

def solution(cart):
    result = 0
    while len(cart) > 1:
        cart.sort()
        #print(1)
        sum = cart[0] + cart[1]
        result += sum
        #print(2)
        cart = cart[2:]
        cart.append(sum)
        print(len(cart))
    return result

print(solution(cart))
'''

# heaq  자료 구조를 활용한 풀이,
# 자료 구조상 heaq은 자동 정렬이 되기 때문에 sort를 사용하지 않아도 된다.
import heapq
import sys

n = int(sys.stdin.readline())
cart = []

for _ in range(n):
    heapq.heappush(cart, int(sys.stdin.readline()))

def solution(cart):
    result = 0
    while len(cart) > 1:
        print(len(cart))
        sum = heapq.heappop(cart) + heapq.heappop(cart)
        result += sum
        print(result)
        heapq.heappush(cart, sum)
    return result

print(solution(cart))