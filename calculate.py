import random
from fractions import Fraction
operation = ['+', '-', '*', '/']   #四则运算的符号
global f
def integer_score():
    #rand = operation[random.randint(0,3)]
    number = random.randint(1,4)     #随机产生的表达式长度
    f = ''
    for i in range(number):
        a = random.randint(1,20)       #随机产生的表达式中的数
        rand = operation[random.randint(0, 3)]     #随机选择一个四则运算中的符号
        if rand == '/':
            b = random.randint(a, 20)               #随机产生的真分数的分母
            f += str(a) + rand + str(b)               #数与符号相连
            rand = operation[random.randint(0, 2)]     #随机选择一个四则运算中的符号
            f += rand
        else:
            f += str(a) + rand
        #print(a,rand,end='')
    b = random.randint(1, 20)
    f += str(b)                     #得到完整的表达式
    n = eval(f)                      #得到表达式的结果
    n = Fraction('{}'.format(n)).limit_denominator()    #小数转化为分数
    if n > 0:
        print('题目：')
        print(f,'=')
        print('请输出答案：')
        x = Fraction('{}'.format(eval(input()))).limit_denominator()
        if n == x:                  #输入的数与表达式比较
            print(True)
        else:
            print(False)
            print('正确的答案为：',n)
    else:
        integer_score()
def integer():
    # rand = operation[random.randint(0,3)]
    number = random.randint(1, 3)
    f = ''
    for i in range(number):
        a = random.randint(1, 10)
        rand = operation[random.randint(0, 3)]
        f += str(a) + rand
    b = random.randint(1, 10)
    f += str(b)
    n = eval(f)
    if isinstance(n, int) and n > 0:
        print('题目：')
        print(f, '=')
        print('请输出答案：')
        x = eval(input())
        if n == x:
            print(True)
        else:
            print(False)
            print('正确的答案为：', n)
    else:
        integer()
def score():
    op = ['+', '-']
    number = random.randint(1, 3)
    f = ''
    for i in range(number):
        a = random.randint(1, 10)
        b = random.randint(a, 10)
        rand = op[random.randint(0, 1)]
        f += str(a) + '/'+ str(b)+rand
    a = random.randint(1, 10)
    b = random.randint(a, 10)
    f += str(a) + '/'+ str(b)
    n = eval(f)
    n = Fraction('{}'.format(n)).limit_denominator()
    if n > 0:
        print('题目：')
        print(f,'=')
        print('请输出答案：')
        x = Fraction('{}'.format(eval(input()))).limit_denominator()
        if n == x:
            print(True)
        else:
            print(False)
            print('正确的答案为：',n)
    else:
        score()

if __name__ == '__main__':
    while True:
        print('选择你想做的题目：')
        print('0(退出)1(分数题目)，2（整数题目),3(综合题目)')
        m = int(input())
        if m == 1:
            score()
        elif m == 2:
            integer()
        elif m == 3:
            integer_score()
        elif m == 0:
            exit()
        else:
            print('请重新输入你的选择')

#isinstance(1, int)