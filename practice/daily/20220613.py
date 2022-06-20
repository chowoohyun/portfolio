def solution(arr):
    tmp = 0
    for i in arr:
        tmp += i
    answer = print(tmp / len(arr))
    return answer



arr1 = [1,2,3,4]
solution(arr1)