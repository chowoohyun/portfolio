def hanoi(num, start, end):
    if num == 1:
        print(start, end)
        return
    else:
        hanoi(num-1, start, 6-start-end)
        print(start, end)
        hanoi(num-1, 6-start-end, end)

N = int(input())

print(2**N -1)
hanoi(N, 1, 3)