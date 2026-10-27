# 一些整数可能拥有以下的性质：
# 性质 1：是偶数；
# 性质 2：大于 4 且不大于 12。
# 小 A 喜欢这两个性质同时成立的整数；Uim 喜欢这至少符合其中一种性质的整数；小 B 喜欢刚好有符合其中一个性质的整数；
# 正妹喜欢不符合这两个性质的整数。现在给出一个整数 x，请问他们是否喜欢这个整数？
#输出这 4 个人是否喜欢这个数字，如果喜欢则输出 1，否则输出 0，用空格分隔。输出顺序为：小 A、Uim、小 B、正妹。
print("请输入数字")
num=int(input())
if num%2==0:
    even=1;
else :
    even=0
if (num>4) and (num<=12):
    size=1
else:
    size=0

a=1 if(even==1) and (size==1) else 0
uim=1 if(even==1) or (size==1) else 0
b=1 if((even==1) and (size==0)) or ((even==0) and (size==1)) else 0
zheng=1 if(even==0) and (size==0) else 0
print(a,uim,b,zheng)