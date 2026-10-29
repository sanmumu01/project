#试计算在区间 1 到 n 的所有整数中，数字 x（0≤x≤9）共出现了多少次？例如，在 1 到 11 中，
# 即在 1,2,3,4,5,6,7,8,9,10,11 中，数字 1 出现了 4 次。
print("请输入查询范围的上限和目标对象")
n,x=map(int,input().split())
appearance=0
for i in range(1,n+1):
    j=i
    while j>0:
        if j%10==x:
            appearance+=1
        j=j//10#不管余数是不是目标对象都削去个位
print(appearance)