# 백준
# 소수 찾기
# 소수의 개념 : 1과 자기 자신만을 약수로 가지는 수

# 소수를 구하는 방법,
# 1. 2부터 n-1까지 나누어 떨어지는지 확인
# 2. 2부터 n의 제곱근까지 나누어 떨어지는지 확인
# 3. 2부터 n의 제곱근까지 나누어 떨어지는지 확인하고, 나누어 떨어지는 수가 있으면 소수가 아님

def prime_number_1(x):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 약수는  n/2보다작거나 같다는 가정이 통하기 때문에
def prime_number_2(x):
    for i in range(2, n//2+1):
        if x % i == 0:
            return False
    return True

# 제곱근 까지 나누기
def prime_number_3(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

# 시간 복잡도를 줄이기 위해 math 모듈을 사용
import math
def prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

# 에라토네스의 체 활용한 방법

def prime_number_4(x):
    n += 1
    array = [True for i in range(n)]
    for i in range(2, int(math.sqrt(n))+1):
        if array[i] == True:
            j = 2
            while i * j < n:
                array[i*j] = False
                j += 1
