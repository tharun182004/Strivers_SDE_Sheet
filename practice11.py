a=[8, 4, 1, 6, 7, 2, 5, 8]
n=len(a)

y=(n*(n+1))//2
yy=(n*(n+1)*(2*n+1))//6

x=0
xx=0

for i in range(n):
    x+=a[i]
    xx+=a[i]*a[i]

val1=x-y
val2=xx-yy
val3=val2//val1
A=(val1+val3)//2
B=val3-A

print(A,B)