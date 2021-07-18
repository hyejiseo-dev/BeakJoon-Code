#2869번 : 달팽이는 올라가고 싶다
# a,b,v = map(int,input().split(' '))
# day = 0 #올라가는데 걸리는 일수
# h = v-a #

# if h % (a-b) == 0: 
#   day = int(h/(a-b)+1)
# else:
#   day = int(h/(a-b)+2)

# print(day)

#10250 : ACM 호텔
# N = int(input())
# for i in range(N):
#   h,w,n = map(int,input().split())
#   room_num = (n%h)*100 + (n//h)+1
#   if n%h == 0:
#     room_num = h*100 + (n//h)
#   print(f'{room_num}')

# 2775 : 부녀회장
# T=int(input()) #2개 층, 호실 받기

# for i in range(T):  
#     k=int(input())
#     n=int(input())
#     base=[j for j in range(1,n+1)] # 1-n호실 까지 리스트 생성 / 0층에는 1,2,3,4,5,6..
#     for l in range(k): 
#         for m in range(1,n):
#             base[m]+=base[m-1] # 아래층 호실 모두 더하기 
#     print(base[n-1])

# # 2839번: 설탕 배달
# n = int(input()) # 설탕

# result = 0 # 봉지 수

# while n >= 0:
#     if n % 5 == 0: # 5로 나눈 나머지가 0인 경우
#         result += n // 5 # 5로 나눈 몫 추력
#         print(result)
#         break
#     n -= 3 # 설탕이 5의 배수가 될때까지 반복
#     result += 1 # 봉지 추가
# else:
#     print(-1) # while문이 거짓이 되면 -1 출력

#10757번 : 큰수 A+B
# A,B = map(int, input().split())
# print(A+B)

# 1978번 : 소수찾기
# n = int(input())
# num = list(map(int, input().split()))
# nk = 0 # 소수개수
# for i in num:
#   cnt = 0
#   if i == 1:  # 1이면 소수가 아님 
#     continue
#   for k in range(2,i+1): # 2부터 입력 수까지
#     if i%k == 0: #자기 자신 포함해서 1번만 나눠지면 소수!
#       nk += 1
      
# print(nk)
  
# 2581번 : 소수
# n = int(input())
# m = int(input())

# nk = []
# for i in range(n,m+1):
#   cnt = 0
#   if i == 1:
#     pass
#   elif i ==2:
#     nk.append(i)
#   else:
#     for k in range(2,i+1):
#         if i % k == 0:
#           cnt += 1
#           if cnt > 2:
#             break
#     if cnt == 1:
#       nk.append(i)

# if len(nk) == 0:
#   print('-1')
# else:      
#   print(sum(nk))
#   print(nk[0])

#11653번 : 소인수분해
# num = int(input())

# # 분해가 전부 될때까지 loop 돌립니다.
# while num != 1:
#     for i in range(2, num + 1):
#         # 나눠지면 출력하고,
#         # 다음을 위해 해당 수로 num을 나눠줍니다.
#         if(num % i == 0):
#             print(i)
#             num = num // i
#             break

#1929번 : 소수 구하기
# import math
# def isPrime(num):
#   if num == 1:
#     return False
#   n = int(math.sqrt(num)) # 여기가 핵심! 제곱근을 까지만 측정해서 시간 절약
#   for k in range(2,n+1):
#     if num % k == 0:
#       return False
#   return True

# m,n = map(int,input().split())
# for k in range(m,n+1):
#   if isPrime(k):
#     print(k)


#4948번: 베스트랑 공준
# import math
# import sys

# def isPrime(num):
#   if num == 1:
#     return False
#   n = int(math.sqrt(num)) # 여기가 핵심! 제곱근을 까지만 측정해서 시간 절약
#   for k in range(2,n+1):
#     if num % k == 0:
#       return False
#   return True

# all_list = list(range(2,246912)) # 문제에서 주어진 범위
# save_list=[]

# for i in all_list : # 주어진 범위 안의 소수들을 찾아서 저장해놓는다.
#     if isPrime(i):
#         save_list.append(i)

# num = int(sys.stdin.readline())

# while num != 0:
#     count = 0
#     for i in save_list: # 저장된 소수들 중,
#         if num < i <= num*2:
#             count += 1
#     print(count)
#     num = int(sys.stdin.readline())

# 9020번: 골드바흐의 추측
# 소수 집합 만들기
# nums = {x for x in range(2, 10_001) if x == 2 or x % 2 == 1}
# # nums = 2와 홀수로 이루어진 집합
# for odd in range(3, 101, 2): # 101 == int(math.sqrt(10_000)) + 1
#     nums -= {i for i in range(2 * odd, 10_001, odd) if i in nums}
#     # 홀수의 배수로 이루어진 집합을 빼줌

# # 골드바흐 수를 출력
# t = int(input())
# for _ in range(t):
#     even = int(input())
#     half = even//2  # 입력받은 짝수를 2로 나눈 몫을 구함. / 기호를 쓰면 실수가 됨.
#     for x in range(half, 1, -1):  # 차이가 적은 두 수를 구하기 위해서 큰수부터 꺼냄
#         if (even-x in nums) and (x in nums):  # even-x 와 x가 소수 집합에 포함 되었는지 확인
#             print(x, even-x)  # 작은수부터 출력
#             break
            
# 1085번 : 직사각형 탈출


