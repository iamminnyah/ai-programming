a,b =map(int,input('점의 좌표 x,y를 입력하시오:').split())

d = ((a-3)**2 + (b-4)**2)**0.5

if d>10:
    print('원 외부에 있음')
elif d<10:
    print('원 내부에 있음')
else:
    print('원 위에 있음')
