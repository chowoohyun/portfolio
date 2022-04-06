#4월 5일  
#for 문 2개를 이용한 구구단

# for i in range(2, 10):
#     print(i,"단")

#     for j in range(1,10):
#         print(i,"x",j,"=",i*j)




# #거꾸로 출력하기, ::-1

#방법 1
# lst = ['a','b','c','d','e','f','g','h']

# for i in lst[::-1] :
#     print(i, end="\t")



#방법 2 a에 리스트 총 길이 값을 넣어주고 하나씩 빼면서 출력
# lst=['dog','hippo','elephant','lion','tiger','alligator']

# a=len(lst)

# index=0

# print(a)

# for i in range(len(lst)):

#     a=a-1

#     index=index+1

#     print(index,'.',lst[a],'',end='')



## 백준 1330

# A, B = map(int, input().split())

# if A > B :
#     print('>')
# elif A < B :
#     print('<')
# else:
#     print("==")


### 백준 10950

# T = int(input()) #테스트 케이스 갯수 T를 입력 받음

# for i in range(T):
#     a, b = map(int, input().split())
#     print(a+b)


#### 백준 2741

# N = int(input())
# for i in range(1,N+1):
#     print(i, end="\n")


##### 백준 11022

# T = int(input())

# for i in range(1,T+1):
#     a, b = map(int, input().split())

#     print(f"Case #{i}: {a} + {b} = {a+b}")



###### 백준 