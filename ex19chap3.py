print('맛나 식당에 오신 것을 환영합니다., 메뉴는 다음과 같습니다.')
print('1)햄버거')
print('2)치킨')
print('3)피자')
a=input('1에서 3까지의 메뉴 선택하세요:')
while a!='1' and a!='2' and a!='3':
    a=input('메뉴를 다시 입력하세요::')

    
while a=='1' or a=='2' or a=='3':
    break
if a=='1':
        print('햄버거를 선택했습니다')
elif a=='2':
          print('치킨을 선택했습니다')
elif a=='3':
          print('피자을 선택했습니다')
