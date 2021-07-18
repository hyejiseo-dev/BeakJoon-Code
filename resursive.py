#재귀 함수
#재귀 함수
#10872번 : 팩토리얼
# def factorial(n):
#     result = 1
#     if n > 0 :
#         result = n * factorial(n-1)
#     return result

# n = int(input())
# print(factorial(n))

#10870번 : 피보나치 수열
# def fibo(n):
#   if n <= 1:
#     return 1
#   else:
#     return fibo(n-1)+fibo(n-2)
# n = int(input())
# print(fibo(n))

# # 2447번: 별 찍기
# def star(n):
#   if n>=3:
#     for i in range(3):
#       for j in range(3):
#           print('*',end='\n')

# print(star(3))

#11729번: 하노이탑 이동순서
def hanoi(n,a,b,c):
  if n == 1:
    move.append([a,c])
  else:
    hanoi(n-1,a,c,b)
    move.append([a,c])
    hanoi(n-1,b,a,c)

move = []
hanoi(int(input()),1,2,3)
print(len(move))
print("\n".join([' '.join(str(i) for i in row) for row in move]))
