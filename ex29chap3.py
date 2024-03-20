tk = 500
while tk >= 50:
    d = int(input('충전 또는 사용한 연료를  +/- 기호와 함께 입력하시오 : '))
    tk = tk + d
    print('현재 탱크양은 {} 입니다'.format(tk))

print('경고 : 연료가 10% 미만이니 충전하세요!')

#30
cal = int(input('1)덧셈 2)뺄셈 3)곱셈 4)나눗셈\n어떤 연산을 원하는지 번호를 입력하세요 : '))
while cal not in [1, 2, 3, 4]:
    print('잘못 입력하였습니다.')
    cal = int(input('1)덧셈 2)뺄셈 3)곱셈 4)나눗셈\n어떤 연산을 원하는지 번호를 입력하세요 : '))
    
n1 = int(input('연산을 원하는 첫 번째 숫자 두 개를 입력하세요\n'))
n2 = int(input())

if cal == 1:
    print('{} + {} = {}'. format(n1, n2, n1+n2))
elif cal == 2:
    print('{} - {} = {}'. format(n1, n2, n1-n2))
elif cal == 3:
    print('{} * {} = {}'. format(n1, n2, n1*n2))
else:
    print('{} / {} = {}'. format(n1, n2, n1/n2))
