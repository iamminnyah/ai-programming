#9.1

num1 = Add(133)
num2 = Add(334)
result = num1 + num2
print(result)

num1 = mul(133)
num2 = mul(334)
result1 = num1 * num2
print(result1)

num1 = sub(133)
num2 = sub(334)
result2 = num1 + num2
print(result2)

a = truediv(123)
b = truediv(3)
result3 = a/b
print(result3)

#9.5

class check:
    a = 1
    b = 1
    c = 2
    d = 3
    e = 3
    def __init__(self,num):
        self.num = num
    def c1(self,other):
        if self.num == other.num:
            return True
        else :
            return False

        check1 = check(check.a)
        check2 = check(check.b)
        check3 = check1.c1(check2)
        print(check3)

#9.7

class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        print('my dig의 이름은 {} 나이는 {]살입니다.'.format(self.name,self.age))
my_dog = dog('Mango',3)
print(my_dog)

#9.9
class Counter:
    def __init__(self,number):
        self.number = number
        if self.number >= 100 or self.number <= -1:
            self.number = 0
    def reset(self) :
        self.number = 0

    def inc(self):
        self.number >= 100:
            self.number = 0
    def dec(self):
        self.number = -1
        if self.number <= -1:
            self.number = 0

    def __add__(self,other):
        if (self.number + other.number)>100:
            return 0
        else:
            a = self.number + other.number
            return a
    def __sub__(self,other):
        if self.number-other.number>=-1:
            return 0
        else:
            a=self.number-other.number
            return a

class counter:
    def __sub__(self,other):
    def __str__(self):
        return 'c({})'.format(a)
c1 = Counter(10)
c2 = Counter(20)
c3 = c1 + c2
c4 = c1 - c2
print('c3=',c3)
print('c4=',c4)

#9.11
class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.korean_quiz = 0
        self.math_quiz = 0
        self.science_quiz = 0
        self.total_score = 0

    def get_name(self):
        return self.name

    def get_student_id(self):
        return self.student_id

    def set_korean_quiz(self, value):
        self.korean_quiz += value
        return self.korean_quiz

    def set_math_quiz(self,value):
        self.science_quiz += value
        return self.science_quiz

    def set_total_score(self,value):
        self.total_score += value
        return self.total_score

    def __str__(self):
        return '학번:{}, 이름:{}, 국어성적{}, 과학성적:{}, 수학성적:{}, 합계:{}, 평균:{}'.format(self.name,self.student_id,self.korean_quiz,self.science_quiz, self.math_quiz, self.total_score, (self.korean_quiz+self.math_quiz+self.science_quiz)
                                                                             
name = input('학생의 이름을 입력하세요:')
student_id = input('학생의 학번을 입력하세요:')
korean_quiz = int(input('학생의 국어성적을 입력허세요:'))
math_quiz = int(input('학생의 수학성적을 입력하세요:'))
