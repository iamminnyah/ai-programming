a_num = []
for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            if a**3+b**3+c**3 == a*100+b*10+c:
                a_num.append(a*100+b*10+c)
         
print('세 자리 암스트롱 수 : ', a_num)
