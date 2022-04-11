# -*- coding: utf-8 -*-
"""GCD_Algorithm

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-pMBK9scH4ICYR18ZGpHYb1Oxs0fbPb8
"""

## 뺄셈 풀이
def gcd_sub(a,b):
    while a != 0 and b != 0:
        if a>b:
            a = a-b
        else:
            b = b-a

    return a+ b

results = gcd_sub(5,20)
print("최대공약수:", results)

##나눗셈 풀이
def gcd_mod(c,d):
    while c != 0 and d != 0:
        if c>d:
            c = c/d
        else:
            d = d/c
    return c + d

#res = gcd_mod(2,6)
#print("최대공약수:", res)

##재귀 함수
def gcd_rec(p, q):
    if q == 0:
        return p
    else:
        return gcd_rec(q, p % q)

result = gcd_rec(10, 12)
print('최대공약수:',result)