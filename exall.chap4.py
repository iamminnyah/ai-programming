#4.1

def my_greet():
    print('환영합니다.')

my_greet()
my_greet()

#4.3

def max2(m,n):
    if m<n:
        return n
    else:
        return m

def min2(m,n):
    if m<n:
        return m
    else:
        return n

print('100과 200중 큰 수는 :', max2(100,200))
print('100과 200중 작은 수는 :', min2(100,200))

#4.5

def inch2cm(inch):
    for inch in range(1,6):
        print(inch, '인치', '=', 2.54*inch, '센티미터')
    

#4.7

a,b,c= input('세 수를 입력하시오 :').split()
a,b,c=int(a),int(b),int(c)

def mean3(a,b,c):
    return(a+b+c)/3

def max3(a,b,c):
    return max(a,b,c)

def min3(a,b,c):
    return min(a,b,c)

print(a,b,c, '의 평균값은', mean3(a,b,c))
print(a,b,c, '의 최댓값은', max3(a,b,c))
print(a,b,c, '의 최솟값은', min3(a,b,c))

#4.9

n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11 = input('정수를 여러개 입력하시오 :').split()
n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11 = int(n1), int(n2), int(n3), int(n4), int(n5), int(n6),int(n7),int(n8),int(n9),int(n10),int(n11)
nums= n1,n2,n3,n4,n5,n6,n7,n8,n9,n9,n10,n11

def mean_of_n(nums):
    return(n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11)/11

def max_of_n(nums):
    return max(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11)

def min_of_n(nums):
    return min(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11)

print('평균값은', mean_of_n(nums))
print("최댓값은", max_of_n(nums))
print("최솟값은", min_of_n(nums))

#4.11

x1 = int(input('x1 좌표를 입력하시오 :'))
y1 = int(input('y1 좌표를 입력하시오 :'))
x2 = int(input('x2 좌표를 입력하시오 :'))
y2 = int(input('y2 좌표를 입력하시오 :'))

def area(x1,y1,x2,y2):
    a = x2-x1
    b = y2-y1
    result = (a+b)/2
    return result

print('직각삼각형의 면적은', area(x1,y1,x2,y2))
               

#4.13

s = 12
def cube(s):
    return s ** 3

s1 = 20
def cube(s1):
    return s1 ** 3

w = 3
h = 5
l = 6
def cuboid(s):
    return w*h*l

r= 20
h = 10
def corn(s):
    return(1/3)*3.14*(r**2)*10

r = 15
def ball(r2):
    return (4/3)*3.14*(r**3)

r = 20
h = 10
def can(s):
    return 3.14*(r**2)*h

print('(1)모서리의 길이가 12인 정육면체:',cube(s))
print('(2)모서리의 길이가 20인 정육면체:',cube(s1))
print('(3)가로, 세로, 길이가 각각 3,5,6인 직육면체:',cuboid(s))
print('(4)반지름과 높이가 각각 20,10인 원뿔:',corn(s))
print('(5)반지름이 15인 구:',ball(r2))
print('(6)반지름과 높이가 각각 20,10인 원기둥:',can(s))

#4.15

def my_sort(*nums):
    a = list(nums)
    a.sort()
    print(f'결과;{a}')

my_sort(45, 3, 4, 56, 5)
my_sort(9, 8, 7, 6, 5, 4, 3)

#4.21

num = input('주민등록번호 첫 6숫자 형식 입력 :')
year = int(num[0:2])
month = int(num[2:4])
day = int(num[4:6])
if year>= 50:
    print(f"19{year}년 {month}월 {day}일")
else: print(f"20{year}년 {month}월 {day}월")

#4.27

def unit_fraction(frac):
    n = 1
    diff = 1.0
    while True:
        new_diff = abs(1/n - frac)
        if (new_diff <= diff):
            diff = new_diff
            print("frac = {:0.3f}, n = {:0.3f}, 1/n = {:0.3f}, diff = {:0.3f}".format(\
            frac, n, 1/n, diff))

        else:
            break
        n += 1
    return n - 1

f_val = float(input('1보다 작고 0보다 큰 소수를 입력하세요:'))

if f_val <= 0.0 or f_val > 1.0 :
    print('입력 오류입니다.')
else :
    nf = unit_fraction(f_val)
    print('가장 가까운 단위분수는 1/{0}이며, 이 값은 {1:.5f}입니다.'.format(nf,\
                                                          1/nf))
            
            
