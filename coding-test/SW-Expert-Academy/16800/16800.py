# 약수 구하는 함수
def get_division(n):
    data = []
    for i in range(1, n//2+1):
        if n %i == 0:
            data.append(i)
    data.append(n)
    return data

T = int(input())

# tc 3 번이 걸린다. 약수 구하는 함수에서 시간이 많이 걸림.
# 해결책은 모르것다.
for tc in range(1, T+1):
    n = int(input())
    i , j = 1, 1
    
    while i * j < n:
        if len(get_division(n)) > 2:
            j = get_division(n)[len(get_division(n))//2]
            i = get_division(n)[len(get_division(n))//2-1]
        else:
            i = get_division(n)[0]
            j = get_division(n)[1]
        print(f'# {i-1+j-1}')
        