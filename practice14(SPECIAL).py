x,n=2,-10
nn=n
ans=1

if nn<0:
    nn=nn*-1

while nn>0:
    if nn%2==0:
        x=x*x
        nn=nn//2

    else:
        ans=ans*x
        nn-=1

if n<0:
    ans=1/ans
    print(ans)
else:
    print(ans)
