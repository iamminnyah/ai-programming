
n = int(input('숫자를 입력하세요: '))
s = 0
for i in range(1, n+1):
    s+= i**2
    i+=1
    
print('결과는 {} 입니다.'.format(s))
