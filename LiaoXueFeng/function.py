# -*- coding: utf-8 -*-
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)

# print fact(10)

## 尾递归的形式

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print fact(10)

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print L

## 切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print [L[0], L[1], L[2]]
print L[0:3]
print L[:3]
print L[1:3]
print L[-2:-1]
print L[-2:]
print L[:-1]

L1 = range(100)
print L1[:10]
print L1[-10:]
print L1[10:20]
print L1[:10:2]
print L1[::5]
print L1[:]
print (0, 1, 2, 3, 4, 5)[:3]
print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]


## 列表生成式
L2 = []
for x in xrange(1,11):
    L2.append(x*x)
print L2
