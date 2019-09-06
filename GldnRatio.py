#!/usr/bin/python3

import sys
import math
import random

# Calculated a Random N digit number
def calc(n):
    x=""
    for i in range(n):
        x+=str(random.randint(0,9))
    return x

# Append a digit to the end of a integer, 
# i.e. append(234,5)=2345
# i.e. append(234,0)=2340
# but  append(0,0)=0

def append(A,x):
    if A=="0":
        return "0"
    else:
        return str(A)+str(x)

# Multiply an integer of arbitary length by an integer of fixed length (1)
def mul(A,x):
    Ans=""
    r=0
    for i in range(len(A)-1,-1,-1):
        Ans+=str((int(A[i])*x+r)%10)
        r=(int(A[i])*x+r)//10
    if r!=0:
        return str(r)+Ans[::-1]
    else:
        return Ans[::-1]

# Divide an integer of arbitary length by a number (just two really)
def div(A,x):
    Ans=""
    r=0
    for i in range(0,len(A),1):
        Ans+=str((int(A[i])+r*10)//x)
        r=(int(A[i])+r*10)%x
    if r!=0:
        return Ans+str(int(r/x*10))
    else:
        return Ans

def sub(A,B):
    A=A.zfill(max(len(A),len(B)))
    B=B.zfill(max(len(A),len(B)))
    C=0
    if B>A:
        C=B
        B=A
        A=C
    r=0
    Ans=""
    for i in range(len(A)-1,-1,-1):
        if  int(A[i])<(int(B[i])+r):
            Ans+=str(10+int(A[i])-(int(B[i])+r))
            r=1
        else:
            Ans+=str(int(A[i])-(int(B[i])+r))
            r=0
    if C==0:
        return Ans[::-1].lstrip("0")
    else:
        return "-"+Ans[::-1].lstrip("0")

def add(A,B):
    A=A.zfill(max(len(A),len(B)))
    B=B.zfill(max(len(A),len(B)))
    r=0
    Ans=""
    for i in range(len(A)-1,-1,-1):
        if  int(A[i])+(int(B[i])+r)>9:
            Ans+=str((10+int(A[i])+(int(B[i])+r))%10)
            r=1
        else:
            Ans+=str(int(A[i])+(int(B[i])+r))
            r=0
    if r==0:
        return Ans[::-1].lstrip("0")
    else:
        return str(r)+Ans[::-1]

def isneg(N):
    N[0]=="-"
        
def check(A,x):
    return (int(A)*10+int(x))*int(x)

def fmt(x):
    count=0
    nblock=10
    ncol=5
    nrow=len(x)//(nblock*ncol)
    nleft=len(x)%(nblock*ncol)
    print("{:08d}:".format(count)+str(x[0])+".",end="")
    for j in range(0,ncol,1):
        print(x[1+(j*nblock):(1+(j+1)*nblock)],end=" ")
        count+=nblock
    print("\\\\")
    for i in range(1,nrow,1):
        print("{:08d}".format(count),end=":  ")
        for j in range(0,ncol,1):
            print(x[(1+i*ncol*nblock+j*nblock):(1+(i*ncol*nblock)+(j+1)*nblock)],end=" ")
            count+=nblock
        print("\\\\")

# Less Than
def lt(A,B):
    if len(A)<len(B):
        return True
    elif len(A)>len(B):
        return False
    else:
        return A<B

def fn(A,x):
    return mul(append(A,x),x)

def root(A,B):
    X=0
    for i in range(1,10):
        if lt(fn(A,X+1),B):
            X+=1
            continue
        else:
            break
    return X

def main():
    n=int(sys.argv[1])
    Xs=[0]*n
    Xs[0]=2
    A="0"
    B="5"
    C="4"
    for i in range(1,n):
        if i%50==0:
            sys.stderr.write(str(i)+"\n")
        A=(add(append(str(A),"0"),str(Xs[i-1]*2)))
        B=(sub(append(str(B),"00"),append(C,"00")))
        Xs[i]=root(A,B)
        C=fn(A,Xs[i])
    # Add one to sqrt(5)
    Xs[0]=3
    sqrt5plusone=''.join([str(x) for x in Xs])
    sqrt5plusone_divby2=str(div(sqrt5plusone,2))

    #print("py")
    #print('{:f}'.format(((1+math.sqrt(5))/2)*10**300))
    #print("hand")
    #print(sqrt5plusone_divby2)
    fmt(sqrt5plusone_divby2)

if __name__=="__main__":
    main()
