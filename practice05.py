#用高精度计算出 S=1!+2!+3!+⋯+n!（n≤50）。
#其中 ! 表示阶乘，定义为 n!=n×(n−1)×(n−2)×⋯×1。例如，5!=5×4×3×2×1=120。
print("请输入一个整数")
n=int(input())
sum=0
for i in range(1,n+1):#如果不规定从1 开始,会多算0的阶乘
    s=1
    for j in range(1,i+1):
        s=j*s
    sum=sum+s
print(sum)
