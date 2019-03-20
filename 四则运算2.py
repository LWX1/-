import random
from fractions import Fraction
operation = ['+', '-', '*', '/']   #四则运算的符号
global f
question = []
result = []
answer = []
def result_integer(f, m):
    try:
        n = eval(f)
        n = Fraction('{}'.format(n)).limit_denominator()  # 把表达式的结果转成分数
        if n > 0:  # 判断结果是否大于0，否则重新产生表达式
            #print('题目：')
            question.append(f)
            result.append(n)
            #print('请输出答案：')
            #x = Fraction('{}'.format(eval(input()))).limit_denominator()
        else:
            integer()
    except:
        integer(m)
def func_integer(number):
    f = ''
    ch = []
    rand = random.randint(0, 1)  #选择内嵌或外嵌括号
    if number != 1:         #避免一个表达式也产生括号
        if rand == 0:
            ch.append('(')
            op = operation[random.randint(0, 1)]
            ch.append(random.randint(1, 10))
            ch.append(op)
            ch.append(random.randint(1, 10))
            ch.append(')')
        else:
            op = operation[random.randint(0, 3)]
            if op == '/':
                a = random.randint(1, 10)
                ch.append(a)
                ch.append(op)
                ch.append(random.randint(a, 10))
            else:
                ch.append(random.randint(1, 10))
                ch.append(op)
                ch.append(random.randint(1, 10))
    else:
        op = operation[random.randint(0, 3)]
        if op == '/':
            a = random.randint(1, 10)
            ch.append(a)
            ch.append(op)
            ch.append(random.randint(a, 10))
        else:
            ch.append(random.randint(1, 10))
            ch.append(op)
            ch.append(random.randint(1, 10))
    for i in ch:       #把产生表达式当成一个整体
        f += str(i)
    return f
def integer(n):
    ch = []                               #存储表达式
    number = random.randint(1, 4)        #随机产生表达式的数量
    for i in range(number):
        rand = random.randint(0, 1)       #随机产生0和1 判断是否使用括号
        a = func_integer(number)          #调用表达式产生函数，产生表达式
        if rand == 0:
            op = operation[random.randint(0,3)]    #产生*，/来连接有括号的表达式，避免产生+，—
            rand = random.randint(0, 1)            #随机产生0和1 判断是否使用内嵌括号或外嵌括号
            if i != number - 1:                    #避免开始和结尾用无意义的括号
                if rand == 0:
                    ch.append('(')
                    ch.append(a)
                    ch.append(op)
                    ch.append(random.randint(1,10))
                    ch.append(')')
                    ch.append(operation[random.randint(0, 3)])
                else:
                    ch.append(a)
                    ch.append(operation[random.randint(0, 3)])
            else:
                ch.append(a)
                ch.append(operation[random.randint(0, 3)])
        else:
            ch.append(a)
            ch.append(operation[random.randint(0, 3)])

    f = ''
    for k,i in enumerate(ch):             #把列表中的所有值用f一个个连起来
        if k != len(ch)-1:
            f += str(i)
    result_integer(f, n)                      #调用输出函数
if __name__ == '__main__':
    print('输入你想做几道题目')
    n = int(input())
    for i in range(n):
        integer(n)
    print('题目：')
    for k, i in enumerate(question):
        print(k + 1,':',i,'=')
    print('请输入你的答案：')
    for i in range(n):
        x = Fraction('{}'.format(eval(input()))).limit_denominator()
        if x == result[i]:
            answer.append('√')
        else:
            answer.append('×')
    for k, i in enumerate(answer):
        print(k + 1, i)

