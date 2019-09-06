#!/usr/bin/python3

import sys
from decimal import *

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

def main():
    dp=int(sys.argv[1])
    getcontext().prec = dp
    fmt('{:f}'.format(((1+Decimal(5).sqrt())/2)*10**dp))

if __name__=="__main__":
    main()
