#!/usr/bin/python3

import math
import random

#print("pi:",math.pi,"\n")


# Calculated a Random N digit number
def calc(n):
    x=""
    for i in range(n):
        x+=str(random.randint(0,9))
    return x

# Append a digit to the end of a integer, i.e. append(234,5)=2345
def append(A,x):
    return str(A)+str(x)

# Multiply an integer of arbitary length by an integer of fixed length
def mul(A,x):
    Ans=""
    r=0
    #print("Start")
    #print(A)
    for i in range(len(A)-1,-1,-1):
        Ans+=str((int(A[i])*x+r)%10)
        #print(A[i],"*",2,"+",r,"=",int(A[i])*x,"+",r,"=",Ans)
        r=(int(A[i])*x+r)//10
    #print("End")
    #print(Ans)
    if r!=0:
        return str(r)+Ans[::-1]
    else:
        return Ans[::-1]

def sub(A,B):
    A=A.zfill(max(len(A),len(B)))
    B=B.zfill(max(len(A),len(B)))
    C=0
    if B>A:
        C=B
        B=A
        A=C
    #print(" ",A)
    #print("-",B)
    r=0
    Ans=""
    for i in range(len(A)-1,-1,-1):
        if  int(A[i])<(int(B[i])+r):
            #print("10+",A[i],"-",B[i],"+",r,"=",10+int(A[i])-(int(B[i])+r))
            Ans+=str(10+int(A[i])-(int(B[i])+r))
            r=1
        else:
            #print(A[i],"-",B[i],"+",r,"=",int(A[i])-(int(B[i])+r))
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
    #print(" ",A)
    #print("+",B)
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
    ncol=10
    nrow=len(x)//(nblock*ncol)
    nleft=len(x)%(nblock*ncol)
    for i in range(0,nrow,1):
        print("{:08d}".format(count),end=" : ")
        for j in range(0,ncol,nblock):
            print(x[(i*j):(i*j+nblock)],end=" ")
            print("",end=" ")
            count+=1
        print("\\\\")


def test_add():
    #N=calc(5)
    #MyAns=mul(append(N,2),2)
    #print(MyAns==str(check(N,2)))
    A=calc(2)
    B=calc(6)
    Ans=add(A,B)
    print(Ans)
    print(str(int(A)+int(B)))
    print(Ans==str(int(A)+int(B)))

def fn(A,x):
    #return (10*A+x)*x
    return mul(append(A,x),x)

def root(A,B):
    X=0
    #print("Start",A,B)
    for i in range(1,10):
        #print(X,fn(A,X+1),fn(B,X+1))
        if int(fn(A,X+1))<B:
            X+=1
            #print("--",X)
            continue
        else:
            #print("->",X)
            break
    #print("End",X)
    return X

def main():
    n=100
    Xs=[0]*n
    Xs[0]=2
    A=0
    B=5
    C=4
    #print("A0",A,"B0",B,"C0",C,"=","X0",Xs[0])
    for i in range(1,n):
        A=10*A+2*Xs[i-1]
        B=B*100-C*100
        Xs[i]=root(A,B)
        C=int(fn(A,Xs[i]))
        #print("A"+str(i),A,"B"+str(i),B,"C"+str(i),C,"=","X"+str(i),Xs[i])
    #print(''.join([str(i//10) for i in range(len(Xs))]))
    #print(''.join([str(i%10) for i in range(len(Xs))]))
    print(''.join([str(x) for x in Xs]))

if __name__=="__main__":
    main()
