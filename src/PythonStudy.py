# 实例1
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                print(i, j, k)

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值
# reverse用来设置排序方式
l = []
for i in range(3):
    x = int(input('integer: \n'))
    l.append(x)
l.sort(reverse=True)
print(l)


# 题目：斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

def fip(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


print(fip(10))

# 题目：将一个列表的数据复制到另一个列表中。
# 程序分析：使用列表[:]。

a = [1, 2, 3, 4, 5]
b = a[:]
print(b)

# 题目：输出 9*9 乘法口诀表。
# 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。

for i in range(1, 9):
    print()
    for j in range(1, i + 1):
        print("%d * %d = %d" % (i, j, i * j), end=',')

# 题目：暂停一秒输出。
# 程序分析：使用 time 模块的 sleep() 函数。
# 以秒为单位

import time

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(1)

# 题目：暂停一秒输出，并格式化当前时间。

import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print(time.time())
time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。

import string

line = input('请输入：')
print(len(line))
letters = 0
space = 0
digit = 0
others = 0
count = 0
while i < len(line):
    c = line[i]
    i += 1
    if c.isspace():
        space += 1
    if c.isdigit():
        digit += 1
    if c.isalpha():
        letters += 1
    else:
        others += 1
print('char = %d,space = %d,digit = %d,others = %d' % (letters, space, digit, others))
