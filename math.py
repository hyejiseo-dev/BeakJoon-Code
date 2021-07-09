#2869번 : 달팽이는 올라가고 싶다
a,b,v = map(int,input().split(' '))
day = 0 #올라가는데 걸리는 일수
h = v-a 

if h % (a-b) == 0: 
   day = int(h/(a-b)+1)
else:
   day = int(h/(a-b)+2)

print(day)

