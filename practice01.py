#给定由 n 个正整数组成的序列 a 1,a 2,⋯,a n和 m 个区间 [l i,r i]，分别求这 m 个区间的区间和。
import numpy as np
print("请输入元素的个数")
num=int(input())

print("请输入每个元素的大小")
arr1=np.array(list(map(int,(input().split()))))#按空格分割开数字.转换类型

print("请输入上下限")
low,hight=map(int, input().split())

while 1>low:
    print("下限不符合要求,请重新输入")
    low=int(input())
while num<hight:
    print('上限不符合要求,请重新输入')
    hight=int(input())

sum=np.sum(arr1[low - 1:hight])
print(sum)
