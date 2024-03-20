for i in range(1, 20001):
    s = 0 # 친화수의 초기값
    s1 = 0 # 친화수의 진약수의 합의 초기값
    for j in range(1,i): # 220의 진약수의 합(284)
        if i % j == 0:
            s = s + j
    for k in range(1,s): # 220의 진약수의 합(284)의 진약수의 합(220)
        if s % k == 0:
            s1 = s1 + k
    if i == s1 and i != s:
        print('{}의 친화수 {}'.format(i, s))
