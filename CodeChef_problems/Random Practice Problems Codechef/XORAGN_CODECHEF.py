#Question Link
#https://www.codechef.com/problems/XORAGN
t=int(input())
for a0 in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    for i in a:
        res=res^i
    print(2*res)
