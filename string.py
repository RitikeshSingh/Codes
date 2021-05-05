a=str(input())
b=str(input())
c=str(input())
q=0
s=0
r=0
A=len(a)
B=len(b)
C=len(c)
if A<B and A<C:
    z=a
elif B<C:
    z=b
else:
    z=c
if z==a[-len(z):]:
    q=q+1
if z==b[-len(z):]:
    s=s+1
if z==c[-len(z):]:
    r=r+1
if q==1 and r==1 and s==1:
    ans=(A+B+C) - 3*len(z)
else :
    ans = (A+B+C)
print(ans)
print(c[-len(z):])
