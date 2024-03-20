n = int(input('숫자를 입력하시오: '))
c = 0
if n%2 == 0 and n != 2:
    print(n,'은 소수가 아닙니다.')
    
else:
    for i in range(3, n, 2):
        if n%i == 0:
            c += 1

    if c == 0:
        print(n, '은 소수입니다.')
    else:
        print(n,'은 소수가 아닙니다.')
